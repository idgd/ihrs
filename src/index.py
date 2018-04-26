import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QLineEdit, QLabel)
from api.DatabaseConnection import DatabaseConnection
from api.tasks.NoiseFloor import NoiseFloor
from api.tasks.MsgCount import MsgCount

class UiWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IHRS Database UI")
        self.setGeometry(448, 156, 1024, 768)
        self.database_connection = DatabaseConnection()
        self.message_index = 0
        self.create_messages_layout(self.message_index)

    def create_messages_layout(self, message_index=0):
        #retrun a list of database documents
        self.messages = self.database_connection.return_list()

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
        self.run_push_button = QPushButton("Run")

        #Connect methods to buttons
        self.add_push_button.clicked.connect(self.add)
        self.remove_push_button.clicked.connect(self.remove)
        self.run_push_button.clicked.connect(self.run)
        #other
        self.task_list_label = QLabel("Task List")
        self.task_queue_label = QLabel("Task Queue")
        self.task_loggerLabel = QLabel("Task Logger")
        #layout

        self.add_remove_layout = QVBoxLayout()
        self.task_list_layout = QVBoxLayout()
        self.task_queue_layout = QVBoxLayout()
        self.task_logger_layout = QVBoxLayout()

        #create layout to hold the widgets
        self.initial_layout = QHBoxLayout()
        self.task_list_layout.addWidget(self.task_list_label)
        self.task_list_layout.addWidget(self.task_list)
        self.add_remove_layout.addWidget(self.add_push_button)
        self.add_remove_layout.addWidget(self.remove_push_button)
        self.task_queue_layout.addWidget(self.task_queue_label)
        self.task_queue_layout.addWidget(self.task_queue)
        self.task_queue_layout.addWidget(self.run_push_button)
        self.task_logger_layout.addWidget(self.task_loggerLabel)
        self.task_logger_layout.addWidget(self.task_logger)
        self.initial_layout.addLayout(self.task_list_layout)
        self.initial_layout.addLayout(self.add_remove_layout)
        self.initial_layout.addLayout(self.task_queue_layout)
        self.initial_layout.addLayout(self.task_logger_layout)

        #create widget to hold layout
        self.message_widget = QWidget()
        self.message_widget.setLayout(self.initial_layout)

        #set the central widget
        self.setCentralWidget(self.message_widget)

    def add(self):
        listItems=self.task_list.selectedItems()
        items = []
        if not listItems:
            for index in range(self.task_list.count()):
                items.append(self.task_list.item(index))
            for i in range(len(items)):
                self.task_queue.addItem(items[i].text())
        else:
            for item in self.task_list.selectedItems():
                self.task_queue.addItem(item.text())
            

    def remove(self):
        self.task_logger.clear()
        listItems=self.task_queue.selectedItems()
        items = []
        if not listItems:
            for index in range(self.task_queue.count()):
                items.append(self.task_queue.item(index))
            for i in range(len(items)):
                self.task_queue.takeItem(self.task_queue.row(items[i]))
        else:
            for item in listItems:
                self.task_queue.takeItem(self.task_queue.row(item))

    def run(self):
        self.task_logger.clear()
        self.messages = self.database_connection.return_list()
        msgs = [f for f in self.messages]
        nf = NoiseFloor()
        mg = MsgCount()
        out = [f for f in range(self.task_queue.count())]
        for i in range(self.task_queue.count()):
            task = self.task_queue.item(i).text()
            if task == "Average Noise Floor":
                out[i] = nf.CalculateAverageNoiseFloor(msgs)
            elif task == "Maximum Noise Floor":
                out[i] = nf.CalculateMaximumNoiseFloor(msgs)
            elif task == "Minimum Noise Floor":
                out[i] = nf.CalculateMinimumNoiseFloor(msgs)
            elif task == "Average Messages Per Second":
                out[i] = mg.CalculateAveragePerSec(msgs)
            else:
                out[i] = mg.CalculateRedundantCount(msgs)
        for f in out:
            self.task_logger.addItem(str(f))

def main():
    app = QApplication(sys.argv) #create new application
    ui_window = UiWindow() #create new instance of main window
    ui_window.show() #make instance visable
    ui_window.raise_() #raise instance to top of window stack
    app.exec_() #monitor application for events

if __name__ == "__main__":
    main()
