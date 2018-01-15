"""This code is a test"""
# pylint: disable-msg=E0611

import sys

from PyQt5.QtWidgets import QApplication, QWidget

APP = QApplication(sys.argv)

WINDOW = QWidget()
WINDOW.setGeometry(50, 50, 500, 300)
WINDOW.setWindowTitle("If you see this, it works!")

WINDOW.show()

input("PRESS ANY KEY TO END...")
