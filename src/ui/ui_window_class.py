"""class_uiwindow"""
# pylint: disable-msg=E0611, C0103

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget

from message_text_area_class import MessagesTextArea #provides the text area widget


class UiWindow(QMainWindow):
    """this class creates a main window"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("IHRS Database UI") #set window title
        self.create_messages_layout()

    def create_messages_layout(self):
        """this is the initial layout of the window - to display the message"""

        #create widgets
        self.messageTextArea = MessagesTextArea("this is the message text", "this is the groupbox label")
        self.nextPushButton = QPushButton("Next")
        self.previousPushButton = QPushButton("Previous")

        #create layout to hold the widges
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.messageTextArea)
        self.initial_layout.addWidget(self.nextPushButton)
        self.initial_layout.addWidget(self.previousPushButton)

        #create widget to hold layout
        self.messageWidget = QWidget()
        self.messageWidget.setLayout(self.initial_layout)

        #set the central widget
        self.setCentralWidget(self.messageWidget)

def main():
    """this is the main function"""

    ihrs_ui = QApplication(sys.argv) #create new application
    ui_window = UiWindow() #create new instance of main window
    ui_window.show() #make instance visable
    ui_window.raise_() #raise instance to top of window stack
    ihrs_ui.exec_() #monitor application for events

if __name__ == "__main__":
    main()
