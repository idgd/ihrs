from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QGroupBox

class MessagesTextArea(QWidget):

    def __init__(self, message="", groupBoxLabel=""):
        super().__init__()

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
