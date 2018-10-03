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

from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QSpinBox, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from lib.TriangleButton import TriangleButton
from lib.RectangleButton import RectangleButton
from lib.Chart import Chart
from lib import Strings
from lib import Styles
import getpass


class ViewDataAcquisition(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        """---------------------------------------------- QPushButtons ----------------------------------------------"""
        self.btnInitExperiment = QPushButton()
        self.btnLaser = QPushButton(Strings.laserStart)
        self.btnFreeRunning = QPushButton(Strings.freeRunning)
        self.btnPeristaltic = QPushButton(Strings.start)
        self.btnInject_A = QPushButton(Strings.inject)
        self.btnInject_B = QPushButton(Strings.inject)
        self.btnPurge_A = QPushButton(Strings.purge)
        self.btnPurge_B = QPushButton(Strings.purge)
        self.btnBackPeristaltic = TriangleButton(40, Strings.backLC)
        self.btnForwardPeristaltic = TriangleButton(40, Strings.forwardLC)
        self.btnStopPeristaltic = RectangleButton(40)
        self.btnChart1000Channel = QPushButton(Strings.x1000)
        self.btnChart10000Channel = QPushButton(Strings.x10000)
        self.btnAutoscaleXChannel = QPushButton(Strings.autoscaleX)
        self.btnAutoscaleYChannel = QPushButton(Strings.autoscaleY)
        # self.btnChart1000Channel1 = QPushButton(Strings.x1000)
        # self.btnChart10000Channel1 = QPushButton(Strings.x10000)
        # self.btnAutoscaleXChannel1 = QPushButton(Strings.autoscaleX)
        # self.btnAutoscaleYChannel1 = QPushButton(Strings.autoscaleY)
        # self.btnChart1000Channel2 = QPushButton(Strings.x1000)
        # self.btnChart10000Channel2 = QPushButton(Strings.x10000)
        # self.btnAutoscaleXChannel2 = QPushButton(Strings.autoscaleX)
        # self.btnAutoscaleYChannel2 = QPushButton(Strings.autoscaleY)
        self.btnSaveFile = QPushButton(Strings.saveFileUC)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QLabels -------------------------------------------------"""
        self.lblImageLogo = QLabel(self)
        self.lblDataSampling = QLabel(Strings.dataSampling)
        self.lblExperimentTime = QLabel(Strings.experimentTime)
        self.lblChannel_1 = QLabel(Strings.channel1LC)
        self.lblChannel_2 = QLabel(Strings.channel2LC)
        self.lblTime = QLabel(Strings.timeLC)
        self.lblBtnInit = QLabel(Strings.startExperiment)
        self.lblPeristaltic = QLabel(Strings.flowPeristaltic)
        self.lblImpulsional_A = QLabel(Strings.injectionA)
        self.lblImpulsional_B = QLabel(Strings.injectionB)
        self.lblBack = QLabel(Strings.backUC)
        self.lblForward = QLabel(Strings.forwardUC)
        self.lblStop = QLabel(Strings.stop)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QLineEdit -----------------------------------------------"""
        self.edtChannel_1 = QLineEdit()
        self.edtChannel_2 = QLineEdit()
        self.edtTime = QLineEdit()
        self.edtSaveFile = QLineEdit()
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QSpinBox ------------------------------------------------"""
        self.edtDataSampling = QSpinBox()
        self.edtExperimentTime = QSpinBox()
        self.edtPeristaltic = QSpinBox()
        self.edtImpulsional_A = QSpinBox()
        self.edtImpulsional_B = QSpinBox()
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QPixmap -------------------------------------------------"""
        self.imageLogo = QPixmap(Strings.imageLogoFull)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------- Charts -------------------------------------------------"""
        # self.myChartChannel1 = Chart(Strings.channel1UC)
        # self.myChartChannel2 = Chart(Strings.channel2UC)

        self.myChartChannel = Chart()
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGroupBoxes -----------------------------------------------"""
        self.timeBoxLayout = QGroupBox(Strings.timeParameters)
        self.dataSamplingBoxLayout = QGroupBox()
        self.experimentTimeBoxLayout = QGroupBox()
        self.fluidicBoxLayout = QGroupBox(Strings.fluidicParameters)
        self.peristalticControlBoxLayout = QGroupBox(Strings.peristalticPumpControl)
        self.injectControlBoxLayout = QGroupBox(Strings.injectionPumpControl)
        self.peristalticBoxLayout = QGroupBox()
        self.saveFileBoxLayout = QGroupBox(Strings.saveFileLC)
        self.imageBoxLayout = QGroupBox()
        self.chartBoxLayout = QGroupBox()
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGridLayouts ----------------------------------------------"""
        self.layoutGrid = QGridLayout(self)
        self.timeLayout = QGridLayout(self)
        self.dataSamplingLayout = QGridLayout(self)
        self.experimentTimeLayout = QGridLayout(self)
        self.fluidicLayout = QGridLayout(self)
        self.peristalticControlLayout = QGridLayout(self)
        self.injectControlLayout = QGridLayout(self)
        self.peristalticLayout = QGridLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QVBoxLayouts ----------------------------------------------"""
        self.btnInitLayout = QVBoxLayout(self)
        self.saveFileLayout = QVBoxLayout(self)
        self.imageLayout = QVBoxLayout(self)
        self.chartLayout = QVBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QHBoxLayouts ----------------------------------------------"""
        # self.btnChartLayoutChannel1 = QHBoxLayout(self)
        # self.btnChartLayoutChannel2 = QHBoxLayout(self)

        self.btnChartLayoutChannel = QHBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """--------------------------------------------- Style Functions --------------------------------------------"""
        self.setStyleButtons()
        self.setStyleSpinBox()
        self.setStyleLineEdit()
        self.setStyleLabels()
        self.setStyleRectangleButton()
        self.setStyleTriangleButton()
        self.setStylePixmap()
        self.setStyleGroupBox()
        self.setStyleLayouts()
        """----------------------------------------------------------------------------------------------------------"""

    def mainWindow(self):
        """Add the main widgets to the main layout.

        Add the group box to the layout of the app.
        """
        self.layoutGrid.addWidget(self.setTimeGroup(), 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.setFluidicGroup(), 1, 0, 1, 2)
        self.layoutGrid.addWidget(self.setSaveFileGroup(), 2, 0, 1, 2)
        self.layoutGrid.addWidget(self.setImageGroup(), 3, 0, 1, 2)
        self.layoutGrid.addWidget(self.setChartGroup(), 0, 2, 4, 8)

    def setTimeGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.btnInitLayout.addWidget(self.lblBtnInit)

        self.btnInitExperiment.setLayout(self.btnInitLayout)

        self.dataSamplingLayout.addWidget(self.lblDataSampling, 0, 0)
        self.dataSamplingLayout.addWidget(self.edtDataSampling, 0, 1)

        self.dataSamplingBoxLayout.setLayout(self.dataSamplingLayout)

        self.experimentTimeLayout.addWidget(self.lblExperimentTime, 0, 1)
        self.experimentTimeLayout.addWidget(self.edtExperimentTime, 0, 2)
        self.experimentTimeLayout.addWidget(self.btnFreeRunning, 1, 0, 1, 3)

        self.experimentTimeBoxLayout.setLayout(self.experimentTimeLayout)

        self.timeLayout.addWidget(self.btnInitExperiment, 0, 0, 5, 1)
        self.timeLayout.addWidget(self.dataSamplingBoxLayout, 0, 1, 1, 3)
        self.timeLayout.addWidget(self.experimentTimeBoxLayout, 1, 1, 1, 3)
        self.timeLayout.addWidget(self.btnLaser, 2, 1, 3, 1)
        self.timeLayout.addWidget(self.lblChannel_1, 2, 2)
        self.timeLayout.addWidget(self.edtChannel_1, 2, 3)
        self.timeLayout.addWidget(self.lblChannel_2, 3, 2)
        self.timeLayout.addWidget(self.edtChannel_2, 3, 3)
        self.timeLayout.addWidget(self.lblTime, 4, 2)
        self.timeLayout.addWidget(self.edtTime, 4, 3)

        self.timeBoxLayout.setLayout(self.timeLayout)

        return self.timeBoxLayout

    def setFluidicGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.peristalticControlLayout.addWidget(self.lblPeristaltic, 0, 0)
        self.peristalticControlLayout.addWidget(self.edtPeristaltic, 1, 0)
        self.peristalticControlLayout.addWidget(self.btnPeristaltic, 0, 1, 2, 1)

        self.peristalticLayout.addWidget(self.btnBackPeristaltic, 0, 0)
        self.peristalticLayout.addWidget(self.btnStopPeristaltic, 0, 1)
        self.peristalticLayout.addWidget(self.btnForwardPeristaltic, 0, 2)
        self.peristalticLayout.addWidget(self.lblBack, 1, 0)
        self.peristalticLayout.addWidget(self.lblStop, 1, 1)
        self.peristalticLayout.addWidget(self.lblForward, 1, 2)

        self.peristalticBoxLayout.setLayout(self.peristalticLayout)

        self.peristalticControlLayout.addWidget(self.peristalticBoxLayout, 2, 0, 1, 3)

        self.peristalticControlBoxLayout.setLayout(self.peristalticControlLayout)

        self.injectControlLayout.addWidget(self.lblImpulsional_A, 0, 0)
        self.injectControlLayout.addWidget(self.lblImpulsional_B, 0, 1)
        self.injectControlLayout.addWidget(self.edtImpulsional_A, 1, 0)
        self.injectControlLayout.addWidget(self.edtImpulsional_B, 1, 1)
        self.injectControlLayout.addWidget(self.btnInject_A, 2, 0)
        self.injectControlLayout.addWidget(self.btnInject_B, 2, 1)
        self.injectControlLayout.addWidget(self.btnPurge_A, 3, 0)
        self.injectControlLayout.addWidget(self.btnPurge_B, 3, 1)

        self.injectControlBoxLayout.setLayout(self.injectControlLayout)

        self.fluidicLayout.addWidget(self.peristalticControlBoxLayout, 0, 0, 2, 1)
        self.fluidicLayout.addWidget(self.injectControlBoxLayout, 0, 1, 1, 1)

        self.fluidicBoxLayout.setLayout(self.fluidicLayout)

        return self.fluidicBoxLayout

    def setSaveFileGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.saveFileLayout.addWidget(self.edtSaveFile)
        self.saveFileLayout.addWidget(self.btnSaveFile)

        self.saveFileBoxLayout.setLayout(self.saveFileLayout)

        return self.saveFileBoxLayout

    def setImageGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.lblImageLogo.setPixmap(self.imageLogo)

        self.imageLayout.addWidget(self.lblImageLogo)

        self.imageBoxLayout.setLayout(self.imageLayout)

        return self.imageBoxLayout

    def setChartGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.myChartChannel.setAddSerie('CHANNEL 1', '#FF9933')
        self.myChartChannel.setAddSerie('CHANNEL 2', '#33CCFF')

        self.btnChartLayoutChannel.addWidget(self.btnAutoscaleYChannel)
        self.btnChartLayoutChannel.addWidget(self.btnAutoscaleXChannel)
        self.btnChartLayoutChannel.addWidget(self.btnChart1000Channel)
        self.btnChartLayoutChannel.addWidget(self.btnChart10000Channel)

        # self.btnChartLayoutChannel1.addWidget(self.btnAutoscaleYChannel1)
        # self.btnChartLayoutChannel1.addWidget(self.btnAutoscaleXChannel1)
        # self.btnChartLayoutChannel1.addWidget(self.btnChart1000Channel1)
        # self.btnChartLayoutChannel1.addWidget(self.btnChart10000Channel1)

        # self.btnChartLayoutChannel2.addWidget(self.btnAutoscaleYChannel2)
        # self.btnChartLayoutChannel2.addWidget(self.btnAutoscaleXChannel2)
        # self.btnChartLayoutChannel2.addWidget(self.btnChart1000Channel2)
        # self.btnChartLayoutChannel2.addWidget(self.btnChart10000Channel2)

        # self.chartLayout.addLayout(self.btnChartLayoutChannel1)
        # self.chartLayout.addWidget(self.myChartChannel1)

        # self.chartLayout.addLayout(self.btnChartLayoutChannel2)
        # self.chartLayout.addWidget(self.myChartChannel2)

        self.chartLayout.addLayout(self.btnChartLayoutChannel)
        self.chartLayout.addWidget(self.myChartChannel)

        self.chartBoxLayout.setLayout(self.chartLayout)

        return self.chartBoxLayout

    """
    ********************************************************************************************************************
    *                                        Init Experiment Button Functions                                          *
    ********************************************************************************************************************
    """

    def setBtnInitExperimentStatus(self, status):
        """Change the status and the text of the init experiment button.

        If status is True, the text of the button is changed to STOP, in the case that status is False, the text of the
        button is changed to START.

        Args:
            status (bool): the status of the button.
        """
        if status:
            text = Strings.stopExperiment

        else:
            text = Strings.startExperiment

        self.lblBtnInit.setText(text)
        self.btnInitExperiment.setChecked(status)

    def getBtnInitExperimentStatus(self):
        """Return the status of the init experiment button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnInitExperiment.isChecked()

    """
    ********************************************************************************************************************
    *                                      End Init Experiment Button Functions                                        *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                              Laser Button Functions                                              *
    ********************************************************************************************************************
    """

    def setBtnLaserStatus(self, status):
        if status:
            text = Strings.laserStop

        else:
            text = Strings.laserStart

        self.btnLaser.setText(text)
        self.btnLaser.setChecked(status)

    def getBtnLaserStatus(self):
        return self.btnLaser.isChecked()

    def setBtnLaserDisable(self, disable):
        self.btnLaser.setDisabled(disable)

    """
    ********************************************************************************************************************
    *                                            End Laser Button Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Experiment Time Functions                                            *
    ********************************************************************************************************************
    """

    def setEdtExperimentTimeValue(self, value):
        self.edtExperimentTime.setValue(value)

    def getEdtExperimentTimeValue(self):
        return self.edtExperimentTime.value()

    """
    ********************************************************************************************************************
    *                                           End Experiment Time Functions                                          *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Acquisition Values Functions                                            *
    ********************************************************************************************************************
    """

    def setEdtChannel1Text(self, text):
        """Change the text of the channel 1 line edit.

        Convert text (float) to float with 3 decimals and to string and, then, the value of the line edit is updated.

        Args:
            text (float): the value to update the channel 1 line edit.
        """
        text = str('{0:.3f}'.format(text))
        self.edtChannel_1.setText(text)

    def getEdtChannel1Text(self):
        """Return the text of the channel 1 line edit.

        Convert the text (string) of the line edit to float.

        Returns:
            float: the value of the channel 1.
        """
        return float(self.edtChannel_1.text())

    def setEdtChannel2Text(self, text):
        """Change the text of the channel 2 line edit.

        Convert text (float) to float with 3 decimals and to string and, then, the value of the line edit is updated.

        Args:
            text (float): the value to update the channel 2 line edit.
        """
        text = str('{0:.3f}'.format(text))
        self.edtChannel_2.setText(text)

    def getEdtChannel2Text(self):
        """Return the text of the channel 2 line edit.

        Convert the text (string) of the line edit to float.

        Returns:
            float: the value of the channel 2.
        """
        return float(self.edtChannel_2.text())

    def setEdtTimeText(self, text):
        """Change the text of the time line edit.

        Convert text (int) to string and add the unit (seconds), then, the value of the line edit is updated.

        Args:
            text (int): the value to update the time line edit.
        """
        self.edtTime.setText(str(text) + Strings.unitTime)

    def getEdtTimeText(self):
        """Return the text of the time line edit.

        Remove the unit (s, seconds) of the string and convert the text (string) of the line edit to int.

        Returns:
            int: the value of the time.
        """
        text = self.edtTime.text().replace(Strings.unitTime, '')
        return int(text)

    """
    ********************************************************************************************************************
    *                                        End Acquisition Values Functions                                          *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Peristaltic Control Functions                                           *
    ********************************************************************************************************************
    """

    def setBtnPeristalticStatus(self, status):
        """Change the status and the text of the peristaltic button.

        If status is True, the text of the button is changed to STOP, in the case that status is False, the text of
        the button is changed to START.

        Args:
            status (bool): the status of the button.
        """
        if status:
            text = Strings.stop

        else:
            text = Strings.start

        self.btnPeristaltic.setText(text)
        self.btnPeristaltic.setChecked(status)

    def getBtnPeristalticStatus(self):
        """Return the status of the peristaltic button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnPeristaltic.isChecked()

    def setBtnPeristalticDisable(self, disable):
        """Enable or disable the peristaltic button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnPeristaltic.setDisabled(disable)

    def setBtnBackPeristalticStatus(self, status):
        """Change the status of the back peristaltic button.

        Args:
            status (bool): the status of the button.
        """
        self.btnBackPeristaltic.setChecked(status)

    def getBtnBackPeristalticStatus(self):
        """Return the status of the back peristaltic button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnBackPeristaltic.isChecked()

    def setBtnBackPeristalticDisable(self, disable):
        """Enable or disable the back peristaltic button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnBackPeristaltic.setDisabled(disable)

    def setBtnStopPeristalticStatus(self, status):
        """Change the status of the stop peristaltic button.

        Args:
            status (bool): the status of the button.
        """
        self.btnStopPeristaltic.setChecked(status)

    def getBtnStopPeristalticStatus(self):
        """Return the status of the stop peristaltic button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnStopPeristaltic.isChecked()

    def setBtnStopPeristalticDisable(self, disable):
        """Enable or disable the stop peristaltic button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnStopPeristaltic.setDisabled(disable)

    def setBtnForwardPeristalticStatus(self, status):
        """Change the status of the forward peristaltic button.

        Args:
            status (bool): the status of the button.
        """
        self.btnForwardPeristaltic.setChecked(status)

    def getBtnForwardPeristalticStatus(self):
        """Return the status of the forward peristaltic button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnForwardPeristaltic.isChecked()

    def setBtnForwardPeristalticDisable(self, disable):
        """Enable or disable the forward peristaltic button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnForwardPeristaltic.setDisabled(disable)

    def setBtnBSFPeristalticStatus(self, status, who):
        """Change the status of the back, stop and forward peristaltic buttons.

        Args:
            status (bool): the status of the button.
            who (int): what button was pressed:
                - 0: Back button
                - 1: Stop button
                - 2: Forward button
        """
        if who == 0:
            self.setBtnBackPeristalticStatus(status)

        elif who == 1:
            self.setBtnStopPeristalticStatus(status)

        else:
            self.setBtnForwardPeristalticStatus(status)

    def getBtnBSFPeristalticStatus(self, who):
        """Return the status of the back, stop and forward peristaltic buttons.

        Args:
            who (int): what button was pressed:
                - 0: Back button
                - 1: Stop button
                - 2: Forward button

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        if who == 0:
            return self.getBtnBackPeristalticStatus()

        elif who == 1:
            return self.getBtnStopPeristalticStatus()

        else:
            return self.getBtnForwardPeristalticStatus()

    def setBtnBSFPeristalticNotStatus(self, status, who):
        """Change the status of the back, stop and forward peristaltic buttons according to the button that was pressed.

        If 'who' is equal to 0 the back button was pressed and the stop and forward buttons are depressed, if 'who' is 1
        the stop button was pressed and the back and forward are depressed, finally, if 'who' is 2 the forward button
        was pressed and the back and stop buttons are depressed.

        Args:
            status (bool): the status of the button.
            who (int): what button was pressed:
                - 0: Back button
                - 1: Stop button
                - 2: Forward button
        """
        if who == 0:
            self.setBtnStopPeristalticStatus(status)
            self.setBtnForwardPeristalticStatus(status)

        elif who == 1:
            self.setBtnBackPeristalticStatus(status)
            self.setBtnForwardPeristalticStatus(status)

        else:
            self.setBtnBackPeristalticStatus(status)
            self.setBtnStopPeristalticStatus(status)

    def setBtnBSFPeristalticDisable(self, disable):
        """Enable or disable the back, stop and forward peristaltic buttons.

        Args:
            disable (bool): if the value is True, the buttons will be disabled, in the opposite case, the buttons will
            be enabled.
        """
        self.setBtnBackPeristalticDisable(disable)
        self.setBtnStopPeristalticDisable(disable)
        self.setBtnForwardPeristalticDisable(disable)

    def setEdtPeristalticValue(self, value):
        """Change the value of the peristaltic line edit.

        Args:
            value (int): the value to update the peristaltic line edit.
        """
        self.edtPeristaltic.setValue(value)

    def getEdtPeristalticValue(self):
        """Return the value of the peristaltic line edit.

        Returns:
            int: the value of the peristaltic.
        """
        return self.edtPeristaltic.value()

    """
    ********************************************************************************************************************
    *                                        End Peristaltic Control Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Impulsional A Control Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnImpulsionalAStatus(self, status):
        """Change the status of the purge A button.

        If status is True, purge A button is pressed and disabled, in the opposite case, the button is depressed and
        enable.

        Args:
            status (bool): the status of the button.
        """
        self.btnPurge_A.setChecked(status)
        self.setBtnImpulsionalADisable(status)

    def getBtnImpulsionalAStatus(self):
        """Return the status of the purge A button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnPurge_A.isChecked()

    def setBtnImpulsionalADisable(self, disable):
        """Enable or disable the purge A button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnPurge_A.setDisabled(disable)

    def setBtnInjectAStatus(self, status):
        """Change the status of the inject A button.

        If status is True, inject A button is pressed and disabled, in the opposite case, the button is depressed and
        enable.

        Args:
            status (bool): the status of the button.
        """
        self.btnInject_A.setChecked(status)
        self.setBtnInjectADisable(status)

    def getBtnInjectAStatus(self):
        """Return the status of the inject A button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnInject_A.isChecked()

    def setBtnInjectADisable(self, disable):
        """Enable or disable the inject A button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnInject_A.setDisabled(disable)

    def setEdtImpulsionalAValue(self, value):
        """Change the value of the impulsional A line edit.

        Args:
            value (int): the value to update the impulsional A line edit.
        """
        self.edtImpulsional_A.setValue(value)

    def getEdtImpulsionalAValue(self):
        """Return the value of the impulsional A line edit.

        Returns:
            int: the value of the impulsional A.
        """
        return self.edtImpulsional_A.value()

    """
    ********************************************************************************************************************
    *                                        End Impulsional A Control Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Impulsional B Control Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnImpulsionalBStatus(self, status):
        """Change the status of the purge B button.

        If status is True, purge B button is pressed and disabled, in the opposite case, the button is depressed and
        enable.

        Args:
            status (bool): the status of the button.
        """
        self.btnPurge_B.setChecked(status)
        self.setBtnImpulsionalBDisable(status)

    def getBtnImpulsionalBStatus(self):
        """Return the status of the purge B button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnPurge_B.isChecked()

    def setBtnImpulsionalBDisable(self, disable):
        """Enable or disable the purge B button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnPurge_B.setDisabled(disable)

    def setBtnInjectBStatus(self, status):
        """Change the status of the inject B button.

        If status is True, inject B button is pressed and disabled, in the opposite case, the button is depressed and
        enable.

        Args:
            status (bool): the status of the button.
        """
        self.btnInject_B.setChecked(status)
        self.setBtnInjectBDisable(status)

    def getBtnInjectBStatus(self):
        """Return the status of the inject B button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnInject_B.isChecked()

    def setBtnInjectBDisable(self, disable):
        """Enable or disable the inject B button.

        Args:
            disable (bool): if the value is True, the button will be disabled, in the opposite case, the button will be
            enabled.
        """
        self.btnInject_B.setDisabled(disable)

    def setEdtImpulsionalBValue(self, value):
        """Change the value of the impulsional B line edit.

        Args:
            value (int): the value to update the impulsional B line edit.
        """
        self.edtImpulsional_B.setValue(value)

    def getEdtImpulsionalBValue(self):
        """Return the value of the impulsional B line edit.

        Returns:
            int: the value of the impulsional B.
        """
        return self.edtImpulsional_B.value()

    """
    ********************************************************************************************************************
    *                                        End Impulsional B Control Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                               Save File Functions                                                *
    ********************************************************************************************************************
    """

    def setEdtSaveFileText(self, text):
        """Change the text of the save file line edit.

        Args:
            text (str): the text to update the save file line edit.
        """
        self.edtSaveFile.setText(text)

    def getEdtSaveFileText(self):
        """Return the text of the save file line edit.

        Returns:
            str: the text of the save file.
        """
        return self.edtSaveFile.text()

    """
    ********************************************************************************************************************
    *                                             End Save File Functions                                              *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                  Chart Functions                                                 *
    ********************************************************************************************************************
    """

    def setDataChart(self, xData, yData1, yData2):
        """Add a new data on the chart of the channel 1.

        Args:
            xData (float): the value of the X Axis.
            yData1 (float): the value of the Y Axis.
        """
        self.myChartChannel.setDataChart(xData, yData1, yData2)

    def initSeries(self):
        """Clean the serie on the chart of the channel 1."""
        self.myChartChannel.initSeries()

    def setRangeY(self, yRange, autoscale):
        """Update the range of the Y axis on the chart of the channel 1.

        Args:
            yRange (list): the beginning and end of the Y axis.
            autoscale (bool): if the autoscale button is activated.
        """
        self.myChartChannel.setRangeY(yRange, autoscale)

    def setRangeX(self, xRange):
        """Update the range of the X axis on the chart of the channel 1.

        Args:
            xRange (list): the beginning and end of the X axis.
        """
        self.myChartChannel.setRangeX(xRange)

    def getRangeX(self):
        """Return the range of the X axis of the channel 1.

        Returns:
            list: the beginning and end of the X axis.
        """
        return self.myChartChannel.getRangeX()

    def setBtnAutoscaleYStatus(self, status):
        """Change the status of the autoscale Y channel 1 button.

        Args:
            status (bool): the status of the button.
        """
        self.btnAutoscaleYChannel.setChecked(status)

    def getBtnAutoscaleYStatus(self):
        """Return the status of the autoscale Y channel 1 button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnAutoscaleYChannel.isChecked()

    def setBtnAutoscaleXStatus(self, status):
        """Change the status of the autoscale X channel 1 button.

        Args:
            status (bool): the status of the button.
        """
        self.btnAutoscaleXChannel.setChecked(status)

    def getBtnAutoscaleXStatus(self):
        """Return the status of the autoscale X channel 1 button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnAutoscaleXChannel.isChecked()

    def setBtnChart1000Status(self, status):
        """Change the status of the x1000 channel 1 button.

        Args:
            status (bool): the status of the button.
        """
        self.btnChart1000Channel.setChecked(status)

    def getBtnChart1000Status(self):
        """Return the status of the x1000 channel 1 button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnChart1000Channel.isChecked()

    def setBtnChart10000Status(self, status):
        """Change the status of the x10000 channel 1 button.

        Args:
            status (bool): the status of the button.
        """
        self.btnChart10000Channel.setChecked(status)

    def getBtnChart10000Status(self):
        """Return the status of the x10000 channel 1 button.

        Returns:
            bool: the status of the button, if the button is pressed or depressed.
        """
        return self.btnChart10000Channel.isChecked()

    # def setDataChannel1(self, xData, yData):
    #     """Add a new data on the chart of the channel 1.
    #
    #     Args:
    #         xData (float): the value of the X Axis.
    #         yData (float): the value of the Y Axis.
    #     """
    #     self.myChartChannel1.setDataChart(xData, yData)
    #
    # def setDataChannel2(self, xData, yData):
    #     """Add a new data on the chart of the channel 2.
    #
    #     Args:
    #         xData (float): the value of the X Axis.
    #         yData (float): the value of the Y Axis.
    #     """
    #     self.myChartChannel2.setDataChart(xData, yData)

    # def setRangeYChannel1(self, yRange, autoscale):
    #     """Update the range of the Y axis on the chart of the channel 1.
    #
    #     Args:
    #         yRange (list): the beginning and end of the Y axis.
    #         autoscale (bool): if the autoscale button is activated.
    #     """
    #     self.myChartChannel1.setRangeY(yRange, autoscale)
    #
    # def setRangeXChannel1(self, xRange):
    #     """Update the range of the X axis on the chart of the channel 1.
    #
    #     Args:
    #         xRange (list): the beginning and end of the X axis.
    #     """
    #     self.myChartChannel1.setRangeX(xRange)
    #
    # def getRangeXChannel1(self):
    #     """Return the range of the X axis of the channel 1.
    #
    #     Returns:
    #         list: the beginning and end of the X axis.
    #     """
    #     return self.myChartChannel1.getRangeX()
    #
    # def setRangeYChannel2(self, yRange, autoscale):
    #     """Update the range of the Y axis on the chart of the channel 2.
    #
    #     Args:
    #         yRange (list): the beginning and end of the Y axis.
    #         autoscale (bool): if the autoscale button is activated.
    #     """
    #     self.myChartChannel2.setRangeY(yRange, autoscale)
    #
    # def setRangeXChannel2(self, xRange):
    #     """Update the range of the X axis on the chart of the channel 2.
    #
    #     Args:
    #         xRange (list): the beginning and end of the X axis.
    #     """
    #     self.myChartChannel2.setRangeX(xRange)
    #
    # def getRangeXChannel2(self):
    #     """Return the range of the X axis of the channel 2.
    #
    #     Returns:
    #         list: the beginning and end of the X axis.
    #     """
    #     return self.myChartChannel2.getRangeX()

    # def initSerieChannel1(self):
    #     """Clean the serie on the chart of the channel 1."""
    #     self.myChartChannel1.initSerie()
    #
    # def initSerieChannel2(self):
    #     """Clean the serie on the chart of the channel 2."""
    #     self.myChartChannel2.initSerie()

    # def setBtnAutoscaleYChannel1Status(self, status):
    #     """Change the status of the autoscale Y channel 1 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnAutoscaleYChannel1.setChecked(status)
    #
    # def getBtnAutoscaleYChannel1Status(self):
    #     """Return the status of the autoscale Y channel 1 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnAutoscaleYChannel1.isChecked()
    #
    # def setBtnAutoscaleXChannel1Status(self, status):
    #     """Change the status of the autoscale X channel 1 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnAutoscaleXChannel1.setChecked(status)
    #
    # def getBtnAutoscaleXChannel1Status(self):
    #     """Return the status of the autoscale X channel 1 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnAutoscaleXChannel1.isChecked()
    #
    # def setBtnChart1000Channel1Status(self, status):
    #     """Change the status of the x1000 channel 1 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnChart1000Channel1.setChecked(status)
    #
    # def getBtnChart1000Channel1Status(self):
    #     """Return the status of the x1000 channel 1 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnChart1000Channel1.isChecked()
    #
    # def setBtnChart10000Channel1Status(self, status):
    #     """Change the status of the x10000 channel 1 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnChart10000Channel1.setChecked(status)
    #
    # def getBtnChart10000Channel1Status(self):
    #     """Return the status of the x10000 channel 1 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnChart10000Channel1.isChecked()
    #
    # def setBtnAutoscaleYChannel2Status(self, status):
    #     """Change the status of the autoscale Y channel 2 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnAutoscaleYChannel2.setChecked(status)
    #
    # def getBtnAutoscaleYChannel2Status(self):
    #     """Return the status of the autoscale Y channel 2 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnAutoscaleYChannel2.isChecked()
    #
    # def setBtnAutoscaleXChannel2Status(self, status):
    #     """Change the status of the autoscale X channel 2 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnAutoscaleXChannel2.setChecked(status)
    #
    # def getBtnAutoscaleXChannel2Status(self):
    #     """Return the status of the autoscale X channel 2 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnAutoscaleXChannel2.isChecked()
    #
    # def setBtnChart1000Channel2Status(self, status):
    #     """Change the status of the x1000 channel 2 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnChart1000Channel2.setChecked(status)
    #
    # def getBtnChart1000Channel2Status(self):
    #     """Return the status of the x1000 channel 2 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnChart1000Channel2.isChecked()
    #
    # def setBtnChart10000Channel2Status(self, status):
    #     """Change the status of the x10000 channel 2 button.
    #
    #     Args:
    #         status (bool): the status of the button.
    #     """
    #     self.btnChart10000Channel2.setChecked(status)
    #
    # def getBtnChart10000Channel2Status(self):
    #     """Return the status of the x10000 channel 2 button.
    #
    #     Returns:
    #         bool: the status of the button, if the button is pressed or depressed.
    #     """
    #     return self.btnChart10000Channel2.isChecked()

    """
    ********************************************************************************************************************
    *                                                End Chart Functions                                               *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Buttons Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleButtons(self):
        """Change the style of the buttons to the custom style."""
        self.btnInitExperiment.setStyleSheet(Styles.buttonInit)
        self.btnInitExperiment.setCheckable(True)

        self.btnLaser.setStyleSheet(Styles.buttonLaserAcquisitionSmall)
        self.btnLaser.setCheckable(True)

        self.btnFreeRunning.setStyleSheet(Styles.buttonFreeRunning)
        self.btnFreeRunning.setCheckable(True)

        self.btnPeristaltic.setStyleSheet(Styles.buttonPeristaltic)
        self.btnPeristaltic.setCheckable(True)

        self.btnInject_A.setStyleSheet(Styles.buttonImpulsionalSmall)
        self.btnInject_A.setCheckable(True)

        self.btnInject_B.setStyleSheet(Styles.buttonImpulsionalSmall)
        self.btnInject_B.setCheckable(True)

        self.btnPurge_A.setStyleSheet(Styles.buttonImpulsionalSmall)
        self.btnPurge_A.setCheckable(True)

        self.btnPurge_B.setStyleSheet(Styles.buttonImpulsionalSmall)
        self.btnPurge_B.setCheckable(True)

        self.btnSaveFile.setStyleSheet(Styles.buttonSaveFile)

        self.btnAutoscaleYChannel.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleYChannel.setCheckable(True)

        self.btnAutoscaleXChannel.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleXChannel.setCheckable(True)

        self.btnChart1000Channel.setStyleSheet(Styles.buttonChart)
        self.btnChart1000Channel.setCheckable(True)

        self.btnChart10000Channel.setStyleSheet(Styles.buttonChart)
        self.btnChart10000Channel.setCheckable(True)

        # self.btnAutoscaleYChannel1.setStyleSheet(Styles.buttonChart)
        # self.btnAutoscaleYChannel1.setCheckable(True)
        #
        # self.btnAutoscaleXChannel1.setStyleSheet(Styles.buttonChart)
        # self.btnAutoscaleXChannel1.setCheckable(True)
        #
        # self.btnChart1000Channel1.setStyleSheet(Styles.buttonChart)
        # self.btnChart1000Channel1.setCheckable(True)
        #
        # self.btnChart10000Channel1.setStyleSheet(Styles.buttonChart)
        # self.btnChart10000Channel1.setCheckable(True)
        #
        # self.btnAutoscaleYChannel2.setStyleSheet(Styles.buttonChart)
        # self.btnAutoscaleYChannel2.setCheckable(True)
        #
        # self.btnAutoscaleXChannel2.setStyleSheet(Styles.buttonChart)
        # self.btnAutoscaleXChannel2.setCheckable(True)
        #
        # self.btnChart1000Channel2.setStyleSheet(Styles.buttonChart)
        # self.btnChart1000Channel2.setCheckable(True)
        #
        # self.btnChart10000Channel2.setStyleSheet(Styles.buttonChart)
        # self.btnChart10000Channel2.setCheckable(True)

    """
    ********************************************************************************************************************
    *                                           End Buttons Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Spin Boxes Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setStyleSpinBox(self):
        """Change the style of the spin boxes to the custom style."""
        self.edtDataSampling.setStyleSheet(Styles.spinBoxGeneral)

        self.edtExperimentTime.setStyleSheet(Styles.spinBoxGeneral)
        self.edtExperimentTime.setRange(0, 100000)

        self.edtPeristaltic.setStyleSheet(Styles.spinBoxGeneral)
        self.edtPeristaltic.setFixedWidth(70)
        self.edtPeristaltic.setRange(0, 100)

        self.edtImpulsional_A.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_A.setFixedWidth(60)
        self.edtImpulsional_A.setRange(0, 100)

        self.edtImpulsional_B.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_B.setFixedWidth(60)
        self.edtImpulsional_B.setRange(0, 100)

    """
    ********************************************************************************************************************
    *                                          End Spin Boxes Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Line Edits Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setStyleLineEdit(self):
        """Change the style of the line edits to the custom style."""
        self.edtDataSampling.setFixedWidth(75)
        self.edtDataSampling.setAlignment(Qt.AlignRight)

        self.edtExperimentTime.setFixedWidth(75)
        self.edtExperimentTime.setAlignment(Qt.AlignRight)

        self.edtChannel_1.setStyleSheet(Styles.lineEditGeneral)
        self.edtChannel_1.setAlignment(Qt.AlignRight)
        self.edtChannel_1.setFixedWidth(100)

        self.edtChannel_2.setStyleSheet(Styles.lineEditGeneral)
        self.edtChannel_2.setAlignment(Qt.AlignRight)
        self.edtChannel_2.setFixedWidth(100)

        self.edtTime.setStyleSheet(Styles.lineEditGeneral)
        self.edtTime.setAlignment(Qt.AlignRight)
        self.edtTime.setFixedWidth(100)

        self.edtSaveFile.setStyleSheet(Styles.lineEditGeneral)

    """
    ********************************************************************************************************************
    *                                          End Line Edits Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                              Labels Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleLabels(self):
        """Change the style of the labels to the custom style."""
        self.lblBtnInit.setStyleSheet(Styles.labelBtnInit)
        self.lblBtnInit.setAlignment(Qt.AlignCenter)
        self.lblBtnInit.setWordWrap(True)

        self.lblDataSampling.setFixedWidth(75)
        self.lblDataSampling.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.lblExperimentTime.setFixedWidth(85)
        self.lblExperimentTime.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.lblChannel_1.setFixedWidth(50)

        self.lblChannel_2.setFixedWidth(50)

        self.lblTime.setFixedWidth(50)

        self.lblPeristaltic.setFixedWidth(70)
        self.lblPeristaltic.setAlignment(Qt.AlignBottom)

        self.lblBack.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblBack.setFixedWidth(42)
        self.lblBack.setAlignment(Qt.AlignCenter)

        self.lblStop.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblStop.setFixedWidth(42)
        self.lblStop.setAlignment(Qt.AlignCenter)

        self.lblForward.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblForward.setFixedWidth(42)
        self.lblForward.setAlignment(Qt.AlignCenter)

        self.lblImpulsional_A.setFixedWidth(60)
        self.lblImpulsional_A.setAlignment(Qt.AlignBottom)

        self.lblImpulsional_B.setFixedWidth(60)
        self.lblImpulsional_B.setAlignment(Qt.AlignBottom)

    """
    ********************************************************************************************************************
    *                                            End Labels Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                         Rectangle Button Styles Functions                                        *
    ********************************************************************************************************************
    """

    def setStyleRectangleButton(self):
        """Change the style of the rectangle button to the custom style."""
        self.btnStopPeristaltic.on_color_1 = QColor(4, 180, 4)
        self.btnStopPeristaltic.on_color_2 = QColor(8, 138, 8)
        self.btnStopPeristaltic.off_color_1 = QColor(0, 0, 0)
        self.btnStopPeristaltic.off_color_2 = QColor(0, 0, 0)

    """
    ********************************************************************************************************************
    *                                      End Rectangle Button Styles Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                         Triangle Button Styles Functions                                         *
    ********************************************************************************************************************
    """

    def setStyleTriangleButton(self):
        """Change the style of the triangle button to the custom style."""
        self.btnBackPeristaltic.on_color_1 = QColor(4, 180, 4)
        self.btnBackPeristaltic.on_color_2 = QColor(8, 138, 8)
        self.btnBackPeristaltic.off_color_1 = QColor(0, 0, 0)
        self.btnBackPeristaltic.off_color_2 = QColor(0, 0, 0)

        self.btnForwardPeristaltic.on_color_1 = QColor(4, 180, 4)
        self.btnForwardPeristaltic.on_color_2 = QColor(8, 138, 8)
        self.btnForwardPeristaltic.off_color_1 = QColor(0, 0, 0)
        self.btnForwardPeristaltic.off_color_2 = QColor(0, 0, 0)

    """
    ********************************************************************************************************************
    *                                      End Triangle Button Styles Functions                                        *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Pixmap Styles Functions                                              *
    ********************************************************************************************************************
    """

    def setStylePixmap(self):
        """Change the style of the pixmap to the custom style."""
        self.imageLogo = self.imageLogo.scaledToHeight(50)

    """
    ********************************************************************************************************************
    *                                           End Pixmap Styles Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Group Box Styles Functions                                            *
    ********************************************************************************************************************
    """

    def setStyleGroupBox(self):
        """Change the style of the group boxes to the custom style."""
        self.timeBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.peristalticBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.peristalticControlBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.injectControlBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.fluidicBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.saveFileBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.imageBoxLayout.setStyleSheet(Styles.groupBoxGeneralWithoutBorder)

        self.chartBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

    """
    ********************************************************************************************************************
    *                                          End Group Box Styles Functions                                          *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Layouts Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleLayouts(self):
        """Change the style of the layouts to the custom style."""
        self.dataSamplingLayout.setAlignment(Qt.AlignRight)

        self.experimentTimeLayout.setAlignment(Qt.AlignRight)

        self.peristalticControlLayout.setAlignment(Qt.AlignBottom)

        self.peristalticLayout.setAlignment(Qt.AlignCenter)

        self.imageLayout.setAlignment(Qt.AlignCenter)

        self.btnChartLayoutChannel.setAlignment(Qt.AlignRight)

        # self.btnChartLayoutChannel1.setAlignment(Qt.AlignRight)

        # self.btnChartLayoutChannel2.setAlignment(Qt.AlignRight)

    """
    ********************************************************************************************************************
    *                                           End Layouts Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                Messages Functions                                                *
    ********************************************************************************************************************
    """

    def setMessageCritical(self, message):
        """Show dialog with a message of error.

        Args:
            message (str): message to show in the dialog.
        """
        QMessageBox.critical(self, Strings.error, message)

    def setMessageQuestion(self, message):
        """Show dialog with a question.

        Args:
            message (str): question to show in the dialog.

        Returns:
            bool: return True if the answer to the question is Yes, in the opposite case, return False if the answer is
            No.
        """
        saveFile = QMessageBox.question(self, Strings.question, message, QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)

        if saveFile == QMessageBox.Yes:
            return True

        else:
            return False

    def setDialogSaveFile(self, myNameFile):
        """Show dialog to save the file with the name (myNameFile).

        Args:
            myNameFile (str): name of the file.

        Returns:
            str: name of the file.
        """
        fileName, _ = QFileDialog.getSaveFileName(self, Strings.saveFileLC, 'C:/Users/' + getpass.getuser() +
                                                  '/Documents/' + myNameFile, '*.DAT')

        return fileName

    """
    ********************************************************************************************************************
    *                                              End Messages Functions                                              *
    ********************************************************************************************************************
    """
