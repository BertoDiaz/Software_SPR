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
from PyQt5.QtWidgets import QApplication
import sys


class ControllerInit:
    def __init__(self):
        self.serialPort = None
        self.dataInit = []
        self.checked = False

        self.viewInit = View(None)

        self.viewInit.mainWindow()

        self.viewInit.show()

        self.run()

    def run(self):

        controllerConnect = ControllerConnect()

        self.serialPort = controllerConnect.serialPort
        self.dataInit = controllerConnect.dataInit

        """For now it's not necessary to send the data to SPR."""
        # if controllerConnect.loadedFile:
        #     self.sendValuesLoaded()

        self.viewInit.btnExit.clicked.connect(self.exit_App)
        self.viewInit.btnLaser.clicked.connect(self.laser_change)

    def sendValuesLoaded(self):

        toSend = [
            self.dataInit["Gain1"],
            self.dataInit["Offset1"],
            self.dataInit["Gain2"],
            self.dataInit["Offset2"]
        ]

        self.serialPort.send_Gain_Offset(toSend)

        """New line to be easier to read the data."""
        self.serialPort.write_port('\n')

        toSend = [
            self.dataInit["Impul1"]
        ]

        self.serialPort.send_Control_Impul_A(toSend)

        """New line to be easier to read the data."""
        self.serialPort.write_port('\n')

        """Here yuo have to send DC1"""

        toSend = [
            self.dataInit["Impul2"]
        ]

        self.serialPort.send_Control_Impul_B(toSend)

        """New line to be easier to read the data."""
        self.serialPort.write_port('\n')

        toSend = [
            self.dataInit["PURG1"],
            self.dataInit["PURG2"]
        ]

        self.serialPort.send_Volume_Purges(toSend)

        """New line to be easier to read the data."""
        self.serialPort.write_port('\n')

    def laser_change(self):
        if not self.checked:
            self.viewInit.btnLaser.setText('Laser ON')
            self.viewInit.btnLaser.setStyleSheet(
                'QPushButton {'
                'font: bold;'
                'background-color: red;'
                'color: white;'
                'font-size: 20px;'
                'height:100px;'
                'width: 20px;'
                '}')

            self.checked = True

            self.serialPort.send_Laser(1)

        else:
            self.viewInit.btnLaser.setText('Laser OFF')
            self.viewInit.btnLaser.setStyleSheet(
                'QPushButton {'
                'font: bold;'
                'background-color: green;'
                'color: white;'
                'font-size: 20x;'
                'height:100px;'
                'width: 20px;'
                '}')

            self.checked = False

            self.serialPort.send_Laser(0)

    def exit_App(self):
        exitApp = self.viewInit.setMessageExit()

        if exitApp:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])

    window = ControllerInit()
    sys.exit(app.exec_())
