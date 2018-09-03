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
        self.acquisitionCommand = '&'
        self.experimentCommand = '|'
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
            'Acquisition Channel 2': 0,
            'Channel 1': 0.000,
            'Channel 2': 0.000,
            'Time': 0
        }
        self.valuesPhotodiodes = {
            'Photodiode A': [],
            'Photodiode B': []
        }

        self.valuesExperiment = {
            'Channel 1': [],
            'Channel 2': []
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

            self.values['Peristaltic'] = self.dataInit["PER1"]
            self.values['Impulsional A'] = self.dataInit["Impul1"]
            self.values['Impulsional B'] = self.dataInit["Impul2"]

            self.viewSystemControl.setEdtPeristalticValue(self.values['Peristaltic'])
            self.viewSystemControl.setEdtImpulsionalAValue(self.values['Impulsional A'])
            self.viewSystemControl.setEdtImpulsionalBValue(self.values['Impulsional B'])

            self.values['Gain A'] = self.dataInit["Gain1"]
            self.values['Gain B'] = self.dataInit["Gain2"]
            self.values['Offset A'] = self.dataInit["Offset1"]
            self.values['Offset B'] = self.dataInit["Offset2"]

            self.viewCurveSetup.setEdtGainAValue(self.values['Gain A'])
            self.viewCurveSetup.setEdtGainBValue(self.values['Gain B'])
            self.viewCurveSetup.setEdtOffsetAValue(self.values['Offset A'])
            self.viewCurveSetup.setEdtOffsetBValue(self.values['Offset B'])

            self.viewCurveSetup.setEdtInitialAngleValue(self.values['Init Angle'])
            self.viewCurveSetup.setEdtAngleLongitudeValue(self.values['Angle Longitude'])
            self.viewCurveSetup.setEdtAngleResolutionValue(self.values['Angle Resolution'])
            self.viewCurveSetup.setEdtFinalAngleValue(self.values['Final Angle'])
            self.viewCurveSetup.setEdtPointsCurveValue(self.values['Points Curve'])

            self.viewCurveSetup.setEdtAcquisitionText(self.values['Automatic'])
            self.viewCurveSetup.setEdtDataSamplingValue(self.values['Data Sampling'])
            self.viewCurveSetup.setEdtACQChannel1Text(self.values['Acquisition Channel 1'])
            self.viewCurveSetup.setEdtACQChannel2Text(self.values['Acquisition Channel 2'])

            self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
            self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
            self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

            """-------------------------------------- System Control Connects ---------------------------------------"""

            self.viewSystemControl.btnLaser.clicked.connect(self.btnLaserChanged)
            self.viewSystemControl.btnPeristaltic.clicked.connect(self.btnPeristalticChanged)
            self.viewSystemControl.btnImpulsional_A.clicked.connect(self.btnImpulsionalAChanged)
            self.viewSystemControl.btnImpulsional_B.clicked.connect(self.btnImpulsionalBChanged)

            self.viewSystemControl.edtPeristaltic.valueChanged.connect(self.edtPeristalticChanged)
            self.viewSystemControl.edtImpulsional_A.valueChanged.connect(self.edtImpulsionalsChanged)
            self.viewSystemControl.edtImpulsional_B.valueChanged.connect(self.edtImpulsionalsChanged)

            """------------------------------------ End System Control Connects -------------------------------------"""

            """---------------------------------------- Curve Setup Connects ----------------------------------------"""

            self.viewCurveSetup.btnCalibrate.clicked.connect(self.btnCalibrateChanged)
            self.viewCurveSetup.btnLaser.clicked.connect(self.btnLaserChanged)
            self.viewCurveSetup.btnReset.clicked.connect(self.btnResetChanged)

            self.viewCurveSetup.btnAutoAcquisition.clicked.connect(self.btnAutoAcquisitionChanged)

            self.viewCurveSetup.edtGainA.valueChanged.connect(self.edtCalibrateChanged)
            self.viewCurveSetup.edtGainB.valueChanged.connect(self.edtCalibrateChanged)
            self.viewCurveSetup.edtOffsetA.valueChanged.connect(self.edtCalibrateChanged)
            self.viewCurveSetup.edtOffsetB.valueChanged.connect(self.edtCalibrateChanged)

            self.viewCurveSetup.edtInitialAngle.valueChanged.connect(self.edtCurvePerformanceChanged)
            self.viewCurveSetup.edtAngleLongitude.valueChanged.connect(self.edtCurvePerformanceChanged)
            self.viewCurveSetup.edtAngleResolution.valueChanged.connect(self.edtCurvePerformanceChanged)

            self.viewCurveSetup.edtDataSampling.valueChanged.connect(self.edtAcquisitionChanged)

            """-------------------------------------- End Curve Setup Connects --------------------------------------"""

            """------------------------------------- Data Acquisition Connects --------------------------------------"""

            self.viewDataAcquisition.btnInitExperiment.clicked.connect(self.btnInitExperimentChanged)

            """----------------------------------- End Data Acquisition Connects ------------------------------------"""

            self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_multiple_data)
            self.serialPort.packet_received.connect(self.commandReceived)

            self.viewTabs.btnExit.clicked.connect(self.exit_App)

    """
    ********************************************************************************************************************
    *                                              Laser Control Functions                                             *
    ********************************************************************************************************************
    """

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
        self.viewDataAcquisition.setLedLaserStatus(self.btnChecked['Laser'])

        self.viewSystemControl.setBtnLaserDisable(False)
        self.viewCurveSetup.setBtnLaserDisable(False)

    """
    ********************************************************************************************************************
    *                                            End Laser Control Functions                                           *
    ********************************************************************************************************************
    """

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                        System Control Tab                                      ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    """
    ********************************************************************************************************************
    *                                           Peristaltic Control Functions                                          *
    ********************************************************************************************************************
    """

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
        if self.btnTimeout:
            status = not self.viewSystemControl.getBtnPeristalticStatus()
            self.btnTimeout = False

        else:
            status = self.viewSystemControl.getBtnPeristalticStatus()

        self.viewSystemControl.setBtnPeristalticStatus(status)
        self.viewSystemControl.setBtnPeristalticDisable(False)

    """
    ********************************************************************************************************************
    *                                         End Peristaltic Control Functions                                        *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Impulsionals Control Functions                                          *
    ********************************************************************************************************************
    """

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

    """
    ********************************************************************************************************************
    *                                        End Impulsionals Control Functions                                        *
    ********************************************************************************************************************
    """

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                      End System Control Tab                                    ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                       SPR Curve Setup Tab                                      ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    """
    ********************************************************************************************************************
    *                                        Calibration Parameters Functions                                          *
    ********************************************************************************************************************
    """

    def edtCalibrateChanged(self):
        self.viewCurveSetup.setBtnCalibrateStatus(False)

        self.values['Gain A'] = self.viewCurveSetup.getEdtGainAValue()
        self.values['Offset A'] = self.viewCurveSetup.getEdtOffsetAValue()
        self.values['Gain B'] = self.viewCurveSetup.getEdtGainBValue()
        self.values['Offset B'] = self.viewCurveSetup.getEdtOffsetBValue()

    def btnCalibrateChanged(self):
        self.viewCurveSetup.setBtnCalibrateDisable(True)

        toSend = [
            self.values['Gain A'],
            self.values['Offset A'],
            self.values['Gain B'],
            self.values['Offset B']
        ]

        self.serialPort.send_Gain_Offset(toSend)
        self.bufferWaitACK.append(self.calibrateCommandReceived)

        functionTimeout = partial(self.setTimeout, messageTimeout=self.viewCurveSetup.timeoutMessage['Calibrate'],
                                  functionTimeout=self.calibrateCommandReceived)
        self.tmrTimeout.timeout.connect(functionTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def calibrateCommandReceived(self):
        if self.btnTimeout:
            done = False
            self.btnTimeout = False

        else:
            done = True

        self.viewCurveSetup.setBtnCalibrateStatus(done)
        self.viewCurveSetup.setBtnCalibrateDisable(False)

    """
    ********************************************************************************************************************
    *                                       End Calibration Parameters Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Curve Performance Functions                                             *
    ********************************************************************************************************************
    """

    def edtCurvePerformanceChanged(self):
        self.viewCurveSetup.setBtnResetStatus(False)

        self.values['Init Angle'] = self.viewCurveSetup.getEdtInitialAngleValue()
        self.values['Angle Longitude'] = self.viewCurveSetup.getEdtAngleLongitudeValue()
        self.values['Angle Resolution'] = self.viewCurveSetup.getEdtAngleResolutionValue()
        self.values['Final Angle'] = int(self.viewCurveSetup.getEdtFinalAngleValue())
        self.values['Points Curve'] = int(self.viewCurveSetup.getEdtPointsCurveValue())

    def btnResetChanged(self):
        if self.viewCurveSetup.getBtnResetStatus():
            self.tmrBtnReset.singleShot(500, self.btnResetChanged)

            self.viewCurveSetup.setBtnResetDisable(True)

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

            self.viewCurveSetup.setBtnResetStatus(False)

        else:
            self.viewCurveSetup.setBtnResetDisable(False)
            self.viewCurveSetup.setBtnResetStatus(True)

            self.viewCurveSetup.edtInitialAngle.valueChanged.connect(self.edtCurvePerformanceChanged)
            self.viewCurveSetup.edtAngleLongitude.valueChanged.connect(self.edtCurvePerformanceChanged)
            self.viewCurveSetup.edtAngleResolution.valueChanged.connect(self.edtCurvePerformanceChanged)

    """
    ********************************************************************************************************************
    *                                        End Curve Performance Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Acquisition Mode Functions                                              *
    ********************************************************************************************************************
    """

    def edtAcquisitionChanged(self):
        self.values['Data Sampling'] = self.viewCurveSetup.getEdtDataSamplingValue()

    def btnAutoAcquisitionChanged(self):
        self.viewCurveSetup.setBtnAutoAcquisitionDisable(True)
        self.viewCurveSetup.setEdtDataSamplingDisable(True)

        laserSwitchOFF = False

        if self.viewCurveSetup.getBtnAutoAcquisitionStatus():

            if self.viewCurveSetup.getBtnLaserStatus():
                toSend = self.values['Data Sampling']

                self.serialPort.send_Auto_Acquisition(toSend)

                self.valuesPhotodiodes['Photodiode A'] = []
                self.valuesPhotodiodes['Photodiode B'] = []

                self.values['Acquisition Channel 1'] = 0
                self.values['Acquisition Channel 2'] = 0
                self.values['Automatic'] = 0

                self.viewCurveSetup.setEdtACQChannel1Text(self.values['Acquisition Channel 1'])
                self.viewCurveSetup.setEdtACQChannel2Text(self.values['Acquisition Channel 2'])
                self.viewCurveSetup.setEdtAcquisitionText(self.values['Automatic'])

            else:
                laserSwitchOFF = True

        else:
            self.serialPort.send_Finish_Experiment()

        if laserSwitchOFF:
            self.viewCurveSetup.setBtnAutoAcquisitionInProcess(False)
            self.viewCurveSetup.setMessageCritical('Error', 'It is necessary the laser is switch ON.')

        else:
            self.bufferWaitACK.append(self.acquisitionCommandReceived)

            functionTimeout = partial(self.setTimeout, messageTimeout=self.viewCurveSetup.timeoutMessage['Automatic'],
                                      functionTimeout=self.acquisitionCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def acquisitionCommandReceived(self):
        if self.btnTimeout:
            acquisitionInProcess = not self.viewCurveSetup.getBtnAutoAcquisitionStatus()
            self.btnTimeout = False

        else:
            acquisitionInProcess = self.viewCurveSetup.getBtnAutoAcquisitionStatus()

        self.viewCurveSetup.setBtnAutoAcquisitionInProcess(acquisitionInProcess)

    def acquisitionDataReceived(self, data):
        if self.viewCurveSetup.getBtnAutoAcquisitionStatus():
            self.valuesPhotodiodes['Photodiode A'].append(int(data[1] + data[2]))
            self.valuesPhotodiodes['Photodiode B'].append(int(data[3] + data[4]))

            self.values['Acquisition Channel 1'] = self.valuesPhotodiodes['Photodiode A'][self.values['Automatic']]
            self.values['Acquisition Channel 2'] = self.valuesPhotodiodes['Photodiode B'][self.values['Automatic']]
            self.values['Automatic'] += 1

            self.viewCurveSetup.setEdtACQChannel1Text(self.values['Acquisition Channel 1'])
            self.viewCurveSetup.setEdtACQChannel2Text(self.values['Acquisition Channel 2'])
            self.viewCurveSetup.setEdtAcquisitionText(self.values['Automatic'])

            if self.values['Automatic'] >= 5:
                self.viewCurveSetup.setBtnAutoAcquisitionInProcess(False)
                self.btnAutoAcquisitionChanged()

    """
    ********************************************************************************************************************
    *                                         End Acquisition Mode Functions                                           *
    ********************************************************************************************************************
    """

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                     End SPR Curve Setup Tab                                    ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                       Data Acquisition Tab                                     ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    def btnInitExperimentChanged(self):
        laserSwitchOFF = False

        if self.viewDataAcquisition.getBtnInitExperimentStatus():

            if self.viewDataAcquisition.getLedLaserStatus():
                self.serialPort.send_Init_Experiment()

                self.valuesExperiment['Channel 1'] = []
                self.valuesExperiment['Channel 2'] = []

                self.values['Channel 1'] = 0.0
                self.values['Channel 2'] = 0.0
                self.values['Time'] = 0

                self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
                self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
                self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

            else:
                laserSwitchOFF = True

        else:
            self.serialPort.send_Finish_Experiment()

        if laserSwitchOFF:
            self.viewDataAcquisition.setBtnInitExperimentStatus(False)
            self.viewDataAcquisition.setMessageCritical('Error', 'It is necessary the laser is switch ON.')

        else:

            self.bufferWaitACK.append(self.initExperimentCommandReceived)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=self.viewDataAcquisition.timeoutMessage['Init Experiment'],
                                      functionTimeout=self.initExperimentCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def initExperimentCommandReceived(self):
        if self.btnTimeout:
            self.viewDataAcquisition.setBtnInitExperimentStatus(not self.viewDataAcquisition.
                                                                getBtnInitExperimentStatus())
            self.btnTimeout = False

        else:
            self.viewDataAcquisition.setBtnInitExperimentStatus(self.viewDataAcquisition.getBtnInitExperimentStatus())

    def experimentDataReceived(self, data):
        if self.viewDataAcquisition.getBtnInitExperimentStatus():
            self.valuesExperiment['Channel 1'].append(float(data[1] + data[2]))
            self.valuesExperiment['Channel 2'].append(float(data[3] + data[4]))

            self.values['Channel 1'] = self.valuesExperiment['Channel 1'][self.values['Time']]
            self.values['Channel 2'] = self.valuesExperiment['Channel 2'][self.values['Time']]
            self.values['Time'] += 1

            self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
            self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
            self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    --------------------------------------------------------------------------------------------------------------------
    ----------                                     End Data Acquisition Tab                                   ---------- 
    --------------------------------------------------------------------------------------------------------------------
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """

    """
    ********************************************************************************************************************
    *                                               Extra Functions                                                    *
    ********************************************************************************************************************
    """

    def commandReceived(self, data):
        for value in data:
            if value == self.ackCommand:
                valueACK = self.bufferWaitACK.pop()

                if valueACK != -1:
                    self.tmrTimeout.stop()
                    self.tmrTimeout.timeout.disconnect()
                    valueACK()

            else:
                if value == self.acquisitionCommand:
                    self.acquisitionDataReceived(data)

                elif value == self.experimentCommand:
                    self.experimentDataReceived(data)

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

    """
    ********************************************************************************************************************
    *                                             End Extra Functions                                                  *
    ********************************************************************************************************************
    """


if __name__ == '__main__':
    app = QApplication([])

    window = ControllerTabs()
    sys.exit(app.exec_())
