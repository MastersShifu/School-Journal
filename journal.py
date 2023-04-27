# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module
# pylint: disable=invalid-name

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel, QStackedWidget
from PyQt5.QtCore import Qt
from login import LoginPage
from register import RegisterPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)
        self.login_widget = LoginPage()
        self.register_widget = RegisterPage()
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.login_widget.regi.clicked.connect(self.show_register)
        self.register_widget.back_button.clicked.connect(self.show_login)
        self.login_widget.login.clicked.connect(self.aut)

    def show_login(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_register(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def aut(self):
        self.login_widget.autorizate()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.setWindowState(Qt.WindowMaximized)
    main_window.show()
    app.exec()
