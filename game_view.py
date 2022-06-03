import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QRegion
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
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.model = Game()
        self.controller = GameManager(self.model, self)
        self.buttons = {}
        self.setMinimumSize(QSize(self.model.cols * Cell.size, self.model.rows * Cell.size))
        self.setMaximumSize(QSize(self.model.cols * Cell.size, self.model.rows * Cell.size))
        self.setStyleSheet("background: black")
        
        for row in range(self.model.rows):
            for col in range(self.model.cols):
                cell = self.model.getBall(row, col)
                button = None
                if cell != " ":
                    if cell == "R":
                        button = Cell(self, [row, col], "red")
                    elif cell == "B":
                        button = Cell(self, [row, col], "blue")
                    else:
                        button = Cell(self, [row, col], "white")
                    self.buttons.setdefault((row, col), button)
                    button.clicked.connect(self.buttonClicked)
    
    # send input to controller here
    def buttonClicked(self):
        ind = self.sender().ind
        self.controller.move(ind)
    
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
            self.buttons[tuple(move)].setColor("cyan")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = GameView()
    mainWin.show()
    sys.exit( app.exec_() )