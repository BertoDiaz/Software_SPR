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
from time import sleep
import sys


class Controller:
    def __init__(self):
        self.numberOfItem = 0
        self.ports = []

        self.serialPort = SerialPort()

        self.view = View(None)
        self.ports = self.serialPort.ask_for_port()
        self.view.setPorts(self.ports)

        self.view.combo.activated.connect(self.onActivated)
        self.view.btnOpen.clicked.connect(self.open_port)
        self.view.btnClose.clicked.connect(self.close_port)

        self.view.show()

        self.connect()

        # self.view.splash.show()
        # self.view.splash.repaint()

    def connect(self):
        foundCount = 0
        connected = False

        self.view.progressBar.setValue(foundCount)
        QApplication.processEvents()

        for foundCount in range(0, 5):

            self.view.progressBar.setValue((foundCount + 1) * 20)

            port_found = self.find_port()

            if port_found[0]:
                self.view.progressBar.setValue((foundCount + 1) * 20)

                connected = self.serialPort.open_port(port_found[1])
                self.view.setPortFound(port_found[1])

                self.serialPort.write_port("?")
                self.numberOfItem = port_found[1]

                break

            sleep(3)

        self.view.mainWindow(connected)

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

    def find_port(self):
        port_found = []
        i = 1
        found = False

        for port in self.ports:
            if port['port'] == "COM6":
                port_found.append(True)
                port_found.append(i)
                found = True

            i += 1

        if not found:
            port_found.append(False)
            port_found.append(0)

        return port_found


if __name__ == '__main__':
    app = QApplication([])

    window = Controller()
    sys.exit(app.exec_())
