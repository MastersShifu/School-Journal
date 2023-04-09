# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=c-extension-no-member
# pylint: disable=no-name-in-module
# pylint: disable=invalid-name

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from login import LoginPage

if __name__ == "__main__":
    app = QApplication([])
    login_page = LoginPage()
    login_page.setWindowState(Qt.WindowMaximized) 
    login_page.show()
    app.exec()
        