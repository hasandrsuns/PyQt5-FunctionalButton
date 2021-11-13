import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.write_text = QtWidgets.QLabel("Number")
        self.button1 = QtWidgets.QPushButton("Increase")
        self.button2 = QtWidgets.QPushButton("Decrease")
        self.number = 0

        #create Layouts
        horizontalLayout = QtWidgets.QHBoxLayout()

        horizontalLayout.addWidget(self.write_text)
        horizontalLayout.addWidget(self.button1)
        horizontalLayout.addWidget(self.button2)

        verticalLayout = QtWidgets.QVBoxLayout()

        verticalLayout.addStretch()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addStretch()

        self.button1.clicked.connect(self.increase)
        self.button2.clicked.connect(self.decrease)

        self.setLayout(verticalLayout)

        self.show()

    def increase(self):
        self.number += 1
        self.write_text.setText(str(self.number))

    def decrease(self):
        self.number -= 1
        self.write_text.setText(str(self.number))

#create app
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
