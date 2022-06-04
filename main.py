from game_view import GameView
from PyQt5.QtWidgets import QMainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from game_controller import GameManager

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = GameView()
    diff = int(input("Enter Difficulty Level: (1:- Easy, 3:- Medium, 5: Hard) (any number in between should also work) "))
    game_controller = GameManager(mainWin.model, mainWin, diff)
    print(mainWin.controller.difficulty)
    mainWin.show()
    sys.exit(app.exec_())
