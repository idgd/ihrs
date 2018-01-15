"""text area widget class"""
# pylint: disable-msg=E0611, C0103

from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QGroupBox

class MessagesTextArea(QWidget):
    """this class creates a text area"""

    #constructor
    def __init__(self, message="", groupBoxLabel="test"):
        super().__init__() #call the super class constructor

        #create widgets
        self.groupBoxWidget = QGroupBox(groupBoxLabel)
        self.textEditWidget = QTextEdit(message)

        #create layout for text area
        self.messagesLayout = QVBoxLayout()

        #add text area to layout
        self.messagesLayout.addWidget(self.textEditWidget)

        #comment
        self.groupBoxWidget.setLayout(self.messagesLayout)

        #create a layout for whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.groupBoxWidget)

        #set the layout for this widget
        self.setLayout(self.main_layout)
    
