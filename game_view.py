from os import system
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QRegion, QFont
from game_model import Game

from game_controller import GameManager

button_style = "\n    color: #333;\n        border-radius: 30px;\n    border-style: outset;\n    background: {};\n    padding: 5px;\n    "

class Cell(QPushButton):
    size = 40
    def __init__(self, parent, ind, color):
        super(Cell, self).__init__(parent)
        self.ind = ind
        self.setColor(color)
        self.setFixedSize(40,40)
        x = ind[1] * 40
        y = ind[0] * 40
        self.move(x, y)

    def resizeEvent(self, event):
        self.setMask(QRegion(self.rect(), QRegion.Ellipse))

    def setColor(self, color):
        self.setStyleSheet(button_style.format(color))
        



class GameView(QMainWindow):

    def changeTurn(self, player):
        if player == "AI":
            self.turnLbl.setText("AI's Turn")
            self.turnLbl.setStyleSheet("color: red")
        else:
            self.turnLbl.setText("Your Turn")
            self.turnLbl.setStyleSheet("color: blue")

    def __init__(self, diff):
        QMainWindow.__init__(self)
        
        self.model = Game()
        self.controller = GameManager(self.model, self, diff)
        self.buttons = {}
        self.setMinimumSize(QSize(self.model.cols * Cell.size, (self.model.rows + 3) * Cell.size))
        self.setMaximumSize(QSize(self.model.cols * Cell.size, (self.model.rows + 3) * Cell.size))
        self.setStyleSheet("background: black")
        self.turnLbl = QLabel(self)
        self.turnLbl.move(0, 40 * 17)
        self.turnLbl.setGeometry(0, 40*17, 200, 200)
        self.turnLbl.setText("Your Turn")
        self.turnLbl.setFont(QFont("Ariel", 20))
        self.turnLbl.setStyleSheet("color: blue")
        
        for row in range(self.model.rows):
            for col in range(self.model.cols):
                cell = self.model.getBall(row, col)
                button = None
                if cell != " ":
                    if cell == "R":
                        button = Cell(self, [row, col], "red")
                    elif cell == "B":
                        button = Cell(self, [row, col], "blue")
                    elif cell == ".":
                        button = Cell(self, [row, col], "white")
                    self.buttons.setdefault((row, col), button)
                    button.clicked.connect(self.buttonClicked)
    
    # send input to controller here
    def buttonClicked(self):
        ind = self.sender().ind
        self.controller.move(ind)
    
    def declareWinner(self, winner):
        dlg = QMessageBox(self)
        dlg.setStyleSheet("background: white")
        dlg.setWindowTitle("We have a winner!")
        dlg.setText("{} won".format(winner))
        button = dlg.exec()

        if button == QMessageBox.Ok:
            sys.exit()

    # re-render the board
    def update(self):
        currInd = 0
        for row in range(self.model.rows):
            for col in range(self.model.cols):
                cell = self.model.getBall(row, col)
                if cell != " ":
                    if cell == "R":
                        self.buttons[(row, col)].setColor("red")
                    elif cell == "B":
                        self.buttons[(row, col)].setColor("blue")
                    else:
                        self.buttons[(row, col)].setColor("white")
                    currInd+=1
    
    def setValidMoves(self, moves):
        for move in moves:
            self.buttons[tuple(move)].setColor("orange")