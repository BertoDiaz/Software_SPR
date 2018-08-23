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
        self.btnChecked = {
            'Laser': False,
            'Peristaltic': False,
            'Impulsional A': False,
            'Impulsional B': False
        }
        self.btnColor = {
            'Laser': '',
            'Peristaltic': '',
            'Impulsional A': '',
            'Impulsional B': ''
        }
        self.btnStatus = {
            'Laser': '',
            'Peristaltic': '',
            'Impulsional A': '',
            'Impulsional B': ''
        }
        # self.btnLaserChecked = False
        # self.btnPeristalticChecked = False
        # self.btnImpulsionalAChecked = False
        # self.btnImpulsionalBChecked = False
        # self.btnLaserColor = None
        # self.btnPeristalticColor = None
        # self.btnImpulsionalAColor = None
        # self.btnImpulsionalBColor = None
        # self.statusLaser = None
        # self.statusPeristaltic = None
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

            self.viewSystemControl.edtPeristaltic.setValue(self.valuePeristaltic)
            self.viewSystemControl.edtImpulsional_A.setValue(self.valueImpulsionalA)
            self.viewSystemControl.edtImpulsional_B.setValue(self.valueImpulsionalB)

            self.valueGainA = self.dataInit["Gain1"]
            self.valueGainB = self.dataInit["Gain2"]
            self.valueOffsetA = self.dataInit["Offset1"]
            self.valueOffsetB = self.dataInit["Offset2"]

            self.viewCurveSetup.edtGainA.setValue(self.valueGainA)
            self.viewCurveSetup.edtGainB.setValue(self.valueGainB)
            self.viewCurveSetup.edtOffsetA.setValue(self.valueOffsetA)
            self.viewCurveSetup.edtOffsetB.setValue(self.valueOffsetB)

            self.viewCurveSetup.edtInitialAngle.setValue(self.valueInitAngle)
            self.viewCurveSetup.edtAngleLongitude.setValue(self.valueAngleLongitude)
            self.viewCurveSetup.edtAngleResolution.setValue(self.valueAngleResolution)
            self.viewCurveSetup.edtFinalAngle.setText(str(self.valueFinalAngle))
            self.viewCurveSetup.edtPointsCurve.setText(str(self.valuePointsCurve))

            self.viewSystemControl.btnLaser.clicked.connect(self.laserChange)
            self.viewSystemControl.btnPeristaltic.clicked.connect(self.btnPeristalticChange)
            self.viewSystemControl.btnImpulsional_A.clicked.connect(self.btnImpulsionalAChange)
            self.viewSystemControl.btnImpulsional_B.clicked.connect(self.btnImpulsionalBChange)

            self.viewSystemControl.edtPeristaltic.valueChanged.connect(self.pumpsControlChange)

            self.viewCurveSetup.btnCalibrate.clicked.connect(self.sendCalibrateParameters)
            self.viewCurveSetup.btnLaser.clicked.connect(self.laserChange)
            self.viewCurveSetup.btnResetValues.clicked.connect(self.resetCurvePerformance)

            self.viewCurveSetup.edtGainA.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtGainB.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtOffsetA.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtOffsetB.valueChanged.connect(self.calibrateChange)

            self.viewCurveSetup.edtInitialAngle.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleLongitude.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleResolution.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtFinalAngle.textChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtPointsCurve.textChanged.connect(self.curvePerformanceChange)

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

    def pumpsControlChange(self):
        self.valuePeristaltic = self.viewSystemControl.edtPeristaltic.value()
        self.valueImpulsionalA = self.viewSystemControl.edtImpulsional_A.value()
        self.valueImpulsionalB = self.viewSystemControl.edtImpulsional_B.value()

    def btnPeristalticChange(self):
        if not self.btnChecked['Peristaltic']:
            self.btnColor['Peristaltic'] = 'grey'
            self.btnStatus['Peristaltic'] = 'STOP'

            self.btnChecked['Peristaltic'] = True

        else:
            self.btnColor['Peristaltic'] = 'blue'
            self.btnStatus['Peristaltic'] = 'START'

            self.btnChecked['Peristaltic'] = False

        self.viewSystemControl.btnPeristaltic.setText(self.btnStatus['Peristaltic'])

        style = 'QPushButton {font: bold; background-color: ' + self.btnColor['Peristaltic'] + \
                '; color: white; font-size: 12px; height: 70px;}'
        self.viewSystemControl.btnPeristaltic.setStyleSheet(style)

    def btnImpulsionalAChange(self):
        if not self.btnChecked['Impulsional A']:
            self.btnColor['Impulsional A'] = 'grey'
            self.btnStatus['Impulsional A'] = 'INJECT'

            self.btnChecked['Impulsional A'] = True

        else:
            self.btnColor['Impulsional A'] = 'blue'
            self.btnStatus['Impulsional A'] = 'INJECT'

            self.btnChecked['Impulsional A'] = False

        self.viewSystemControl.btnImpulsional_A.setText(self.btnStatus['Impulsional A'])

        style = 'QPushButton {font: bold; background-color: ' + self.btnColor['Impulsional A'] + \
                '; color: white; font-size: 12px; height: 70px;}'
        self.viewSystemControl.btnImpulsional_A.setStyleSheet(style)

    def btnImpulsionalBChange(self):
        if not self.btnChecked['Impulsional B']:
            self.btnColor['Impulsional B'] = 'grey'
            self.btnStatus['Impulsional B'] = 'INJECT'

            self.btnChecked['Impulsional B'] = True

        else:
            self.btnColor['Impulsional B'] = 'blue'
            self.btnStatus['Impulsional B'] = 'INJECT'

            self.btnChecked['Impulsional B'] = False

        self.viewSystemControl.btnImpulsional_B.setText(self.btnStatus['Impulsional B'])

        style = 'QPushButton {font: bold; background-color: ' + self.btnColor['Impulsional B'] + \
                '; color: white; font-size: 12px; height: 70px;}'
        self.viewSystemControl.btnImpulsional_B.setStyleSheet(style)

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

    def calibrateChange(self):
        self.valueGainA = self.viewCurveSetup.edtGainA.value()
        self.valueOffsetA = self.viewCurveSetup.edtOffsetA.value()
        self.valueGainB = self.viewCurveSetup.edtGainB.value()
        self.valueOffsetB = self.viewCurveSetup.edtOffsetB.value()

    def calibrateReceive(self, data):
        if data != '@':
            self.viewCurveSetup.setMessageCritical("Error", "The device has not been calibrated, try again.")

        self.serialPort.serialPort.readyRead.disconnect()
        self.serialPort.packet_received.disconnect()

    def laserChange(self):
        if not self.btnChecked['Laser']:
            self.btnColor['Laser'] = 'red'
            self.btnStatus['Laser'] = 'Laser ON'

            self.btnChecked['Laser'] = True

            send = 1

        else:
            self.btnColor['Laser'] = 'green'
            self.btnStatus['Laser'] = 'Laser OFF'

            self.btnChecked['Laser'] = False

            send = 0

        self.serialPort.send_Laser(send)

        self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_data)
        self.serialPort.packet_received.connect(self.laserReceive)

    def laserReceive(self, data):
        if data == '@':
            self.viewSystemControl.btnLaser.setText(self.btnStatus['Laser'])
            self.viewCurveSetup.btnLaser.setText(self.btnStatus['Laser'])

            style = 'QPushButton {font: bold; background-color: ' + self.btnColor['Laser'] + \
                    '; color: white; font-size: 20px; height:100px; width: 20px;}'
            self.viewSystemControl.btnLaser.setStyleSheet(style)

            style = 'QPushButton {font: bold; background-color: ' + self.btnColor['Laser'] + \
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

        self.viewCurveSetup.edtInitialAngle.setValue(self.valueInitAngle)
        self.viewCurveSetup.edtAngleLongitude.setValue(self.valueAngleLongitude)
        self.viewCurveSetup.edtAngleResolution.setValue(self.valueAngleResolution)
        self.viewCurveSetup.edtFinalAngle.setText(str(self.valueFinalAngle))
        self.viewCurveSetup.edtPointsCurve.setText(str(self.valuePointsCurve))

    def curvePerformanceChange(self):
        self.valueInitAngle = self.viewCurveSetup.edtInitialAngle.value()
        self.valueAngleLongitude = self.viewCurveSetup.edtAngleLongitude.value()
        self.valueAngleResolution = self.viewCurveSetup.edtAngleResolution.value()

        try:
            self.valueFinalAngle = int(self.viewCurveSetup.edtFinalAngle.text())
            self.valuePointsCurve = int(self.viewCurveSetup.edtPointsCurve.text())

        except Exception:
            self.viewCurveSetup.setMessageCritical("Error", "The value can only be a number.")
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
