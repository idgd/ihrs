import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QLineEdit, QLabel)

from api.ihrs_api import (DatabaseConnection) # provides database methods
from ui.message_text_area_class import MessagesTextArea  # provides the text area widget

class UiWindow(QMainWindow):
    """this class creates a main window"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("IHRS Database UI") #set window title
        self.setGeometry(500, 250, 500, 500)
        self.database_connection = DatabaseConnection() #get database connection
        self.message_index = 0
        self.create_messages_layout(self.message_index) #sets the message window as the main window

    def create_messages_layout(self, message_index=0):
        """this is the initial layout of the window - to display the message"""

        #retrun a list of database documents
        self.messages = self.database_connection.return_list()
        initial_message_text = self.messages[message_index]["text"]
        initial_message_id = str("Message ID: ") + str(self.messages[message_index]["_id"])

        #create widgets
        #lists
        self.task_list = QListWidget()
        self.task_queue = QListWidget()
        self.task_logger = QListWidget()
        self.task_list.addItem("Average Noise Floor")
        self.task_list.addItem("Maximum Noise Floor")
        self.task_list.addItem("Minimum Noise Floor")
        self.task_list.addItem("Average Messages Per Second")
        self.task_list.addItem("Count Redundant Messages")
        #buttons
        self.add_push_button = QPushButton("Add")
        self.remove_push_button = QPushButton("Remove")
        self.browse_push_button = QPushButton("Browse")
        self.run_push_button = QPushButton("Run")
        self.view_push_button = QPushButton("View")
        #Connect methods to buttons
        self.add_push_button.clicked.connect(self.add)
        self.remove_push_button.clicked.connect(self.remove)
        self.browse_push_button.clicked.connect(self.browse)
        self.run_push_button.clicked.connect(self.run)
        self.view_push_button.clicked.connect(self.view)
        #other
        self.browse_line = QLineEdit()
        self.task_list_label = QLabel("Task List")
        self.task_queue_label = QLabel("Task Queue")
        self.task_loggerLabel = QLabel("Task Logger")
        #layout
        self.browse_layout = QHBoxLayout()
        self.add_remove_layout = QVBoxLayout()
        self.task_list_layout = QVBoxLayout()
        self.task_queue_layout = QVBoxLayout()
        self.task_logger_layout = QVBoxLayout()

        #create layout to hold the widgets
        self.initial_layout = QHBoxLayout()

        self.browse_layout.addWidget(self.browse_line)
        self.browse_layout.addWidget(self.browse_push_button)

        self.task_list_layout.addLayout(self.browse_layout)
        self.task_list_layout.addWidget(self.task_list)

        self.add_remove_layout.addWidget(self.add_push_button)
        self.add_remove_layout.addWidget(self.remove_push_button)

        self.task_queue_layout.addWidget(self.task_queue_label)
        self.task_queue_layout.addWidget(self.task_queue)
        self.task_queue_layout.addWidget(self.run_push_button)

        self.task_logger_layout.addWidget(self.task_loggerLabel)
        self.task_logger_layout.addWidget(self.task_logger)
        self.task_logger_layout.addWidget(self.view_push_button)

        self.initial_layout.addLayout(self.task_list_layout)
        self.initial_layout.addLayout(self.add_remove_layout)
        self.initial_layout.addLayout(self.task_queue_layout)
        self.initial_layout.addLayout(self.task_logger_layout)

        #create widget to hold layout
        self.message_widget = QWidget()
        self.message_widget.setLayout(self.initial_layout)

        #set the central widget
        self.setCentralWidget(self.message_widget)

        #connections
#        self.nextPushButton.clicked.connect(self.next_message)
#        self.previousPushButton.clicked.connect(self.previouse_message)

    def add(self):
        '''t'''

    def remove(self):
        '''t'''

    def browse(self):
        '''t'''

    def run(self):
        '''t'''

    def view(self):
        '''t'''

    def next_message(self):
        """this method returns the next message in the database"""

        if self.message_index != self.messages.count()-1:
            self.message_index = self.message_index + 1
        self.create_messages_layout(self.message_index)

    def previouse_message(self):
        """this method returns the previous message in the database"""

        if self.message_index != 0:
            self.message_index = self.message_index - 1
        self.create_messages_layout(self.message_index)

def main():
    """this is the main function"""

    ihrs_ui = QApplication(sys.argv) #create new application
    ui_window = UiWindow() #create new instance of main window
    ui_window.show() #make instance visable
    ui_window.raise_() #raise instance to top of window stack
    ihrs_ui.exec_() #monitor application for events

if __name__ == "__main__":
    main()
