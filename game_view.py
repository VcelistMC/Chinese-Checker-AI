import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QToolButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QRegion
from game_model import Game

from game_controller import GameManager

button_style = "\n    color: #333;\n        border-radius: 30px;\n    border-style: outset;\n    background: {};\n    padding: 5px;\n    "

class Cell(QPushButton):
    def __init__(self, parent, ind, color):
        super(Cell, self).__init__(parent)
        self.ind = ind
        self.setStyleSheet(button_style.format(color))
        self.setFixedSize(40,40)
        x = 40 if ind[1] == 0 else ind[1] * 32
        y = 40 if ind[0] == 0 else ind[0] * 32
        print(x,y)
        self.move(x, y)

    def resizeEvent(self, event):
        self.setMask(QRegion(self.rect(), QRegion.Ellipse))
        

class GameView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.model = Game()
        self.controller = GameManager(self.model, self)

        self.setMinimumSize(QSize(801, 801))
        self.setMaximumSize(QSize(801, 801))
        self.setStyleSheet("background:url(res/board.jpg)")

        # circle = Cell(self, [1,11], "yellow")
        # circle.clicked.connect(self.buttonClicked)

    # send input to controller here
    def buttonClicked(self):
        print(self.sender().ind)
    
    # re-render the board
    def notify(board):
        pass