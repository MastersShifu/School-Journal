# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module
# pylint: disable=invalid-name

from PyQt5.QtWidgets import QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sqlite3
import re


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.reg_name = QLineEdit()
        self.reg_pass = QLineEdit()
        self.reg_mail = QLineEdit()
        self.f_name = QLineEdit()

        self.l_name = QLabel()

        self.reg_button = QPushButton("Register")
        self.back_button = QPushButton("<- Back")

        self.reg_name.setPlaceholderText("Enter login")
        self.reg_pass.setPlaceholderText("Enter pass")
        self.reg_mail.setPlaceholderText("Enter mail")
        self.f_name.setPlaceholderText("Full name")

        self.back_button.setStyleSheet("background-color: transparent; border: none; color: White;")
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg_name.setMaxLength(16)
        self.reg_pass.setMaxLength(16)

        layout.addWidget(self.f_name)
        layout.addWidget(self.reg_name)
        layout.addWidget(self.reg_pass)
        layout.addWidget(self.reg_mail)
        layout.addWidget(self.reg_button)
        layout.addWidget(self.back_button)
        layout.addWidget(self.l_name)

        self.reg_name.setFixedSize(200, 40)
        self.reg_pass.setFixedSize(200, 40)
        self.reg_mail.setFixedSize(200, 40)
        self.f_name.setFixedSize(200, 40)
        self.reg_button.setFixedSize(200, 50)

        widget = QWidget()
        widget.setLayout(layout)
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)

    def register(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        rename = r"^[a-zA-Zа-яА-ЯёЁ]+$"
        try: 
            r_n = self.reg_name.text()
            r_p = self.reg_pass.text()
            r_p = int(r_p)
            r_m = self.reg_mail.text()
            r_f_n = self.f_name.text()
        except ValueError:
            return

        con = sqlite3.connect("/home/shifu/projects/Journal/tutorial.db")
        cursor = con.cursor()

        cursor.execute("SELECT id FROM acc")
        id_list = [row[0] for row in cursor.fetchall()]
        max_id = max(id_list)
        max_id += 1

        logins = cursor.execute("SELECT name FROM acc")
        r_l = logins.fetchall()
        r_l_c = r_l

        mails = cursor.execute("SELECT email FROM acc")
        r_e = mails.fetchall()
        r_m_c = r_e

        if (r_n, ) in r_l_c:
            print("This name is taked")
            self.l_name.setText("This name is taked")

        elif (r_m, ) in r_m_c:
            print("This email is taken")
            self.l_name.setText("This email is taken")

        elif not re.fullmatch(regex, r_m):
            print('Invaild email')
            self.l_name.setText("Invail email")

        elif len(str(r_p)) < 6:
            self.l_name.setText("Password too small")

        elif not re.fullmatch(rename, r_m):
            self.l_name.setText("Login has incorect symbols")

        elif len(r_n) > 10:
            self.l_name.setText("Login is too big")

        else:
            cursor.execute(
                "INSERT INTO acc (id, name, password, email, f_name) VALUES (?, ?, ?, ?, ?)", 
                (max_id, f"{r_n}", f"{r_p}", f"{r_m}", f"{r_f_n}"))
            con.commit()
            con.close()
            self.close()
