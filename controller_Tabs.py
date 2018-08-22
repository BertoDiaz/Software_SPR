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
        self.btnLaserChecked = False
        self.color = None
        self.statusLaser = None
        self.valuePeristaltic = 0
        self.valueImpulsionalA = 0
        self.valueImpulsionalB = 0
        self.valueGainA = 0
        self.valueGainB = 0
        self.valueOffsetA = 0
        self.valueOffsetB = 0
        self.valueInitAngle = 0
        self.valueAngleLongitude = 3
        self.valueAngleResolution = 0.2
        self.valueFinalAngle = 0
        self.valuePointsCurve = 0

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

        if controllerConnect.finish:
            self.exit_All()

        else:

            self.serialPort = controllerConnect.serialPort
            self.dataInit = controllerConnect.dataInit

            """For now it's not necessary to send the data to SPR."""
            # if controllerConnect.loadedFile:
            #     self.sendValuesLoaded()

            self.valuePeristaltic = self.dataInit["PER1"]
            self.valueImpulsionalA = self.dataInit["Impul1"]
            self.valueImpulsionalB = self.dataInit["Impul2"]

            self.viewSystemControl.edtPeristaltic.setText(str(self.valuePeristaltic))
            self.viewSystemControl.edtImpulsional_A.setText(str(self.valueImpulsionalA))
            self.viewSystemControl.edtImpulsional_B.setText(str(self.valueImpulsionalB))

            self.valueGainA = self.dataInit["Gain1"]
            self.valueGainB = self.dataInit["Gain2"]
            self.valueOffsetA = self.dataInit["Offset1"]
            self.valueOffsetB = self.dataInit["Offset2"]

            self.viewCurveSetup.edtGainA.setText(str(self.valueGainA))
            self.viewCurveSetup.edtGainB.setText(str(self.valueGainB))
            self.viewCurveSetup.edtOffsetA.setText(str(self.valueOffsetA))
            self.viewCurveSetup.edtOffsetB.setText(str(self.valueOffsetB))

            self.viewCurveSetup.edtInitialAngle.setText(str(self.valueInitAngle))
            self.viewCurveSetup.edtAngleLongitude.setText(str(self.valueAngleLongitude))
            self.viewCurveSetup.edtAngleResolution.setText(str(self.valueAngleResolution))
            self.viewCurveSetup.edtFinalAngle.setText(str(self.valueFinalAngle))
            self.viewCurveSetup.edtPointsCurve.setText(str(self.valuePointsCurve))

            # self.viewSystemControl.btnExit.clicked.connect(self.exit_App)
            self.viewSystemControl.btnLaser.clicked.connect(self.laser_change)
            self.viewCurveSetup.btnCalibrate.clicked.connect(self.sendCalibrateParameters)
            self.viewCurveSetup.btnLaser.clicked.connect(self.laser_change)
            self.viewCurveSetup.btnResetValues.clicked.connect(self.resetCurvePerformance)

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

    def sendCalibrateParameters(self):
        toSend = [
            self.valueGainA,
            self.valueOffsetA,
            self.valueGainB,
            self.valueOffsetB
        ]

        self.serialPort.send_Gain_Offset(toSend)

        self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_data)
        self.serialPort.packet_received.connect(self.calibrateReceive)

    def calibrateReceive(self, data):
        if data != '@':
            self.viewCurveSetup.setMessageCritical("Error", "The device has not been calibrated, try again.")

        self.serialPort.serialPort.readyRead.disconnect()
        self.serialPort.packet_received.disconnect()

    def laser_change(self):
        if not self.btnLaserChecked:
            self.color = 'red'
            self.statusLaser = 'Laser ON'

            self.btnLaserChecked = True

            send = 1

        else:
            self.color = 'green'
            self.statusLaser = 'Laser OFF'

            self.btnLaserChecked = False

            send = 0

        self.serialPort.send_Laser(send)

        self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_data)
        self.serialPort.packet_received.connect(self.laserReceive)

    def laserReceive(self, data):
        if data == '@':
            self.viewSystemControl.btnLaser.setText(self.statusLaser)
            self.viewCurveSetup.btnLaser.setText(self.statusLaser)

            style = 'QPushButton {font: bold; background-color: ' + self.color + \
                    '; color: white; font-size: 20px; height:100px; width: 20px;}'
            self.viewSystemControl.btnLaser.setStyleSheet(style)

            style = 'QPushButton {font: bold; background-color: ' + self.color + \
                    '; color: white; font-size: 12px; height: 80px; width: 20px;}'
            self.viewCurveSetup.btnLaser.setStyleSheet(style)

        else:
            self.viewCurveSetup.setMessageCritical("Error", "The laser was not switch ON/OFF, try again.")

        self.serialPort.serialPort.readyRead.disconnect()
        self.serialPort.packet_received.disconnect()

    def resetCurvePerformance(self):
        self.valueInitAngle = 0
        self.valueAngleLongitude = 3
        self.valueAngleResolution = 0.2
        self.valueFinalAngle = 0
        self.valuePointsCurve = 0

        self.viewCurveSetup.edtInitialAngle.setText(str(self.valueInitAngle))
        self.viewCurveSetup.edtAngleLongitude.setText(str(self.valueAngleLongitude))
        self.viewCurveSetup.edtAngleResolution.setText(str(self.valueAngleResolution))
        self.viewCurveSetup.edtFinalAngle.setText(str(self.valueFinalAngle))
        self.viewCurveSetup.edtPointsCurve.setText(str(self.valuePointsCurve))

    def exit_App(self):
        exitApp = self.viewTabs.setMessageExit()

        if exitApp:
            QApplication.quit()

    @staticmethod
    def exit_All():
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])

    window = ControllerTabs()
    sys.exit(app.exec_())
