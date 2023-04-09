# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module
# pylint: disable=invalid-name

from PySide6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
import gc
import sqlite3
from register import RegisterPage

con = sqlite3.connect("/home/shifu/projects/Journal/tutorial.db")
cursor = con.cursor()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Journal")
        self.registration = RegisterPage()

        layout = QVBoxLayout()

        self.name = QLineEdit()
        self.password = QLineEdit()

        self.label = QLabel() # login error

        self.login = QPushButton("Authorization")
        self.regi = QPushButton("Registration")

        self.name.setPlaceholderText("Enter name")
        self.password.setPlaceholderText("Enter password")
        self.regi.setStyleSheet("background-color: transparent; border: none; color: White;")
        self.regi.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet("color: red")
        self.password.setEchoMode(QLineEdit.Password)

        self.name.setFixedSize(200, 40)
        self.password.setFixedSize(200, 40)
        self.login.setFixedSize(200, 50)
        self.label.setFixedSize(200, 40)

        layout.addWidget(self.label)
        layout.addWidget(self.name)
        layout.addWidget(self.password)
        layout.addWidget(self.login)
        layout.addWidget(self.regi)

        self.login.clicked.connect(self.autorizate)
        self.regi.clicked.connect(self.register)

        self.setLayout(layout)

        layout.setAlignment(Qt.AlignCenter)

    def autorizate(self):
        cursor.execute("SELECT * FROM acc")

        name = self.name.text()
        password = self.password.text()
        password = int(password)
        print(name)
        print(password)

        for accaunt in cursor.fetchall():
            if name == accaunt[1]:
                if password == accaunt[2]:
                    print("Yes!")
                    gc.collect()
                    self.cabinet()

        self.label.setText("Incorect password or login")

    def prin(self):
        print("asd")

    def register(self):
        self.registration.resize(400, 500)
        self.registration.show()

    def cabinet(self):
        self.name.hide()
        self.password.hide()
        self.login.hide()
        self.label.hide()
        self.regi.hide()
