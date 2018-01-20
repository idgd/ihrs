"""class_uiwindow"""
# pylint: disable-msg=E0611, C0103

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)

from api.ihrs_api import (DatabaseConnection) # provides database methods
from ui.message_text_area_class import MessagesTextArea  # provides the text area widget

class UiWindow(QMainWindow):
    """this class creates a main window"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("IHRS Database UI") #set window title
        self.setGeometry(500, 250, 500, 500)
        self.databaseConnection = DatabaseConnection() #get database connection
        self.messageIndex = 0
        self.create_messages_layout(self.messageIndex) #sets the message window as the main window

    def create_messages_layout(self, messageIndex=0):
        """this is the initial layout of the window - to display the message"""

        #retrun a list of database documents
        self.messages = self.databaseConnection.return_list()
        initialMessageText = self.messages[messageIndex]["text"]
        initialMessageId = str("Message ID: ") + str(self.messages[messageIndex]["_id"])

        #create widgets
        self.messageTextArea = MessagesTextArea(initialMessageText, initialMessageId)
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

        #connections
        self.nextPushButton.clicked.connect(self.next_message)
        self.previousPushButton.clicked.connect(self.previouse_message)

    def next_message(self):
        """this method returns the next message in the database"""

        if self.messageIndex != self.messages.count()-1:
            self.messageIndex = self.messageIndex + 1
        self.create_messages_layout(self.messageIndex)

    def previouse_message(self):
        """this method returns the previous message in the database"""

        if self.messageIndex != 0:
            self.messageIndex = self.messageIndex - 1
        self.create_messages_layout(self.messageIndex)

def main():
    """this is the main function"""

    ihrs_ui = QApplication(sys.argv) #create new application
    ui_window = UiWindow() #create new instance of main window
    ui_window.show() #make instance visable
    ui_window.raise_() #raise instance to top of window stack
    ihrs_ui.exec_() #monitor application for events

if __name__ == "__main__":
    main()
