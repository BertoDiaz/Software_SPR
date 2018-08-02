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
from views_Tabs import ViewTabs
from PyQt5.QtWidgets import QApplication
import sys


class ControllerTabs:
    def __init__(self):
        self.serialPort = None
        self.dataInit = []
        self.checked = False

        self.viewTabs = ViewTabs(None)
        self.viewSystemControl = self.viewTabs.tab_SystemControl
        self.viewCurveSetup = self.viewTabs.tab_CurveSetup

        self.viewTabs.mainWindow()
        self.viewSystemControl.mainWindow()
        self.viewCurveSetup.mainWindow()

        self.viewTabs.show()

        self.run()

    def run(self):

        controllerConnect = ControllerConnect()

        self.serialPort = controllerConnect.serialPort
        self.dataInit = controllerConnect.dataInit

        """For now it's not necessary to send the data to SPR."""
        # if controllerConnect.loadedFile:
        #     self.sendValuesLoaded()

        self.viewSystemControl.editPeristaltic.setText(str(self.dataInit["PER1"]))
        self.viewSystemControl.editImpulsional_A.setText(str(self.dataInit["Impul1"]))
        self.viewSystemControl.editImpulsional_B.setText(str(self.dataInit["Impul2"]))

        self.viewCurveSetup.editGainA.setText(str(self.dataInit["Gain1"]))
        self.viewCurveSetup.editGainB.setText(str(self.dataInit["Gain2"]))
        self.viewCurveSetup.editOffsetA.setText(str(self.dataInit["Offset1"]))
        self.viewCurveSetup.editOffsetB.setText(str(self.dataInit["Offset2"]))

        # self.viewSystemControl.btnExit.clicked.connect(self.exit_App)
        self.viewSystemControl.btnLaser.clicked.connect(self.laser_change)

        self.viewTabs.btnExit.clicked.connect(self.exit_App)

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
            self.viewSystemControl.btnLaser.setText('Laser ON')
            self.viewSystemControl.btnLaser.setStyleSheet(
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
            self.viewSystemControl.btnLaser.setText('Laser OFF')
            self.viewSystemControl.btnLaser.setStyleSheet(
                'QPushButton {'
                'font: bold;'
                'background-color: green;'
                'color: white;'
                'font-size: 20px;'
                'height:100px;'
                'width: 20px;'
                '}')

            self.checked = False

            self.serialPort.send_Laser(0)

    def exit_App(self):
        exitApp = self.viewTabs.setMessageExit()

        if exitApp:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])

    window = ControllerTabs()
    sys.exit(app.exec_())
