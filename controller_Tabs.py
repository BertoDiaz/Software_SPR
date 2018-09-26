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
from lib import Strings
import winsound
import datetime
import sys
import csv


class ControllerTabs:
    def __init__(self):

        """-------------------------------------------- Global Variables --------------------------------------------"""

        self.serialPort = None
        self.dataInit = {}
        self.laserON = 1
        self.laserOFF = 0
        self.peristalticON = 1
        self.peristalticOFF = 0
        self.backPeristaltic = 0
        self.stopPeristaltic = 1
        self.forwardPeristaltic = 2
        self.msTimeout = 1000
        self.bufferWaitACK = Queue()
        self.btnTimeout = False
        self.baseX = 58.00
        self.axisYMax = 0
        self.axisYMin = 0
        # self.axisYMaxChannel1 = 0
        # self.axisYMinChannel1 = 0
        # self.axisYMaxChannel2 = 0
        # self.axisYMinChannel2 = 0
        self.myFileNameCalibration = datetime.datetime.now().strftime('%d-%m-%Y') + '_calibration.DAT'
        self.myFileNameMeasure = datetime.datetime.now().strftime('%d-%m-%Y') + '_measure.DAT'
        self.myFileCalibration = None
        self.myFileMeasure = None
        self.fileNameCalibration = None
        self.fileNameMeasure = None
        self.btnLaserChecked = False

        self.values = {
            'Peristaltic': 0,
            'Impulsional A': 0,
            'Impulsional B': 0,
            'Gain A': 0,
            'Gain B': 0,
            'Offset A': 0,
            'Offset B': 0,
            'Init Angle': 58,
            'Angle Longitude': 4,
            'Angle Resolution': 0.2,
            'Final Angle': 0,
            'Points Curve': 0,
            'Automatic': 0,
            'Data Sampling': 2,
            'Acquisition Channel 1': 0,
            'Acquisition Channel 2': 0,
            'Angle': 0,
            'Experiment Time': 10000,
            'Channel 1': 0.000,
            'Channel 2': 0.000,
            'Time': 0
        }
        self.valuesPhotodiodes = {
            'Photodiode A': [],
            'Photodiode B': [],
            'Angle': []
        }

        self.valuesExperiment = {
            'Channel 1': [],
            'Channel 2': [],
            'Time': []
        }

        """------------------------------------------ End Global Variables ------------------------------------------"""

        """------------------------------------------------ Timers --------------------------------------------------"""

        self.tmrBtnImpulsional_A = QTimer()
        self.tmrBtnImpulsional_B = QTimer()
        self.tmrBtnInject_A = QTimer()
        self.tmrBtnInject_B = QTimer()
        self.tmrBtnReset = QTimer()
        self.tmrBtnStopPeristaltic = QTimer()
        self.tmrTimeout = QTimer()

        """---------------------------------------------- End Timers ------------------------------------------------"""

        """------------------------------------------------- Tabs ---------------------------------------------------"""

        self.viewTabs = ViewTabs(None)
        self.viewSystemControl = self.viewTabs.tab_SystemControl
        self.viewCurveSetup = self.viewTabs.tab_CurveSetup
        self.viewDataAcquisition = self.viewTabs.tab_DataAcquisition

        """----------------------------------------------- End Tabs -------------------------------------------------"""

        """-------------------------------------------- Init View Tabs ----------------------------------------------"""

        self.viewTabs.mainWindow()
        self.viewSystemControl.mainWindow()
        self.viewCurveSetup.mainWindow()
        self.viewDataAcquisition.mainWindow()

        self.viewTabs.show()

        """------------------------------------------ End Init View Tabs --------------------------------------------"""

        """----------------------------------------- Init Controller Tabs -------------------------------------------"""

        self.run()

        """--------------------------------------- End Init Controller Tabs -----------------------------------------"""

    """
    ********************************************************************************************************************
    *                                                   Run Function                                                   *
    ********************************************************************************************************************
    """

    def run(self):
        """Init the app controller."""

        """Init the connection with the COM port."""
        controllerConnect = ControllerConnect()

        if controllerConnect.finish:
            self.exit_All()

        else:

            """Get the serial port connected and the initial data."""
            self.serialPort = controllerConnect.serialPort
            self.dataInit = controllerConnect.dataInit

            """Set the initial data in the view."""
            self.values['Peristaltic'] = self.dataInit['PER1']
            self.values['Impulsional A'] = self.dataInit['Impul1']
            self.values['Impulsional B'] = self.dataInit['Impul2']

            self.viewSystemControl.setEdtPeristalticValue(self.values['Peristaltic'])
            self.viewSystemControl.setEdtImpulsionalAValue(self.values['Impulsional A'])
            self.viewSystemControl.setEdtImpulsionalBValue(self.values['Impulsional B'])

            self.values['Gain A'] = self.dataInit['Gain1']
            self.values['Gain B'] = self.dataInit['Gain2']
            self.values['Offset A'] = self.dataInit['Offset1']
            self.values['Offset B'] = self.dataInit['Offset2']

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

            self.viewCurveSetup.setEdtSaveFileText(self.myFileNameCalibration)

            self.viewDataAcquisition.setEdtExperimentTimeValue(self.values['Experiment Time'])
            self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
            self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
            self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

            self.viewDataAcquisition.setEdtSaveFileText(self.myFileNameMeasure)

            """-------------------------------------- System Control Connects ---------------------------------------"""

            self.viewSystemControl.btnLaser.clicked.connect(self.btnLaserChanged)

            btnPeristalticParameters = partial(self.btnPeristalticChanged, who=self.viewSystemControl)
            self.viewSystemControl.btnPeristaltic.clicked.connect(btnPeristalticParameters)

            btnImpulsionalAParameters = partial(self.btnImpulsionalAChanged, who=self.viewSystemControl)
            self.viewSystemControl.btnImpulsional_A.clicked.connect(btnImpulsionalAParameters)

            btnImpulsionalBParameters = partial(self.btnImpulsionalBChanged, who=self.viewSystemControl)
            self.viewSystemControl.btnImpulsional_B.clicked.connect(btnImpulsionalBParameters)

            edtPeristalticParameters = partial(self.edtPeristalticChanged, who=self.viewSystemControl)
            self.viewSystemControl.edtPeristaltic.valueChanged.connect(edtPeristalticParameters)

            edtImpulsionalAParameters = partial(self.edtImpulsionalsChanged, who=self.viewSystemControl)
            self.viewSystemControl.edtImpulsional_A.valueChanged.connect(edtImpulsionalAParameters)

            edtImpulsionalBParameters = partial(self.edtImpulsionalsChanged, who=self.viewSystemControl)
            self.viewSystemControl.edtImpulsional_B.valueChanged.connect(edtImpulsionalBParameters)

            """------------------------------------ End System Control Connects -------------------------------------"""

            """---------------------------------------- Curve Setup Connects ----------------------------------------"""

            self.viewCurveSetup.btnCalibrate.clicked.connect(self.btnCalibrateChanged)
            self.viewCurveSetup.btnLaser.clicked.connect(self.btnLaserChanged)
            self.viewCurveSetup.btnReset.clicked.connect(self.btnResetChanged)
            self.viewCurveSetup.btnAutoAcquisition.clicked.connect(self.btnAutoAcquisitionChanged)
            self.viewCurveSetup.btnSaveFile.clicked.connect(self.btnSaveFileCalibrationChanged)

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
            self.viewDataAcquisition.btnLaser.clicked.connect(self.btnLaserChanged)

            btnPeristalticParameters = partial(self.btnPeristalticChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.btnPeristaltic.clicked.connect(btnPeristalticParameters)

            btnImpulsionalAParameters = partial(self.btnImpulsionalAChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.btnPurge_A.clicked.connect(btnImpulsionalAParameters)

            btnImpulsionalBParameters = partial(self.btnImpulsionalBChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.btnPurge_B.clicked.connect(btnImpulsionalBParameters)

            self.viewDataAcquisition.btnInject_A.clicked.connect(self.btnInjectAChanged)
            self.viewDataAcquisition.btnInject_B.clicked.connect(self.btnInjectBChanged)

            btnBackPeristaltic = partial(self.btnBSFPeristalticChanged, who=self.backPeristaltic)
            self.viewDataAcquisition.btnBackPeristaltic.clicked.connect(btnBackPeristaltic)

            btnStopPeristaltic = partial(self.btnBSFPeristalticChanged, who=self.stopPeristaltic)
            self.viewDataAcquisition.btnStopPeristaltic.clicked.connect(btnStopPeristaltic)

            btnForwardPeristaltic = partial(self.btnBSFPeristalticChanged, who=self.forwardPeristaltic)
            self.viewDataAcquisition.btnForwardPeristaltic.clicked.connect(btnForwardPeristaltic)

            self.viewDataAcquisition.btnSaveFile.clicked.connect(self.btnSaveFileMeasureChanged)
            self.viewDataAcquisition.btnAutoscaleYChannel.clicked.connect(self.btnAutoscaleYChanged)
            self.viewDataAcquisition.btnAutoscaleXChannel.clicked.connect(self.btnAutoscaleXChanged)
            self.viewDataAcquisition.btnChart1000Channel.clicked.connect(self.btnChart1000Changed)
            self.viewDataAcquisition.btnChart10000Channel.clicked.connect(self.btnChart10000Changed)
            # self.viewDataAcquisition.btnAutoscaleYChannel1.clicked.connect(self.btnAutoscaleYChannel1Changed)
            # self.viewDataAcquisition.btnAutoscaleXChannel1.clicked.connect(self.btnAutoscaleXChannel1Changed)
            # self.viewDataAcquisition.btnChart1000Channel1.clicked.connect(self.btnChart1000Channel1Changed)
            # self.viewDataAcquisition.btnChart10000Channel1.clicked.connect(self.btnChart10000Channel1Changed)
            # self.viewDataAcquisition.btnAutoscaleYChannel2.clicked.connect(self.btnAutoscaleYChannel2Changed)
            # self.viewDataAcquisition.btnAutoscaleXChannel2.clicked.connect(self.btnAutoscaleXChannel2Changed)
            # self.viewDataAcquisition.btnChart1000Channel2.clicked.connect(self.btnChart1000Channel2Changed)
            # self.viewDataAcquisition.btnChart10000Channel2.clicked.connect(self.btnChart10000Channel2Changed)

            self.viewDataAcquisition.edtExperimentTime.valueChanged.connect(self.edtExperimentTimeChanged)

            edtPeristalticParameters = partial(self.edtPeristalticChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.edtPeristaltic.valueChanged.connect(edtPeristalticParameters)

            edtImpulsionalAParameters = partial(self.edtImpulsionalsChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.edtImpulsional_A.valueChanged.connect(edtImpulsionalAParameters)

            edtImpulsionalBParameters = partial(self.edtImpulsionalsChanged, who=self.viewDataAcquisition)
            self.viewDataAcquisition.edtImpulsional_B.valueChanged.connect(edtImpulsionalBParameters)

            """----------------------------------- End Data Acquisition Connects ------------------------------------"""

            """---------------------------------------- Serial Port Connects ----------------------------------------"""

            self.serialPort.serialPort.readyRead.connect(self.serialPort.receive_multiple_data)
            self.serialPort.packet_received.connect(self.commandReceived)

            """-------------------------------------- End Serial Port Connects --------------------------------------"""

            """-------------------------------------- Close App Button Connect --------------------------------------"""

            self.viewTabs.btnExit.clicked.connect(self.exit_App)

            """------------------------------------ End Close App Button Connect ------------------------------------"""

    """
    ********************************************************************************************************************
    *                                                End Run Function                                                  *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                              Laser Control Functions                                             *
    ********************************************************************************************************************
    """

    def btnLaserChanged(self):
        """Control the action when the laser buttons are de/pressed.

        The function disable the laser buttons, if the button is de/pressed the command to switch on/off the laser is
        sent. Also, the timeout to wait for the ACK command is activated.
        """
        self.viewSystemControl.setBtnLaserDisable(True)
        self.viewCurveSetup.setBtnLaserDisable(True)
        self.viewDataAcquisition.setBtnLaserDisable(True)

        if not self.btnLaserChecked:
            self.btnLaserChecked = True
            toSend = self.laserON

        else:
            self.btnLaserChecked = False
            toSend = self.laserOFF

        self.serialPort.send_Laser(toSend)
        self.bufferWaitACK.append(self.laserCommandReceived)

        messageTimeout = partial(self.setTimeout, messageTimeout=Strings.messageTimeoutLaser,
                                 functionTimeout=self.laserCommandReceived)
        self.tmrTimeout.timeout.connect(messageTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def laserCommandReceived(self):
        """Control the action when ACK command is/is not received.

        When the ACK command is received the laser buttons and led are activated, and the laser buttons are enabled
        again. If the ACK command is not received and the timeout is finished, the laser buttons are put in not pressed
        state (initial state).
        """
        if self.btnTimeout:
            self.btnLaserChecked = not self.btnLaserChecked
            self.btnTimeout = False

        self.viewSystemControl.setBtnLaserStatus(self.btnLaserChecked)
        self.viewCurveSetup.setBtnLaserStatus(self.btnLaserChecked)
        self.viewDataAcquisition.setBtnLaserStatus(self.btnLaserChecked)
        self.viewCurveSetup.setLedLaserStatus(self.btnLaserChecked)

        self.viewSystemControl.setBtnLaserDisable(False)
        self.viewCurveSetup.setBtnLaserDisable(False)
        self.viewDataAcquisition.setBtnLaserDisable(False)

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

    def edtPeristalticChanged(self, who):
        """Control the action when the peristaltic line edits are changed.

        The value of the peristaltic line edit is get and set in the both peristaltic line edit, then, the status of the
        peristaltic buttons are True, the command to switch on the peristaltic with the new value of the speed are sent
        and the timeout to wait for the ACK command is activated.

        Args:
            who (ViewTabs): the tab where the edit line was changed.
        """
        self.values['Peristaltic'] = who.getEdtPeristalticValue()

        self.viewSystemControl.setEdtPeristalticValue(self.values['Peristaltic'])
        self.viewDataAcquisition.setEdtPeristalticValue(self.values['Peristaltic'])

        if who.getBtnPeristalticStatus():
            toSend = [
                self.peristalticON,
                self.values['Peristaltic']
            ]

            self.serialPort.send_Control_Peristaltic(toSend)
            self.bufferWaitACK.append(self.peristalticCommandReceived)

            functionTimeout = partial(self.setTimeout, messageTimeout=Strings.messageTimeoutPeristaltic,
                                      functionTimeout=self.peristalticCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def btnPeristalticChanged(self, who):
        """Control the action when the peristaltic buttons are de/pressed.

        The buttons are disabled, then, if the button is de/pressed, the command to switch on/off the peristaltic with
        the value of the speed are sent. And the timeout to wait for the ACK command is activated.

        Args:
            who (ViewTabs): the tab where the button was pressed.
        """
        self.viewSystemControl.setBtnPeristalticDisable(True)
        self.viewDataAcquisition.setBtnPeristalticDisable(True)

        if who.getBtnPeristalticStatus():
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
        peristalticCommand = partial(self.peristalticCommandReceived, who=who)
        self.bufferWaitACK.append(peristalticCommand)

        functionTimeout = partial(self.setTimeout, messageTimeout=Strings.messageTimeoutPeristaltic,
                                  functionTimeout=peristalticCommand)
        self.tmrTimeout.timeout.connect(functionTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def peristalticCommandReceived(self, who):
        """Control the action when ACK command is/is not received in order to peristaltic.

        When the ACK command is received the peristaltic buttons are activated and are enabled again. If the ACK command
        is not received and the timeout is finished, the peristaltic buttons are put in not pressed state (initial
        state).

        Args:
            who (ViewTabs): the tab where the button was pressed or the edit line was changed.
        """
        if self.btnTimeout:
            status = not who.getBtnPeristalticStatus()
            self.btnTimeout = False

        else:
            status = who.getBtnPeristalticStatus()

        self.viewSystemControl.setBtnPeristalticStatus(status)
        self.viewDataAcquisition.setBtnPeristalticStatus(status)
        self.viewSystemControl.setBtnPeristalticDisable(False)
        self.viewDataAcquisition.setBtnPeristalticDisable(False)

    def btnBSFPeristalticChanged(self, who):
        """Control the action when the peristaltic buttons (Back, Stop and Forward) are pressed.

        If the button is pressed, the others buttons are depressed and all buttons are disabled, the command to do the
        action is sent and the timeout to wait for the ACK command is activated.

        Args:
            who (int): what button was pressed.
        """
        if self.viewDataAcquisition.getBtnBSFPeristalticStatus(who):

            self.viewDataAcquisition.setBtnBSFPeristalticNotStatus(False, who)

            self.viewDataAcquisition.setBtnBSFPeristalticDisable(True)
            self.serialPort.send_BSF_Peristaltic(who)
            peristalticCommand = partial(self.bsfPeristalticCommandReceived, who=who)
            self.bufferWaitACK.append(peristalticCommand)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=Strings.messageTimeoutPeristaltic,
                                      functionTimeout=peristalticCommand)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def bsfPeristalticCommandReceived(self, who):
        """Control the action when ACK command is/is not received in order to (Back, Stop and Forward) peristaltic.

        When the ACK command is received the peristaltic buttons are activated and are enabled again. If the ACK command
        is not received and the timeout is finished, the peristaltic buttons are put in not pressed state (initial
        state).

        Args:
            who (int): what button was pressed.
        """
        if self.btnTimeout:
            status = not self.viewDataAcquisition.getBtnBSFPeristalticStatus(who)
            self.btnTimeout = False

        else:
            status = self.viewDataAcquisition.getBtnBSFPeristalticStatus(who)

            if who == self.stopPeristaltic:
                self.tmrBtnStopPeristaltic.singleShot(500, self.btnStopPeristalticOFF)

        self.viewDataAcquisition.setBtnBSFPeristalticStatus(status, who)
        self.viewDataAcquisition.setBtnBSFPeristalticDisable(False)

    def btnStopPeristalticOFF(self):
        self.viewDataAcquisition.setBtnStopPeristalticStatus(False)

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

    def edtImpulsionalsChanged(self, who):
        """Control the action when the impulsional line edits are changed.

        The value of the impulsional line edit is get and set in the both impulsional line edits.

        Args:
            who (ViewTabs): the tab where the edit line was changed.
        """
        self.values['Impulsional A'] = who.getEdtImpulsionalAValue()
        self.values['Impulsional B'] = who.getEdtImpulsionalBValue()

        self.viewSystemControl.setEdtImpulsionalAValue(self.values['Impulsional A'])
        self.viewDataAcquisition.setEdtImpulsionalAValue(self.values['Impulsional A'])
        self.viewSystemControl.setEdtImpulsionalBValue(self.values['Impulsional B'])
        self.viewDataAcquisition.setEdtImpulsionalBValue(self.values['Impulsional B'])

    def btnImpulsionalAChanged(self, who):
        """Control the action when the impulsional A buttons are pressed.

        If the buttons are pressed and the line edits are other than 0, the buttons in the different tabs are changed to
        True state, the value is adjusted to the volume of the impulsional, the command is sent and the timeout to wait
        for the ACK command is activated. In the case that the line edits are equal to 0, the buttons are disabled and
        a message to change the value is showed.

        Args:
            who (ViewTabs): the tab where the button was pressed.
        """
        if who.getBtnImpulsionalAStatus():

            if who.getEdtImpulsionalAValue() != 0:
                self.changeImpulsionalAStatus(True)

                toSend = self.values['Impulsional A'] * 50

                self.serialPort.send_Control_Impul_A(toSend)
                self.bufferWaitACK.append(self.impulsionalACommandReceived)

                functionTimeout = partial(self.setTimeout,
                                          messageTimeout=Strings.messageTimeoutImpulsionalA,
                                          functionTimeout=self.impulsionalACommandReceived)
                self.tmrTimeout.timeout.connect(functionTimeout)
                self.tmrTimeout.start(self.msTimeout)

            else:
                self.changeImpulsionalAStatus(False)
                self.viewSystemControl.setMessageCritical(Strings.messageNotCeroImpulsionalA)

    def impulsionalACommandReceived(self):
        """Control the action when ACK command is/is not received in order to impulsional A.

        When the ACK command is received the time of the impulses is calculated and the timer for depressed the
        impulsional A buttons is activated. In the case that the ACK command is not received the time of the impulses is
        0 and the impulsional A buttons are depressed.
        """
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = self.values['Impulsional A'] * 500

        finishImpulses = partial(self.changeImpulsionalAStatus, status=False)
        self.tmrBtnImpulsional_A.singleShot(timeImpulses, finishImpulses)

    def changeImpulsionalAStatus(self, status):
        """Change the status of the impulsional A buttons.

        The impulsional A buttons are pressed or depressed according to status.

        Args:
            status (bool): the value to change the status of the impulsional A buttons.
        """
        self.viewSystemControl.setBtnImpulsionalAStatus(status)
        self.viewDataAcquisition.setBtnImpulsionalAStatus(status)

    def btnInjectAChanged(self):
        """Control the action when the inject A button is de/pressed.

        If the button is pressed, the button is disabled and the command to do one injection is sent and the timeout to
        wait for the ACK command is activated. In the case that the button is depressed, the button is enabled and
        depressed (initial state, status = False).
        """
        if self.viewDataAcquisition.getBtnInjectAStatus():
            self.viewDataAcquisition.setBtnInjectADisable(True)
            toSend = 50

            self.serialPort.send_Control_Impul_A(toSend)
            self.bufferWaitACK.append(self.injectACommandReceived)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=Strings.messageTimeoutImpulsionalA,
                                      functionTimeout=self.injectACommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

        else:
            self.viewDataAcquisition.setBtnInjectAStatus(False)
            self.viewDataAcquisition.setBtnInjectADisable(False)

    def injectACommandReceived(self):
        """Control the action when ACK command is/is not received in order to inject A.

        When the ACK command is received the timer for depressed the inject A button is activated for one injection. In
        the case that the ACK command is not received the time of the injection is 0 and the inject A button is
        depressed.
        """
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = 500

        finishImpulses = partial(self.viewDataAcquisition.setBtnInjectAStatus, status=False)
        self.tmrBtnInject_A.singleShot(timeImpulses, finishImpulses)

    def btnImpulsionalBChanged(self, who):
        """Control the action when the impulsional B buttons are pressed.

        If the buttons are pressed and the line edits are other than 0, the buttons in the different tabs are changed to
        True state, the value is adjusted to the volume of the impulsional, the command is sent and the timeout to wait
        for the ACK command is activated. In the case that the line edits are equal to 0, the buttons are disabled and
        a message to change the value is showed.

        Args:
            who (ViewTabs): the tab where the button was pressed.
        """
        if who.getBtnImpulsionalBStatus():

            if who.getEdtImpulsionalBValue() != 0:
                self.changeImpulsionalBStatus(True)

                toSend = self.values['Impulsional B'] * 50

                self.serialPort.send_Control_Impul_B(toSend)
                self.bufferWaitACK.append(self.impulsionalBCommandReceived)

                functionTimeout = partial(self.setTimeout,
                                          messageTimeout=Strings.messageTimeoutImpulsionalB,
                                          functionTimeout=self.impulsionalBCommandReceived)
                self.tmrTimeout.timeout.connect(functionTimeout)
                self.tmrTimeout.start(self.msTimeout)

            else:
                self.changeImpulsionalBStatus(False)
                self.viewSystemControl.setMessageCritical(Strings.messageNotCeroImpulsionalB)

    def impulsionalBCommandReceived(self):
        """Control the action when ACK command is/is not received in order to impulsional B.

        When the ACK command is received the time of the impulses is calculated and the timer for depressed the
        impulsional A buttons is activated. In the case that the ACK command is not received the time of the impulses is
        0 and the impulsional B buttons are depressed.
        """
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = self.values['Impulsional B'] * 500

        finishImpulses = partial(self.changeImpulsionalBStatus, status=False)
        self.tmrBtnImpulsional_B.singleShot(timeImpulses, finishImpulses)

    def changeImpulsionalBStatus(self, status):
        """Change the status of the impulsional B buttons.

        The impulsional B buttons are pressed or depressed according to status.

        Args:
            status (bool): the value to change the status of the impulsional B buttons.
        """
        self.viewSystemControl.setBtnImpulsionalBStatus(status)
        self.viewDataAcquisition.setBtnImpulsionalBStatus(status)

    def btnInjectBChanged(self):
        """Control the action when the inject B button is de/pressed.

        If the button is pressed, the button is disabled and the command to do one injection is sent and the timeout to
        wait for the ACK command is activated. In the case that the button is depressed, the button is enabled and
        depressed (initial state, status = False).
        """
        if self.viewDataAcquisition.getBtnInjectBStatus():
            self.viewDataAcquisition.setBtnInjectBDisable(True)
            toSend = 50

            self.serialPort.send_Control_Impul_B(toSend)
            self.bufferWaitACK.append(self.injectBCommandReceived)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=Strings.messageTimeoutImpulsionalB,
                                      functionTimeout=self.injectBCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

        else:
            self.viewDataAcquisition.setBtnInjectBStatus(False)
            self.viewDataAcquisition.setBtnInjectBDisable(False)

    def injectBCommandReceived(self):
        """Control the action when ACK command is/is not received in order to inject B.

        When the ACK command is received the timer for depressed the inject B button is activated for one injection. In
        the case that the ACK command is not received the time of the injection is 0 and the inject B button is
        depressed.
        """
        if self.btnTimeout:
            timeImpulses = 0
            self.btnTimeout = False

        else:
            timeImpulses = 500

        finishImpulses = partial(self.viewDataAcquisition.setBtnInjectBStatus, status=False)
        self.tmrBtnInject_B.singleShot(timeImpulses, finishImpulses)

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
        """Control the action when the calibrate line edits are changed.

        The calibrate button is set to depressed (False status) and the values of the line edits are get.
        """
        self.viewCurveSetup.setBtnCalibrateStatus(False)

        self.values['Gain A'] = self.viewCurveSetup.getEdtGainAValue()
        self.values['Offset A'] = self.viewCurveSetup.getEdtOffsetAValue()
        self.values['Gain B'] = self.viewCurveSetup.getEdtGainBValue()
        self.values['Offset B'] = self.viewCurveSetup.getEdtOffsetBValue()

    def btnCalibrateChanged(self):
        """Control the action when the calibrate button is pressed.

        When the button is pressed, the button is disabled, the command with the values of the calibration is sent and
        the timeout to wait for the ACK command is activated.
        """
        self.viewCurveSetup.setBtnCalibrateDisable(True)

        toSend = [
            self.values['Gain A'],
            self.values['Offset A'],
            self.values['Gain B'],
            self.values['Offset B']
        ]

        self.serialPort.send_Gain_Offset(toSend)
        self.bufferWaitACK.append(self.calibrateCommandReceived)

        functionTimeout = partial(self.setTimeout, messageTimeout=Strings.messageTimeoutCalibrate,
                                  functionTimeout=self.calibrateCommandReceived)
        self.tmrTimeout.timeout.connect(functionTimeout)
        self.tmrTimeout.start(self.msTimeout)

    def calibrateCommandReceived(self):
        """Control the action when ACK command is/is not received in order to calibrate.

        When the ACK command is received the calibrate button is depressed, enabled and changed the style.
        """
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
        """Control the action when the curve performance line edits are changed.

        The reset button is depressed (False status) and the values of the line edits are get.
        """
        self.viewCurveSetup.setBtnResetStatus(False)

        self.values['Init Angle'] = self.viewCurveSetup.getEdtInitialAngleValue()
        self.values['Angle Longitude'] = self.viewCurveSetup.getEdtAngleLongitudeValue()
        self.values['Angle Resolution'] = self.viewCurveSetup.getEdtAngleResolutionValue()
        self.values['Final Angle'] = int(self.viewCurveSetup.getEdtFinalAngleValue())
        self.values['Points Curve'] = int(self.viewCurveSetup.getEdtPointsCurveValue())

    def btnResetChanged(self):
        """Control the action when the reset button is de/pressed.

        If the button is pressed, the timer to do the reset is activated, the button is disabled, the line edits are
        disabled, the initial values are set in the line edits and the button is depressed. If the button is depressed,
        the button is enabled, pressed and the line edits are enabled.
        """
        if self.viewCurveSetup.getBtnResetStatus():
            self.tmrBtnReset.singleShot(500, self.btnResetChanged)

            self.viewCurveSetup.setBtnResetDisable(True)

            self.viewCurveSetup.edtInitialAngle.valueChanged.disconnect()
            self.viewCurveSetup.edtAngleLongitude.valueChanged.disconnect()
            self.viewCurveSetup.edtAngleResolution.valueChanged.disconnect()

            self.values['Init Angle'] = 58
            self.values['Angle Longitude'] = 4
            self.values['Angle Resolution'] = 0.2
            self.values['Final Angle'] = self.values['Init Angle'] + self.values['Angle Longitude']
            self.values['Points Curve'] = (self.values['Angle Longitude'] / self.values['Angle Resolution']) + 1

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
        """Control the action when the acquisition line edit is changed.

        The value of the data sampling line edit is updated.
        """
        self.values['Data Sampling'] = self.viewCurveSetup.getEdtDataSamplingValue()

    def btnAutoAcquisitionChanged(self):
        """Control the action when the autoacquisition button is de/pressed.

        The button and the data sampling line edit are disabled. If the autoacquisition button and laser button are
        pressed, the command to start the acquisition is sent, the values to the charts are initialised, if the laser
        button is depressed, the laser switch off flag is activated. In the case that the autoacquisition button is
        depressed, the command to finish the acquisition is sent.
        Also, if the laser switch off flag is activated, the autoacquisition button is depressed (initial status), if,
        instead, the laser switch off flag is deactivated the timeout to wait for the ACK command is activated.
        """
        self.viewCurveSetup.setBtnAutoAcquisitionDisable(True)
        self.viewCurveSetup.setEdtDataSamplingDisable(True)

        laserSwitchOFF = False

        if self.viewCurveSetup.getBtnAutoAcquisitionStatus():

            if self.viewCurveSetup.getBtnLaserStatus():
                toSend = self.values['Data Sampling']

                self.serialPort.send_Auto_Acquisition(toSend)

                # self.viewCurveSetup.initSerieChannel1()
                # self.viewCurveSetup.initSerieChannel2()

                self.viewCurveSetup.initSerieChannel()

                self.valuesPhotodiodes['Photodiode A'] = []
                self.valuesPhotodiodes['Photodiode B'] = []
                self.valuesPhotodiodes['Time'] = []

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
            self.viewCurveSetup.setMessageCritical(Strings.messageNecessaryLaserON)

        else:
            self.bufferWaitACK.append(self.acquisitionCommandReceived)

            functionTimeout = partial(self.setTimeout, messageTimeout=Strings.messageTimeoutAutomatic,
                                      functionTimeout=self.acquisitionCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def acquisitionCommandReceived(self):
        """Control the action when ACK command is/is not received in order to autoacquisition.

        When the ACK command is received and the autoacquisition button is depressed, the auto save function is
        executed. Instead, if the timeout is finished and the ACK command is not received, the autoacquisition button is
        depressed.
        """
        if self.btnTimeout:
            acquisitionInProcess = not self.viewCurveSetup.getBtnAutoAcquisitionStatus()
            self.btnTimeout = False

        else:
            acquisitionInProcess = self.viewCurveSetup.getBtnAutoAcquisitionStatus()

            if not acquisitionInProcess:
                self.autoSaveFileCalibration()

        self.viewCurveSetup.setBtnAutoAcquisitionInProcess(acquisitionInProcess)

    def acquisitionDataReceived(self, data):
        if self.viewCurveSetup.getBtnAutoAcquisitionStatus():

            self.setBeep()

            self.valuesPhotodiodes['Photodiode A'].append(int(data[1] + data[2]))
            self.valuesPhotodiodes['Photodiode B'].append(int(data[3] + data[4]))
            self.valuesPhotodiodes['Angle'].append(self.baseX + (self.values['Automatic'] * 0.2))

            self.values['Acquisition Channel 1'] = self.valuesPhotodiodes['Photodiode A'][self.values['Automatic']]
            self.values['Acquisition Channel 2'] = self.valuesPhotodiodes['Photodiode B'][self.values['Automatic']]
            self.values['Angle'] = self.valuesPhotodiodes['Angle'][self.values['Automatic']]

            self.values['Automatic'] += 1

            self.viewCurveSetup.setEdtACQChannel1Text(self.values['Acquisition Channel 1'])
            self.viewCurveSetup.setEdtACQChannel2Text(self.values['Acquisition Channel 2'])
            self.viewCurveSetup.setEdtAcquisitionText(self.values['Automatic'])

            # self.viewCurveSetup.setDataChannel1(self.values['Angle'], self.values['Acquisition Channel 1'])
            # self.viewCurveSetup.setDataChannel2(self.values['Angle'], self.values['Acquisition Channel 2'])

            # valueX1 = self.values['Acquisition Channel 1'] - self.valuesPhotodiodes['Photodiode A'][0]
            # valueX2 = self.values['Acquisition Channel 2'] - self.valuesPhotodiodes['Photodiode B'][0]

            valueX1 = self.values['Acquisition Channel 1']
            valueX2 = self.values['Acquisition Channel 2']

            self.viewCurveSetup.setDataChannel(self.values['Angle'], valueX1, valueX2)

            if self.values['Automatic'] >= self.values['Points Curve']:
                self.viewCurveSetup.setBtnAutoAcquisitionInProcess(False)
                self.btnAutoAcquisitionChanged()

    """
    ********************************************************************************************************************
    *                                         End Acquisition Mode Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                Save File Functions                                               *
    ********************************************************************************************************************
    """

    def autoSaveFileCalibration(self):
        if self.fileNameCalibration is not None:
            self.myFileCalibration = open(self.fileNameCalibration, Strings.write)

            myData = [[Strings.angle, Strings.channel1UC, Strings.channel2UC]]

            for i in range(0, len(self.valuesPhotodiodes['Photodiode A'])):
                myData.append([self.valuesPhotodiodes['Angle'][i], self.valuesPhotodiodes['Photodiode A'][i],
                               self.valuesPhotodiodes['Photodiode B'][i]])

            with self.myFileCalibration:
                writer = csv.writer(self.myFileCalibration, delimiter='\t')
                writer.writerows(myData)

        else:
            if self.viewCurveSetup.setMessageQuestion(Strings.messageSaveData):
                self.btnSaveFileCalibrationChanged()

            else:
                pass

    def btnSaveFileCalibrationChanged(self):

            self.myFileNameCalibration = self.viewCurveSetup.getEdtSaveFileText()

            self.fileNameCalibration = self.viewCurveSetup.setDialogSaveFile(self.myFileNameCalibration)

            if self.fileNameCalibration != '':
                self.myFileCalibration = open(self.fileNameCalibration, Strings.write)

                if len(self.valuesPhotodiodes['Photodiode A']) > 0:

                    myData = [[Strings.angle, Strings.channel1UC, Strings.channel2UC]]

                    for i in range(0, len(self.valuesPhotodiodes['Photodiode A'])):
                        myData.append([self.valuesPhotodiodes['Angle'][i], self.valuesPhotodiodes['Photodiode A'][i],
                                       self.valuesPhotodiodes['Photodiode B'][i]])

                    with self.myFileCalibration:
                        writer = csv.writer(self.myFileCalibration, delimiter='\t')
                        writer.writerows(myData)

            else:
                pass

    """
    ********************************************************************************************************************
    *                                              End Save File Functions                                             *
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

    """
    ********************************************************************************************************************
    *                                           Init Experiment Functions                                              *
    ********************************************************************************************************************
    """

    def btnInitExperimentChanged(self):
        laserSwitchOFF = False
        peristalticSwitchOFF = False
        experimentTimeChange = False

        if self.viewDataAcquisition.getBtnInitExperimentStatus():

            if self.viewDataAcquisition.getBtnLaserStatus():

                if self.viewDataAcquisition.getBtnPeristalticStatus():

                    if not self.viewDataAcquisition.setMessageQuestion(Strings.messageChangeExperimentTimePart1 +
                                                                       str(self.values['Experiment Time']) +
                                                                       Strings.messageChangeExperimentTimePart2):

                        self.serialPort.send_Init_Experiment()

                        # self.viewDataAcquisition.initSerieChannel1()
                        # self.viewDataAcquisition.initSerieChannel2()

                        self.viewDataAcquisition.initSeries()

                        self.valuesExperiment['Channel 1'] = []
                        self.valuesExperiment['Channel 2'] = []

                        self.values['Channel 1'] = 0.0
                        self.values['Channel 2'] = 0.0
                        self.values['Time'] = 0

                        self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
                        self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
                        self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

                    else:
                        experimentTimeChange = True

                else:
                    peristalticSwitchOFF = True

            else:
                laserSwitchOFF = True

        else:
            self.serialPort.send_Finish_Experiment()

        if laserSwitchOFF:
            self.viewDataAcquisition.setBtnInitExperimentStatus(False)
            self.viewDataAcquisition.setMessageCritical(Strings.messageNecessaryLaserON)

        elif peristalticSwitchOFF:
            self.viewDataAcquisition.setBtnInitExperimentStatus(False)
            self.viewDataAcquisition.setMessageCritical(Strings.messageNecessaryPeristalticON)

        elif experimentTimeChange:
            self.viewDataAcquisition.setBtnInitExperimentStatus(False)

        else:

            self.bufferWaitACK.append(self.initExperimentCommandReceived)

            functionTimeout = partial(self.setTimeout,
                                      messageTimeout=Strings.messageTimeoutInitExperiment,
                                      functionTimeout=self.initExperimentCommandReceived)
            self.tmrTimeout.timeout.connect(functionTimeout)
            self.tmrTimeout.start(self.msTimeout)

    def initExperimentCommandReceived(self):
        if self.btnTimeout:
            self.viewDataAcquisition.setBtnInitExperimentStatus(not self.viewDataAcquisition.
                                                                getBtnInitExperimentStatus())
            self.btnTimeout = False

        else:

            if not self.viewDataAcquisition.getBtnInitExperimentStatus():
                self.autoSaveFileMeasure()

            self.viewDataAcquisition.setBtnInitExperimentStatus(self.viewDataAcquisition.getBtnInitExperimentStatus())

    def experimentDataReceived(self, data):
        if self.viewDataAcquisition.getBtnInitExperimentStatus():
            self.valuesExperiment['Channel 1'].append(float(data[1] + data[2]))
            self.valuesExperiment['Channel 2'].append(float(data[3] + data[4]))
            self.valuesExperiment['Time'].append(self.values['Time'])

            self.values['Channel 1'] = self.valuesExperiment['Channel 1'][self.values['Time']]
            self.values['Channel 2'] = self.valuesExperiment['Channel 2'][self.values['Time']]

            self.viewDataAcquisition.setEdtChannel1Text(self.values['Channel 1'])
            self.viewDataAcquisition.setEdtChannel2Text(self.values['Channel 2'])
            self.viewDataAcquisition.setEdtTimeText(self.values['Time'])

            # self.viewDataAcquisition.setDataChannel1(self.values['Time'], self.values['Channel 1'])
            # self.viewDataAcquisition.setDataChannel2(self.values['Time'], self.values['Channel 2'])

            valueX1 = self.values['Channel 1'] - self.valuesExperiment['Channel 1'][0]
            valueX2 = self.values['Channel 2'] - self.valuesExperiment['Channel 2'][0]

            self.viewDataAcquisition.setDataChannel(self.values['Time'], valueX1, valueX2)

            self.values['Time'] += 1

            if self.viewDataAcquisition.getBtnAutoscaleYStatus():
                if self.values['Channel 1'] > self.axisYMax:
                    self.axisYMax = self.values['Channel 1']

                if self.values['Channel 1'] < self.axisYMin:
                    self.axisYMin = self.values['Channel 1']

                autoscale = True

                self.viewDataAcquisition.setRangeY([self.axisYMin, self.axisYMax], autoscale)

            # if self.viewDataAcquisition.getBtnAutoscaleYChannel1Status():
            #     if self.values['Channel 1'] > self.axisYMaxChannel1:
            #         self.axisYMaxChannel1 = self.values['Channel 1']
            #
            #     if self.values['Channel 1'] < self.axisYMinChannel1:
            #         self.axisYMinChannel1 = self.values['Channel 1']
            #
            #     autoscale = True
            #
            #     self.viewDataAcquisition.setRangeYChannel1([self.axisYMinChannel1, self.axisYMaxChannel1], autoscale)
            #
            # if self.viewDataAcquisition.getBtnAutoscaleYChannel2Status():
            #     if self.values['Channel 2'] > self.axisYMaxChannel2:
            #         self.axisYMaxChannel2 = self.values['Channel 2']
            #
            #     if self.values['Channel 2'] < self.axisYMinChannel2:
            #         self.axisYMinChannel2 = self.values['Channel 2']
            #
            #     autoscale = True
            #
            #     self.viewDataAcquisition.setRangeYChannel2([self.axisYMinChannel2, self.axisYMaxChannel2], autoscale)

            if not self.viewDataAcquisition.getBtnLaserStatus():
                self.viewDataAcquisition.setMessageCritical(Strings.messageNecessaryLaserON)

            if not self.viewDataAcquisition.getBtnPeristalticStatus():
                self.viewDataAcquisition.setMessageCritical(Strings.messageNecessaryPeristalticON)

    """
    ********************************************************************************************************************
    *                                         End Init Experiment Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                           Experiment Time Functions                                              *
    ********************************************************************************************************************
    """

    def edtExperimentTimeChanged(self):
        self.values['Experiment Time'] = self.viewDataAcquisition.getEdtExperimentTimeValue()

    """
    ********************************************************************************************************************
    *                                         End Experiment Time Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                Save File Functions                                               *
    ********************************************************************************************************************
    """

    def autoSaveFileMeasure(self):
        if self.fileNameMeasure is not None:
            self.myFileMeasure = open(self.fileNameMeasure, Strings.write)

            myData = [[Strings.timeUC, Strings.channel1UC, Strings.channel2UC]]

            for i in range(0, len(self.valuesExperiment['Channel 1'])):
                myData.append([self.valuesExperiment['Time'][i], self.valuesExperiment['Channel 1'][i],
                               self.valuesExperiment['Channel 2'][i]])

            with self.myFileMeasure:
                writer = csv.writer(self.myFileMeasure, delimiter='\t')
                writer.writerows(myData)

        else:
            if self.viewDataAcquisition.setMessageQuestion(Strings.messageSaveData):
                self.btnSaveFileMeasureChanged()

            else:
                pass

    def btnSaveFileMeasureChanged(self):

        self.myFileNameMeasure = self.viewDataAcquisition.getEdtSaveFileText()

        self.fileNameMeasure = self.viewDataAcquisition.setDialogSaveFile(self.myFileNameMeasure)

        if self.fileNameMeasure != '':
            self.myFileMeasure = open(self.fileNameMeasure, Strings.write)

            if len(self.valuesExperiment['Channel 1']) > 0:

                myData = [[Strings.timeUC, Strings.channel1UC, Strings.channel2UC]]

                for i in range(0, len(self.valuesExperiment['Channel 1'])):
                    myData.append([self.valuesExperiment['Time'][i], self.valuesExperiment['Channel 1'][i],
                                   self.valuesExperiment['Channel 2'][i]])

                with self.myFileMeasure:
                    writer = csv.writer(self.myFileMeasure, delimiter='\t')
                    writer.writerows(myData)

        else:
            pass

    """
    ********************************************************************************************************************
    *                                              End Save File Functions                                             *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                           Chart Experiment Functions                                             *
    ********************************************************************************************************************
    """

    def btnAutoscaleYChanged(self):
        if self.viewDataAcquisition.getBtnAutoscaleYStatus():

            if len(self.valuesExperiment['Channel 1']) > 100:
                init = len(self.valuesExperiment['Channel 1']) - 100

            else:
                init = 0

            if len(self.valuesExperiment['Channel 1']) > 0:
                self.axisYMin = min(self.valuesExperiment['Channel 1'][init], self.valuesExperiment['Channel 2'][init])
                self.axisYMax = max(self.valuesExperiment['Channel 1'][init], self.valuesExperiment['Channel 2'][init])

                for i in range(init, len(self.valuesExperiment['Channel 1'])):

                    if self.valuesExperiment['Channel 1'][i] > self.axisYMax:
                        self.axisYMax = self.valuesExperiment['Channel 1'][i]

                    if self.valuesExperiment['Channel 2'][i] > self.axisYMax:
                        self.axisYMax = self.valuesExperiment['Channel 2'][i]

                    if self.valuesExperiment['Channel 1'][i] < self.axisYMin:
                        self.axisYMin = self.valuesExperiment['Channel 1'][i]

                    if self.valuesExperiment['Channel 2'][i] < self.axisYMin:
                        self.axisYMin = self.valuesExperiment['Channel 1'][i]

            else:
                self.axisYMin = 0
                self.axisYMax = 0

            autoscale = True

        else:
            self.axisYMin = 0
            self.axisYMax = 100

            autoscale = False

        self.viewDataAcquisition.setRangeY([self.axisYMin, self.axisYMax], autoscale)

    def btnAutoscaleXChanged(self):
        if self.viewDataAcquisition.getBtnAutoscaleXStatus():

            self.viewDataAcquisition.setBtnChart1000Status(False)
            self.viewDataAcquisition.setBtnChart10000Status(False)

            rangeX = self.viewDataAcquisition.getRangeX()
            rangeX[0] = 0

            if self.values['Time'] is not 0:
                rangeX[1] = self.values['Time']

            else:
                rangeX[1] = 100

            self.viewDataAcquisition.setRangeX(rangeX)

    def btnChart1000Changed(self):
        if self.viewDataAcquisition.getBtnChart1000Status():

            self.viewDataAcquisition.setBtnAutoscaleXStatus(False)
            self.viewDataAcquisition.setBtnChart10000Status(False)

            rangeX = self.viewDataAcquisition.getRangeX()

            if self.values['Time'] > 1000:
                rangeX[0] = self.values['Time'] - 1000

            else:
                rangeX[1] = 1000

            self.viewDataAcquisition.setRangeX(rangeX)

        else:
            if not self.viewDataAcquisition.getBtnAutoscaleYStatus()\
                    and not self.viewDataAcquisition.getBtnChart10000Status():

                self.viewDataAcquisition.setBtnAutoscaleXStatus(True)
                self.btnAutoscaleXChanged()

    def btnChart10000Changed(self):
        if self.viewDataAcquisition.getBtnChart10000Status():

            self.viewDataAcquisition.setBtnAutoscaleXStatus(False)
            self.viewDataAcquisition.setBtnChart1000Status(False)

            rangeX = self.viewDataAcquisition.getRangeX()

            if rangeX[1] > 10000:
                rangeX[0] = rangeX[1] - 10000

            else:
                rangeX[1] = 10000

            self.viewDataAcquisition.setRangeX(rangeX)

        else:
            if not self.viewDataAcquisition.getBtnAutoscaleYStatus()\
                    and not self.viewDataAcquisition.getBtnChart1000Status():

                self.viewDataAcquisition.setBtnAutoscaleXStatus(True)
                self.btnAutoscaleXChanged()

    # def btnAutoscaleYChannel1Changed(self):
    #     if self.viewDataAcquisition.getBtnAutoscaleYChannel1Status():
    #
    #         if len(self.valuesExperiment['Channel 1']) > 100:
    #             initChannel1 = len(self.valuesExperiment['Channel 1']) - 100
    #
    #         else:
    #             initChannel1 = 0
    #
    #         if len(self.valuesExperiment['Channel 1']) > 0:
    #             self.axisYMinChannel1 = self.valuesExperiment['Channel 1'][initChannel1]
    #             self.axisYMaxChannel1 = self.valuesExperiment['Channel 1'][initChannel1]
    #
    #             for i in range(initChannel1, len(self.valuesExperiment['Channel 1'])):
    #
    #                 if self.valuesExperiment['Channel 1'][i] > self.axisYMaxChannel1:
    #                     self.axisYMaxChannel1 = self.valuesExperiment['Channel 1'][i]
    #
    #                 if self.valuesExperiment['Channel 1'][i] < self.axisYMinChannel1:
    #                     self.axisYMinChannel1 = self.valuesExperiment['Channel 1'][i]
    #
    #         else:
    #             self.axisYMinChannel1 = 0
    #             self.axisYMaxChannel1 = 0
    #
    #         autoscale = True
    #
    #     else:
    #         self.axisYMinChannel1 = 0
    #         self.axisYMaxChannel1 = 100
    #
    #         autoscale = False
    #
    #     self.viewDataAcquisition.setRangeYChannel1([self.axisYMinChannel1, self.axisYMaxChannel1], autoscale)
    #
    # def btnAutoscaleXChannel1Changed(self):
    #     if self.viewDataAcquisition.getBtnAutoscaleXChannel1Status():
    #
    #         self.viewDataAcquisition.setBtnChart1000Channel1Status(False)
    #         self.viewDataAcquisition.setBtnChart10000Channel1Status(False)
    #
    #         rangeXChannel1 = self.viewDataAcquisition.getRangeXChannel1()
    #         rangeXChannel1[0] = 0
    #
    #         if self.values['Time'] is not 0:
    #             rangeXChannel1[1] = self.values['Time']
    #
    #         else:
    #             rangeXChannel1[1] = 100
    #
    #         self.viewDataAcquisition.setRangeXChannel1(rangeXChannel1)
    #
    # def btnChart1000Channel1Changed(self):
    #     if self.viewDataAcquisition.getBtnChart1000Channel1Status():
    #
    #         self.viewDataAcquisition.setBtnAutoscaleXChannel1Status(False)
    #         self.viewDataAcquisition.setBtnChart10000Channel1Status(False)
    #
    #         rangeXChannel1 = self.viewDataAcquisition.getRangeXChannel1()
    #
    #         if self.values['Time'] > 1000:
    #             rangeXChannel1[0] = self.values['Time'] - 1000
    #
    #         else:
    #             rangeXChannel1[1] = 1000
    #
    #         self.viewDataAcquisition.setRangeXChannel1(rangeXChannel1)
    #
    #     else:
    #         if not self.viewDataAcquisition.getBtnAutoscaleYChannel1Status()\
    #                 and not self.viewDataAcquisition.getBtnChart10000Channel1Status():
    #
    #             self.viewDataAcquisition.setBtnAutoscaleXChannel1Status(True)
    #             self.btnAutoscaleXChannel1Changed()
    #
    # def btnChart10000Channel1Changed(self):
    #     if self.viewDataAcquisition.getBtnChart10000Channel1Status():
    #
    #         self.viewDataAcquisition.setBtnAutoscaleXChannel1Status(False)
    #         self.viewDataAcquisition.setBtnChart1000Channel1Status(False)
    #
    #         rangeXChannel1 = self.viewDataAcquisition.getRangeXChannel1()
    #
    #         if rangeXChannel1[1] > 10000:
    #             rangeXChannel1[0] = rangeXChannel1[1] - 10000
    #
    #         else:
    #             rangeXChannel1[1] = 10000
    #
    #         self.viewDataAcquisition.setRangeXChannel1(rangeXChannel1)
    #
    #     else:
    #         if not self.viewDataAcquisition.getBtnAutoscaleYChannel1Status()\
    #                 and not self.viewDataAcquisition.getBtnChart1000Channel1Status():
    #
    #             self.viewDataAcquisition.setBtnAutoscaleXChannel1Status(True)
    #             self.btnAutoscaleXChannel1Changed()
    #
    # def btnAutoscaleYChannel2Changed(self):
    #     if self.viewDataAcquisition.getBtnAutoscaleYChannel2Status():
    #
    #         if len(self.valuesExperiment['Channel 2']) > 100:
    #             initChannel2 = len(self.valuesExperiment['Channel 2']) - 100
    #
    #         else:
    #             initChannel2 = 0
    #
    #         if len(self.valuesExperiment['Channel 2']) > 0:
    #             self.axisYMinChannel2 = self.valuesExperiment['Channel 2'][initChannel2]
    #             self.axisYMaxChannel2 = self.valuesExperiment['Channel 2'][initChannel2]
    #
    #             for i in range(initChannel2, len(self.valuesExperiment['Channel 2'])):
    #
    #                 if self.valuesExperiment['Channel 2'][i] > self.axisYMaxChannel2:
    #                     self.axisYMaxChannel2 = self.valuesExperiment['Channel 2'][i]
    #
    #                 if self.valuesExperiment['Channel 2'][i] < self.axisYMinChannel2:
    #                     self.axisYMinChannel2 = self.valuesExperiment['Channel 2'][i]
    #
    #         else:
    #             self.axisYMinChannel2 = 0
    #             self.axisYMaxChannel2 = 0
    #
    #         autoscale = True
    #
    #     else:
    #         self.axisYMinChannel2 = 0
    #         self.axisYMaxChannel2 = 100
    #
    #         autoscale = False
    #
    #     self.viewDataAcquisition.setRangeYChannel2([self.axisYMinChannel2, self.axisYMaxChannel2], autoscale)
    #
    # def btnAutoscaleXChannel2Changed(self):
    #     if self.viewDataAcquisition.getBtnAutoscaleXChannel2Status():
    #
    #         self.viewDataAcquisition.setBtnChart1000Channel2Status(False)
    #         self.viewDataAcquisition.setBtnChart10000Channel2Status(False)
    #
    #         rangeXChannel2 = self.viewDataAcquisition.getRangeXChannel2()
    #         rangeXChannel2[0] = 0
    #
    #         if self.values['Time'] is not 0:
    #             rangeXChannel2[1] = self.values['Time']
    #
    #         else:
    #             rangeXChannel2[1] = 100
    #
    #         self.viewDataAcquisition.setRangeXChannel2(rangeXChannel2)
    #
    # def btnChart1000Channel2Changed(self):
    #     if self.viewDataAcquisition.getBtnChart1000Channel2Status():
    #
    #         self.viewDataAcquisition.setBtnAutoscaleXChannel2Status(False)
    #         self.viewDataAcquisition.setBtnChart10000Channel2Status(False)
    #
    #         rangeXChannel2 = self.viewDataAcquisition.getRangeXChannel2()
    #
    #         if self.values['Time'] > 1000:
    #             rangeXChannel2[0] = self.values['Time'] - 1000
    #
    #         else:
    #             rangeXChannel2[1] = 1000
    #
    #         self.viewDataAcquisition.setRangeXChannel2(rangeXChannel2)
    #
    #     else:
    #         if not self.viewDataAcquisition.getBtnAutoscaleYChannel2Status()\
    #                 and not self.viewDataAcquisition.getBtnChart10000Channel2Status():
    #
    #             self.viewDataAcquisition.setBtnAutoscaleXChannel2Status(True)
    #             self.btnAutoscaleXChannel2Changed()
    #
    # def btnChart10000Channel2Changed(self):
    #     if self.viewDataAcquisition.getBtnChart10000Channel2Status():
    #
    #         self.viewDataAcquisition.setBtnAutoscaleXChannel2Status(False)
    #         self.viewDataAcquisition.setBtnChart1000Channel2Status(False)
    #
    #         rangeXChannel2 = self.viewDataAcquisition.getRangeXChannel2()
    #
    #         if rangeXChannel2[1] > 10000:
    #             rangeXChannel2[0] = rangeXChannel2[1] - 10000
    #
    #         else:
    #             rangeXChannel2[1] = 10000
    #
    #         self.viewDataAcquisition.setRangeXChannel2(rangeXChannel2)
    #
    #     else:
    #         if not self.viewDataAcquisition.getBtnAutoscaleYChannel2Status()\
    #                 and not self.viewDataAcquisition.getBtnChart1000Channel2Status():
    #
    #             self.viewDataAcquisition.setBtnAutoscaleXChannel2Status(True)
    #             self.btnAutoscaleXChannel2Changed()

    """
    ********************************************************************************************************************
    *                                         End Chart Experiment Functions                                           *
    ********************************************************************************************************************
    """

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
            if value == Strings.ackCommand:
                valueACK = self.bufferWaitACK.pop()

                if valueACK != -1:
                    self.tmrTimeout.stop()
                    self.tmrTimeout.timeout.disconnect()
                    valueACK()

            else:
                if value == Strings.acquisitionCommand:
                    self.acquisitionDataReceived(data)

                elif value == Strings.experimentCommand:
                    self.experimentDataReceived(data)

    def setTimeout(self, messageTimeout, functionTimeout):
        self.btnTimeout = True
        self.viewSystemControl.setMessageCritical(messageTimeout)
        functionTimeout()

        self.tmrTimeout.stop()
        self.tmrTimeout.timeout.disconnect()

    @staticmethod
    def setBeep():
        winsound.Beep(800, 500)

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
