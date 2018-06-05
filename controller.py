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

from views import View
from SerialPort import SerialPort
from PyQt5.QtWidgets import QApplication
import sys


class Controller:
    def __init__(self):
        self.numberOfItem = 0

        self.serialPort = SerialPort()

        self.view = View(None)
        self.view.setPorts(self.serialPort.ask_for_port())

        self.view.combo.activated.connect(self.onActivated)
        self.view.btnOpen.clicked.connect(self.open_port)
        self.view.btnClose.clicked.connect(self.close_port)

        self.view.show()

    def onActivated(self, numberItem):
        self.numberOfItem = numberItem

    def open_port(self):
        if self.serialPort.open_port(self.numberOfItem):
            self.view.btnOpen.setDisabled(True)
            self.view.btnClose.setDisabled(False)
            self.view.combo.setDisabled(True)

            self.serialPort.write_port("?")

        else:
            self.view.setMessageCritical("Error", "Port cannot be opened")

    def close_port(self):
        self.view.btnOpen.setDisabled(False)
        self.view.btnClose.setDisabled(True)
        self.view.combo.setDisabled(False)

        self.serialPort.close_port()


if __name__ == '__main__':
    app = QApplication([])

    window = Controller()
    sys.exit(app.exec_())
