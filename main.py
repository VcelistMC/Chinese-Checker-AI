from game_view import GameView
from PyQt5.QtWidgets import QMainWindow
import sys
from PyQt5 import QtCore, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = GameView()
    mainWin.show()
    sys.exit( app.exec_() )
    #comment