import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.unit_ui()

    def unit_ui(self):
        self.user_name_correct = "hasandrsuns"
        self.password_correct = "12345"

        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter = QtWidgets.QPushButton("Login")
        self.message = QtWidgets.QLabel("")

        horizontalLayout = QtWidgets.QHBoxLayout()

        horizontalLayout.addWidget(self.user_name)
        horizontalLayout.addWidget(self.password)
        horizontalLayout.addWidget(self.enter)
        horizontalLayout.addWidget(self.message)
        horizontalLayout.addStretch()

        verticalLayout = QtWidgets.QVBoxLayout()

        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addStretch()

        self.enter.clicked.connect(self.click)

        self.setLayout(verticalLayout)
        self.setWindowTitle("User Login")

        self.show()

    def click(self):
        if(self.user_name.text() == self.user_name_correct and self.password.text() == self.password_correct):
            self.message.setText("Welcome " + self.user_name.text())
        else:
            self.message.setText("Username or Passwprd Incorrect!")

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())