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
from lib.Queue import Queue
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from functools import partial
import sys


class ControllerTabs:
    def __init__(self):
        self.serialPort = None
        self.dataInit = {}
        self.ackCommand = '@'
        self.laserON = 1
        self.laserOFF = 0
        self.peristalticON = 1
        self.peristalticOFF = 0
        self.msTimeout = 1000
        self.bufferWaitACK = Queue()
        self.btnTimeout = False

        self.btnChecked = {
            'Laser': False,
            'Peristaltic': False,
            'Impulsional A': False,
            'Impulsional B': False,
            'Reset': False,
            'Auto Acquisition': False
        }
        self.btnStatus = {
            'Laser': '',
            'Peristaltic': '',
            'Impulsional A': '',
            'Impulsional B': ''
        }
        self.btnDisable = {
            'Laser': False,
            'Peristaltic': False,
            'Impulsional A': False,
            'Impulsional B': False
        }
        self.values = {
            'Peristaltic': 0,
            'Impulsional A': 0,
            'Impulsional B': 0,
            'Gain A': 0,
            'Gain B': 0,
            'Offset A': 0,
            'Offset B': 0,
            'Init Angle': 0,
            'Angle Longitude': 3,
            'Angle Resolution': 0.2,
            'Final Angle': 0,
            'Points Curve': 0,
            'Automatic': 0,
            'Data Sampling': 2,
            'Acquisition Channel 1': 0,
            'Acquisition Channel 2': 0
        }
        self.valuesPhotodiodes = {
            'Photodiode A': [],
            'Photodiode B': []
        }

        self.tmrBtnImpulsional_A = QTimer()
        self.tmrBtnImpulsional_B = QTimer()
        self.tmrBtnReset = QTimer()
        self.tmrTimeout = QTimer()

        self.viewTabs = ViewTabs(None)
        self.viewSystemControl = self.viewTabs.tab_SystemControl
        self.viewCurveSetup = self.viewTabs.tab_CurveSetup
        self.viewDataAcquisition = self.viewTabs.tab_DataAcquisition

        self.viewTabs.mainWindow()
        self.viewSystemControl.mainWindow()
        self.viewCurveSetup.mainWindow()
        self.viewDataAcquisition.mainWindow()

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

            self.values['Peristaltic'] = self.dataInit["PER1"]
            self.values['Impulsional A'] = self.dataInit["Impul1"]
            self.values['Impulsional B'] = self.dataInit["Impul2"]

            self.viewSystemControl.edtPeristaltic.setValue(self.values['Peristaltic'])
            self.viewSystemControl.edtImpulsional_A.setValue(self.values['Impulsional A'])
            self.viewSystemControl.edtImpulsional_B.setValue(self.values['Impulsional B'])

            self.values['Gain A'] = self.dataInit["Gain1"]
            self.values['Gain B'] = self.dataInit["Gain2"]
            self.values['Offset A'] = self.dataInit["Offset1"]
            self.values['Offset B'] = self.dataInit["Offset2"]

            self.viewCurveSetup.edtGainA.setValue(self.values['Gain A'])
            self.viewCurveSetup.edtGainB.setValue(self.values['Gain B'])
            self.viewCurveSetup.edtOffsetA.setValue(self.values['Offset A'])
            self.viewCurveSetup.edtOffsetB.setValue(self.values['Offset B'])

            self.viewCurveSetup.edtInitialAngle.setValue(self.values['Init Angle'])
            self.viewCurveSetup.edtAngleLongitude.setValue(self.values['Angle Longitude'])
            self.viewCurveSetup.edtAngleResolution.setValue(self.values['Angle Resolution'])
            self.viewCurveSetup.edtFinalAngle.setText(str(self.values['Final Angle']))
            self.viewCurveSetup.edtPointsCurve.setText(str(self.values['Points Curve']))

            self.viewCurveSetup.edtAcquisition.setText(str(self.values['Automatic']))
            self.viewCurveSetup.edtDataSampling.setValue(self.values['Data Sampling'])
            self.viewCurveSetup.edtACQChannel_1.setText(str(self.values['Acquisition Channel 1']))
            self.viewCurveSetup.edtACQChannel_2.setText(str(self.values['Acquisition Channel 2']))

            self.viewSystemControl.btnLaser.clicked.connect(self.btnLaserChanged)
            self.viewSystemControl.btnPeristaltic.clicked.connect(self.btnPeristalticChanged)
            self.viewSystemControl.btnImpulsional_A.clicked.connect(self.btnImpulsionalAChanged)
            self.viewSystemControl.btnImpulsional_B.clicked.connect(self.btnImpulsionalBChanged)

            self.viewSystemControl.edtPeristaltic.valueChanged.connect(self.edtPeristalticChanged)
            self.viewSystemControl.edtImpulsional_A.valueChanged.connect(self.edtImpulsionalsChanged)
            self.viewSystemControl.edtImpulsional_B.valueChanged.connect(self.edtImpulsionalsChanged)

            self.viewCurveSetup.btnCalibrate.clicked.connect(self.sendCalibrateParameters)
            self.viewCurveSetup.btnLaser.clicked.connect(self.btnLaserChanged)
            self.viewCurveSetup.btnResetValues.clicked.connect(self.resetCurvePerformance)

            self.viewCurveSetup.btnAutoAcquisition.clicked.connect(self.initAutoAcquisition)

            self.viewCurveSetup.edtGainA.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtGainB.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtOffsetA.valueChanged.connect(self.calibrateChange)
            self.viewCurveSetup.edtOffsetB.valueChanged.connect(self.calibrateChange)

            self.viewCurveSetup.edtInitialAngle.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleLongitude.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleResolution.valueChanged.connect(self.curvePerformanceChange)

            self.viewCurveSetup.edtDataSampling.valueChanged.connect(self.acquisitionChange)

            self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_multiple_data)
            self.serialPort.packet_received.connect(self.receiveData)

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

    def edtPeristalticChanged(self):
        self.values['Peristaltic'] = self.viewSystemControl.getEdtPeristalticValue()

        if self.viewSystemControl.getBtnPeristalticStatus():
            toSend = [
                self.peristalticON,
                self.values['Peristaltic']
            ]

            self.serialPort.send_Control_Peristaltic(toSend)
            self.bufferWaitACK.append(self.peristalticCommandReceived)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=self.viewSystemControl.timeoutMessage['Peristaltic'],
                                      functionTimeout=self.peristalticCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def btnPeristalticChanged(self):
        self.viewSystemControl.setBtnPeristalticDisable(True)

        if self.viewSystemControl.getBtnPeristalticStatus():
            toSend = [
                self.peristalticON,
                self.values['Peristaltic']
            ]

        else:
            toSend = [
                self.peristalticOFF,
                self.values['Peristaltic']
            ]

        self.serialPort.send_Control_Peristaltic(toSend)
        self.bufferWaitACK.append(self.peristalticCommandReceived)

        functionTimeout = partial(self.setTimeout, messageTimeout=self.viewSystemControl.timeoutMessage['Peristaltic'],
                                  functionTimeout=self.peristalticCommandReceived)
        self.tmrTimeout.timeout.connect(functionTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def peristalticCommandReceived(self):
        status = self.viewSystemControl.getBtnPeristalticStatus()

        if self.btnTimeout:
            status = not self.viewSystemControl.getBtnPeristalticStatus()
            self.btnTimeout = False

        self.viewSystemControl.setBtnPeristalticStatus(status)
        self.viewSystemControl.setBtnPeristalticDisable(False)

    def edtImpulsionalsChanged(self):
        self.values['Impulsional A'] = self.viewSystemControl.getEdtImpulsionalAValue()
        self.values['Impulsional B'] = self.viewSystemControl.getEdtImpulsionalBValue()

    def btnImpulsionalAChanged(self):
        if self.viewSystemControl.getBtnImpulsionalAStatus():

            if self.viewSystemControl.getEdtImpulsionalAValue() != 0:
                self.viewSystemControl.setBtnImpulsionalADisable(True)

                toSend = self.values['Impulsional A'] * 50

                self.serialPort.send_Control_Impul_A(toSend)
                self.bufferWaitACK.append(self.impulsionalACommandReceived)

                functionTimeout = partial(self.setTimeout,
                                          messageTimeout=self.viewSystemControl.timeoutMessage['Impulsional A'],
                                          functionTimeout=self.impulsionalACommandReceived)
                self.tmrTimeout.timeout.connect(functionTimeout)
                self.tmrTimeout.start(self.msTimeout)

            else:
                self.viewSystemControl.setBtnImpulsionalAStatus(False)
                self.viewSystemControl.setMessageCritical("Error",
                                                          self.viewSystemControl.notCeroMessage['Impulsional A'])

    def impulsionalACommandReceived(self):
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = self.values['Impulsional A'] * 500

        finishImpulses = partial(self.viewSystemControl.setBtnImpulsionalAStatus, status=False)
        self.tmrBtnImpulsional_A.singleShot(timeImpulses, finishImpulses)

    def btnImpulsionalBChanged(self):
        if self.viewSystemControl.getBtnImpulsionalBStatus():

            if self.viewSystemControl.getEdtImpulsionalBValue() != 0:
                self.viewSystemControl.setBtnImpulsionalBDisable(True)

                toSend = self.values['Impulsional B'] * 50

                self.serialPort.send_Control_Impul_B(toSend)
                self.bufferWaitACK.append(self.impulsionalBCommandReceived)

                functionTimeout = partial(self.setTimeout,
                                          messageTimeout=self.viewSystemControl.timeoutMessage['Impulsional B'],
                                          functionTimeout=self.impulsionalBCommandReceived)
                self.tmrTimeout.timeout.connect(functionTimeout)
                self.tmrTimeout.start(self.msTimeout)

            else:
                self.viewSystemControl.setBtnImpulsionalBStatus(False)
                self.viewSystemControl.setMessageCritical("Error",
                                                          self.viewSystemControl.notCeroMessage['Impulsional B'])

    def impulsionalBCommandReceived(self):
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = self.values['Impulsional B'] * 500

        finishImpulses = partial(self.viewSystemControl.setBtnImpulsionalBStatus, status=False)
        self.tmrBtnImpulsional_B.singleShot(timeImpulses, finishImpulses)

    def sendCalibrateParameters(self):
        toSend = [
            self.values['Gain A'],
            self.values['Offset A'],
            self.values['Gain B'],
            self.values['Offset B']
        ]

        self.serialPort.send_Gain_Offset(toSend)

        self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_data)
        self.serialPort.packet_received.connect(self.calibrateReceive)

    def calibrateChange(self):
        self.values['Gain A'] = self.viewCurveSetup.edtGainA.value()
        self.values['Offset A'] = self.viewCurveSetup.edtOffsetA.value()
        self.values['Gain B'] = self.viewCurveSetup.edtGainB.value()
        self.values['Offset B'] = self.viewCurveSetup.edtOffsetB.value()

    def calibrateReceive(self, data):
        if data != '@':
            self.viewCurveSetup.setMessageCritical("Error", "The device has not been calibrated, try again.")

        else:
            self.viewCurveSetup.setCalibrateDone()

        self.serialPort.serialPort.readyRead.disconnect()
        self.serialPort.packet_received.disconnect()

    def btnLaserChanged(self):
        self.viewSystemControl.setBtnLaserDisable(True)
        self.viewCurveSetup.setBtnLaserDisable(True)

        if not self.btnChecked['Laser']:
            self.btnChecked['Laser'] = True
            toSend = self.laserON

        else:
            self.btnChecked['Laser'] = False
            toSend = self.laserOFF

        self.serialPort.send_Laser(toSend)
        self.bufferWaitACK.append(self.laserCommandReceived)

        messageTimeout = partial(self.setTimeout, messageTimeout=self.viewSystemControl.timeoutMessage['Laser'],
                                 functionTimeout=self.laserCommandReceived)
        self.tmrTimeout.timeout.connect(messageTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def laserCommandReceived(self):
        if self.btnTimeout:
            self.btnChecked['Laser'] = not self.btnChecked['Laser']
            self.btnTimeout = False

        self.viewSystemControl.setBtnLaserStatus(self.btnChecked['Laser'])
        self.viewCurveSetup.setBtnLaserStatus(self.btnChecked['Laser'])

        self.viewSystemControl.setBtnLaserDisable(False)
        self.viewCurveSetup.setBtnLaserDisable(False)

    def resetCurvePerformance(self):
        if not self.btnChecked['Reset']:
            self.tmrBtnReset.singleShot(1000, self.resetCurvePerformance)

            self.viewCurveSetup.btnResetValues.setDisabled(True)

            self.viewCurveSetup.edtInitialAngle.valueChanged.disconnect()
            self.viewCurveSetup.edtAngleLongitude.valueChanged.disconnect()
            self.viewCurveSetup.edtAngleResolution.valueChanged.disconnect()

            self.values['Init Angle'] = 0
            self.values['Angle Longitude'] = 3
            self.values['Angle Resolution'] = 0.2
            self.values['Final Angle'] = 0
            self.values['Points Curve'] = 0

            self.viewCurveSetup.edtInitialAngle.setValue(self.values['Init Angle'])
            self.viewCurveSetup.edtAngleLongitude.setValue(self.values['Angle Longitude'])
            self.viewCurveSetup.edtAngleResolution.setValue(self.values['Angle Resolution'])
            self.viewCurveSetup.edtFinalAngle.setText(str(self.values['Final Angle']))
            self.viewCurveSetup.edtPointsCurve.setText(str(self.values['Points Curve']))

            self.btnChecked['Reset'] = True

        else:

            self.viewCurveSetup.btnResetValues.setChecked(False)
            self.viewCurveSetup.btnResetValues.setDisabled(False)
            self.btnChecked['Reset'] = False

            self.viewCurveSetup.edtInitialAngle.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleLongitude.valueChanged.connect(self.curvePerformanceChange)
            self.viewCurveSetup.edtAngleResolution.valueChanged.connect(self.curvePerformanceChange)

    def curvePerformanceChange(self):
        self.values['Init Angle'] = self.viewCurveSetup.edtInitialAngle.value()
        self.values['Angle Longitude'] = self.viewCurveSetup.edtAngleLongitude.value()
        self.values['Angle Resolution'] = self.viewCurveSetup.edtAngleResolution.value()

    def initAutoAcquisition(self):
        if not self.btnChecked['Auto Acquisition']:
            self.serialPort.send_Auto_Acquisition(self.values['Data Sampling'])

            # self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_multiple_data)
            # self.serialPort.packet_received.connect(self.acquisitionReceive)

            self.valuesPhotodiodes['Photodiode A'] = []
            self.valuesPhotodiodes['Photodiode B'] = []

            self.btnChecked['Auto Acquisition'] = True

        else:
            self.serialPort.send_Finish_Experiment()

            self.btnChecked['Auto Acquisition'] = False

    def acquisitionChange(self):
        self.values['Data Sampling'] = self.viewCurveSetup.edtDataSampling.value()

    def acquisitionReceive(self, data):
        if data == '@':
            if self.btnChecked['Auto Acquisition']:
                self.viewCurveSetup.setAutoAcquisitionInProcess()

            else:
                self.serialPort.serialPort.readyRead.disconnect()
                self.serialPort.packet_received.disconnect()

                self.viewCurveSetup.setAutoAcquisitionFinish()

        elif data[0] == '&':
            self.valuesPhotodiodes['Photodiode A'].append(int(data[1] + data[2]))
            self.valuesPhotodiodes['Photodiode B'].append(int(data[3] + data[4]))

            self.dataReceived()

    def dataReceived(self):
        self.values['Acquisition Channel 1'] = self.valuesPhotodiodes['Photodiode A'][self.values['Automatic']]
        self.values['Acquisition Channel 2'] = self.valuesPhotodiodes['Photodiode B'][self.values['Automatic']]
        self.values['Automatic'] += 1

        self.viewCurveSetup.edtACQChannel_1.setText(str(self.values['Acquisition Channel 1']))
        self.viewCurveSetup.edtACQChannel_2.setText(str(self.values['Acquisition Channel 2']))
        self.viewCurveSetup.edtAcquisition.setText(str(self.values['Automatic']))

        if self.values['Automatic'] >= 48:
            self.viewCurveSetup.btnAutoAcquisition.setChecked(False)
            self.initAutoAcquisition()

    def receiveData(self, data):
        for value in data:
            if value == self.ackCommand:
                valueACK = self.bufferWaitACK.pop()

                if valueACK != -1:
                    self.tmrTimeout.stop()
                    self.tmrTimeout.timeout.disconnect()
                    valueACK()

    def setTimeout(self, messageTimeout, functionTimeout):
        self.btnTimeout = True
        self.viewSystemControl.setMessageCritical('Error', messageTimeout)
        functionTimeout()

        self.tmrTimeout.stop()
        self.tmrTimeout.timeout.disconnect()

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
