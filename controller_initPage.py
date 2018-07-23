"""
Copyright (C) 2018  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from controller_connect import ControllerConnect
from views_initPage import View
from SerialPort import SerialPort
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from time import sleep
import sys
import codecs


class ControllerInit:
    def __init__(self):

        self.viewInit = View(None)

        self.viewInit.mainWindow()

        self.viewInit.btnExit.clicked.connect(self.exit_App)

        self.viewInit.show()

        ControllerConnect()

    def exit_App(self):
        exitApp = self.viewInit.setMessageExit()

        if exitApp:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])

    window = ControllerInit()
    sys.exit(app.exec_())
