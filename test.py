"""This code is a test"""

import sys
from PyQt5 import QtWidgets

APP = QtWidgets.QApplication(sys.argv)

WINDOW = QtWidgets.QWidget()
WINDOW.setGeometry(50, 50, 500, 300)
WINDOW.setWindowTitle("If you see this, it works!")

WINDOW.show()

input("PRESS ANY KEY TO END...")
