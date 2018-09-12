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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit, QSpinBox
from PyQt5.QtCore import Qt
from lib.LedIndicatorWidget import LedIndicator
from lib.TriangleButton import TriangleButton
from lib.RectangleButton import RectangleButton
from lib.Chart import Chart
from lib import Styles


class ViewDataAcquisition(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.unitTime = ' s'
        self.forward = 'forward'
        self.back = 'back'

        self.timeoutMessage = {
            'Init Experiment': 'The device has not respond, try again.'
        }

        self.lblDataSampling = QLabel('Data Sampling:')
        self.edtDataSampling = QSpinBox()
        self.lblExperimentTime = QLabel('Experiment Time:')
        self.edtExperimentTime = QSpinBox()
        self.lblLaser = QLabel('Status Laser')
        self.lblChannel_1 = QLabel('Channel 1')
        self.edtChannel_1 = QLineEdit()
        self.lblChannel_2 = QLabel('Channel 2')
        self.edtChannel_2 = QLineEdit()
        self.lblTime = QLabel('Time')
        self.edtTime = QLineEdit()
        self.lblBtnInit = QLabel('Start Experiment')

        self.lblPeristaltic = QLabel('Flow Peristaltic')
        self.edtPeristaltic = QSpinBox()
        self.lblImpulsional_A = QLabel('Injection A:')
        self.edtImpulsional_A = QSpinBox()
        self.lblImpulsional_B = QLabel('Injection B:')
        self.edtImpulsional_B = QSpinBox()
        self.lblBack = QLabel('BACK')
        self.lblForward = QLabel('FORWARD')
        self.lblStop = QLabel('STOP')

        self.btnInitExperiment = QPushButton()
        self.btnFreeRunning = QPushButton('Free Running')

        self.btnPeristaltic = QPushButton('START')
        self.btnInject_A = QPushButton('INJECT')
        self.btnInject_B = QPushButton('INJECT')
        self.btnPurge_A = QPushButton('PURGE')
        self.btnPurge_B = QPushButton('PURGE')
        self.btnBackPeristaltic = TriangleButton(50, self.back)
        self.btnForwardPeristaltic = TriangleButton(50, self.forward)
        self.btnStopPeristaltic = RectangleButton(50)
        self.btnChart1000Channel1 = QPushButton('x1000')
        self.btnChart10000Channel1 = QPushButton('x10000')
        self.btnAutoscaleXChannel1 = QPushButton('Autoscale X')
        self.btnAutoscaleYChannel1 = QPushButton('Autoscale Y')
        self.btnChart1000Channel2 = QPushButton('x1000')
        self.btnChart10000Channel2 = QPushButton('x10000')
        self.btnAutoscaleXChannel2 = QPushButton('Autoscale X')
        self.btnAutoscaleYChannel2 = QPushButton('Autoscale Y')

        self.ledLaser = LedIndicator(self)

        self.myChartChannel1 = Chart('CHANNEL 1')
        self.myChartChannel2 = Chart('CHANNEL 2')

        self.layoutGrid = QGridLayout(self)

        self.timeBoxLayout = QGroupBox('Time Parameters')
        self.dataSamplingBoxLayout = QGroupBox()
        self.experimentTimeBoxLayout = QGroupBox()
        self.statusLaserBoxLayout = QGroupBox()

        self.fluidicBoxLayout = QGroupBox('Fluidic Parameters')
        self.peristalticControlBoxLayout = QGroupBox('Peristaltic Pump Control')
        self.injectControlBoxLayout = QGroupBox('Injection Pump Control')
        self.peristalticBoxLayout = QGroupBox()
        self.chartBoxLayout = QGroupBox()

        self.filledBoxLayout_1 = QGroupBox()
        self.filledLayout_2 = QGroupBox()

        self.timeLayout = QGridLayout(self)
        self.dataSamplingLayout = QGridLayout(self)
        self.experimentTimeLayout = QGridLayout(self)
        self.statusLaserLayout = QGridLayout(self)

        self.fluidicLayout = QGridLayout(self)
        self.peristalticControlLayout = QGridLayout(self)
        self.injectControlLayout = QGridLayout(self)
        self.peristalticLayout = QGridLayout(self)

        self.btnInitLayout = QVBoxLayout(self)
        self.chartLayout = QVBoxLayout(self)

        self.btnChartLayoutChannel1 = QHBoxLayout(self)
        self.btnChartLayoutChannel2 = QHBoxLayout(self)

        self.setStyleButtons()
        self.setStyleSpinBox()
        self.setStyleLineEdit()
        self.setStyleLabels()

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setTimeGroup(), 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.setFluidicGroup(), 1, 0, 1, 2)
        self.layoutGrid.addWidget(self.setChartGroup(), 0, 2, 8, 8)
        # self.layoutGrid.addWidget(self.setFilledGroup_1(), 2, 0, 5, 10)

    def setFilledGroup_1(self):
        self.filledBoxLayout_1.setStyleSheet(Styles.groupBoxFilled)

        return self.filledBoxLayout_1

    def setFilledGroup_2(self):
        self.filledLayout_2.setStyleSheet(Styles.groupBoxFilled)

        return self.filledLayout_2

    def setTimeGroup(self):
        self.setLedLaserDisable(True)

        self.dataSamplingLayout.setAlignment(Qt.AlignRight)
        self.experimentTimeLayout.setAlignment(Qt.AlignRight)

        self.btnInitLayout.addWidget(self.lblBtnInit)

        self.btnInitExperiment.setLayout(self.btnInitLayout)

        self.dataSamplingLayout.addWidget(self.lblDataSampling, 0, 0)
        self.dataSamplingLayout.addWidget(self.edtDataSampling, 0, 1)

        self.dataSamplingBoxLayout.setLayout(self.dataSamplingLayout)

        self.experimentTimeLayout.addWidget(self.lblExperimentTime, 0, 1)
        self.experimentTimeLayout.addWidget(self.edtExperimentTime, 0, 2)
        self.experimentTimeLayout.addWidget(self.btnFreeRunning, 1, 0, 1, 3)

        self.experimentTimeBoxLayout.setLayout(self.experimentTimeLayout)

        self.statusLaserLayout.addWidget(self.lblLaser, 0, 0)
        self.statusLaserLayout.addWidget(self.ledLaser, 1, 0)

        self.statusLaserBoxLayout.setLayout(self.statusLaserLayout)

        self.timeLayout.addWidget(self.btnInitExperiment, 0, 0, 5, 1)
        self.timeLayout.addWidget(self.dataSamplingBoxLayout, 0, 1, 1, 3)
        self.timeLayout.addWidget(self.experimentTimeBoxLayout, 1, 1, 1, 3)
        self.timeLayout.addWidget(self.statusLaserBoxLayout, 2, 1, 3, 1)
        self.timeLayout.addWidget(self.lblChannel_1, 2, 2)
        self.timeLayout.addWidget(self.edtChannel_1, 2, 3)
        self.timeLayout.addWidget(self.lblChannel_2, 3, 2)
        self.timeLayout.addWidget(self.edtChannel_2, 3, 3)
        self.timeLayout.addWidget(self.lblTime, 4, 2)
        self.timeLayout.addWidget(self.edtTime, 4, 3)

        self.timeBoxLayout.setStyleSheet(Styles.groupBoxGeneral)
        self.timeBoxLayout.setLayout(self.timeLayout)

        return self.timeBoxLayout

    def setFluidicGroup(self):
        self.peristalticControlLayout.setAlignment(Qt.AlignBottom)

        self.peristalticControlLayout.addWidget(self.lblPeristaltic, 0, 0)
        self.peristalticControlLayout.addWidget(self.edtPeristaltic, 1, 0)
        self.peristalticControlLayout.addWidget(self.btnPeristaltic, 0, 1, 2, 1)

        self.peristalticLayout.addWidget(self.btnBackPeristaltic, 0, 0)
        self.peristalticLayout.addWidget(self.btnStopPeristaltic, 0, 1)
        self.peristalticLayout.addWidget(self.btnForwardPeristaltic, 0, 2)
        self.peristalticLayout.addWidget(self.lblBack, 1, 0)
        self.peristalticLayout.addWidget(self.lblStop, 1, 1)
        self.peristalticLayout.addWidget(self.lblForward, 1, 2)

        self.peristalticLayout.setAlignment(Qt.AlignCenter)

        self.peristalticBoxLayout.setStyleSheet(Styles.groupBoxGeneralWithoutBorder)
        self.peristalticBoxLayout.setLayout(self.peristalticLayout)

        self.peristalticControlLayout.addWidget(self.peristalticBoxLayout, 2, 0, 1, 3)

        self.peristalticControlBoxLayout.setStyleSheet(Styles.groupBoxGeneral)
        self.peristalticControlBoxLayout.setLayout(self.peristalticControlLayout)

        self.injectControlLayout.addWidget(self.lblImpulsional_A, 0, 0)
        self.injectControlLayout.addWidget(self.lblImpulsional_B, 0, 1)
        self.injectControlLayout.addWidget(self.edtImpulsional_A, 1, 0)
        self.injectControlLayout.addWidget(self.edtImpulsional_B, 1, 1)
        self.injectControlLayout.addWidget(self.btnInject_A, 2, 0)
        self.injectControlLayout.addWidget(self.btnInject_B, 2, 1)
        self.injectControlLayout.addWidget(self.btnPurge_A, 3, 0)
        self.injectControlLayout.addWidget(self.btnPurge_B, 3, 1)

        self.injectControlBoxLayout.setStyleSheet(Styles.groupBoxGeneral)
        self.injectControlBoxLayout.setLayout(self.injectControlLayout)

        self.fluidicLayout.addWidget(self.peristalticControlBoxLayout, 0, 0, 2, 1)
        self.fluidicLayout.addWidget(self.injectControlBoxLayout, 0, 1, 1, 1)

        self.fluidicBoxLayout.setStyleSheet(Styles.groupBoxGeneral)
        self.fluidicBoxLayout.setLayout(self.fluidicLayout)

        return self.fluidicBoxLayout

    def setChartGroup(self):
        self.btnChartLayoutChannel1.setAlignment(Qt.AlignRight)
        self.btnChartLayoutChannel2.setAlignment(Qt.AlignRight)

        self.btnChartLayoutChannel1.addWidget(self.btnAutoscaleYChannel1)
        self.btnChartLayoutChannel1.addWidget(self.btnAutoscaleXChannel1)
        self.btnChartLayoutChannel1.addWidget(self.btnChart1000Channel1)
        self.btnChartLayoutChannel1.addWidget(self.btnChart10000Channel1)

        self.btnChartLayoutChannel2.addWidget(self.btnAutoscaleYChannel2)
        self.btnChartLayoutChannel2.addWidget(self.btnAutoscaleXChannel2)
        self.btnChartLayoutChannel2.addWidget(self.btnChart1000Channel2)
        self.btnChartLayoutChannel2.addWidget(self.btnChart10000Channel2)

        self.chartLayout.addLayout(self.btnChartLayoutChannel1)
        self.chartLayout.addWidget(self.myChartChannel1)
        self.chartLayout.addLayout(self.btnChartLayoutChannel2)
        self.chartLayout.addWidget(self.myChartChannel2)

        self.chartBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.chartBoxLayout.setLayout(self.chartLayout)

        return self.chartBoxLayout

    """
    ********************************************************************************************************************
    *                                        Init Experiment Button Functions                                          *
    ********************************************************************************************************************
    """

    def setBtnInitExperimentStatus(self, status):
        if status:
            text = 'Stop Experiment'

        else:
            text = 'Start Experiment'

        self.lblBtnInit.setText(text)
        self.btnInitExperiment.setChecked(status)

    def getBtnInitExperimentStatus(self):
        return self.btnInitExperiment.isChecked()

    """
    ********************************************************************************************************************
    *                                      End Init Experiment Button Functions                                        *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                               Laser Led Functions                                                *
    ********************************************************************************************************************
    """

    def setLedLaserStatus(self, status):
        self.ledLaser.setChecked(status)

    def getLedLaserStatus(self):
        return self.ledLaser.isChecked()

    def setLedLaserDisable(self, disable):
        self.ledLaser.setDisabled(disable)

    """
    ********************************************************************************************************************
    *                                             End Laser Led Functions                                              *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Acquisition Values Functions                                            *
    ********************************************************************************************************************
    """

    def setEdtChannel1Text(self, text):
        text = str('{0:.3f}'.format(text))
        self.edtChannel_1.setText(text)

    def getEdtChannel1Text(self):
        return float(self.edtChannel_1.text())

    def setEdtChannel2Text(self, text):
        text = str('{0:.3f}'.format(text))
        self.edtChannel_2.setText(text)

    def getEdtChannel2Text(self):
        return float(self.edtChannel_2.text())

    def setEdtTimeText(self, text):
        self.edtTime.setText(str(text) + self.unitTime)

    def getEdtTimeText(self):
        text = self.edtTime.text().replace(' s', '')
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
        if status:
            text = 'STOP'

        else:
            text = 'START'

        self.btnPeristaltic.setText(text)
        self.btnPeristaltic.setChecked(status)

    def getBtnPeristalticStatus(self):
        return self.btnPeristaltic.isChecked()

    def setBtnPeristalticDisable(self, disable):
        self.btnPeristaltic.setDisabled(disable)

    def setBtnBackPeristalticStatus(self, status):
        self.btnBackPeristaltic.setChecked(status)

    def getBtnBackPeristalticStatus(self):
        return self.btnBackPeristaltic.isChecked()

    def setBtnBackPeristalticDisable(self, disable):
        self.btnBackPeristaltic.setDisabled(disable)

    def setBtnStopPeristalticStatus(self, status):
        self.btnStopPeristaltic.setChecked(status)

    def getBtnStopPeristalticStatus(self):
        return self.btnStopPeristaltic.isChecked()

    def setBtnStopPeristalticDisable(self, disable):
        self.btnStopPeristaltic.setDisabled(disable)

    def setBtnForwardPeristalticStatus(self, status):
        self.btnForwardPeristaltic.setChecked(status)

    def getBtnForwardPeristalticStatus(self):
        return self.btnForwardPeristaltic.isChecked()

    def setBtnForwardPeristalticDisable(self, disable):
        self.btnForwardPeristaltic.setDisabled(disable)

    def setBtnBSFPeristalticStatus(self, status, who):
        if who == 0:
            self.setBtnBackPeristalticStatus(status)

        elif who == 1:
            self.setBtnStopPeristalticStatus(status)

        else:
            self.setBtnForwardPeristalticStatus(status)

    def getBtnBSFPeristalticStatus(self, who):
        if who == 0:
            return self.getBtnBackPeristalticStatus()

        elif who == 1:
            return self.getBtnStopPeristalticStatus()

        else:
            return self.getBtnForwardPeristalticStatus()

    def setBtnBSFPeristalticNotStatus(self, status, who):
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
        self.setBtnBackPeristalticDisable(disable)
        self.setBtnStopPeristalticDisable(disable)
        self.setBtnForwardPeristalticDisable(disable)

    def setEdtPeristalticValue(self, value):
        self.edtPeristaltic.setValue(value)

    def getEdtPeristalticValue(self):
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
        self.btnPurge_A.setChecked(status)
        self.setBtnImpulsionalADisable(status)

    def getBtnImpulsionalAStatus(self):
        return self.btnPurge_A.isChecked()

    def setBtnImpulsionalADisable(self, disable):
        self.btnPurge_A.setDisabled(disable)

    def setBtnInjectAStatus(self, status):
        self.btnInject_A.setChecked(status)
        self.setBtnInjectADisable(status)

    def getBtnInjectAStatus(self):
        return self.btnInject_A.isChecked()

    def setBtnInjectADisable(self, disable):
        self.btnInject_A.setDisabled(disable)

    def setEdtImpulsionalAValue(self, value):
        self.edtImpulsional_A.setValue(value)

    def getEdtImpulsionalAValue(self):
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
        self.btnPurge_B.setChecked(status)
        self.setBtnImpulsionalBDisable(status)

    def getBtnImpulsionalBStatus(self):
        return self.btnPurge_B.isChecked()

    def setBtnImpulsionalBDisable(self, disable):
        self.btnPurge_B.setDisabled(disable)

    def setBtnInjectBStatus(self, status):
        self.btnInject_B.setChecked(status)
        self.setBtnInjectBDisable(status)

    def getBtnInjectBStatus(self):
        return self.btnInject_B.isChecked()

    def setBtnInjectBDisable(self, disable):
        self.btnInject_B.setDisabled(disable)

    def setEdtImpulsionalBValue(self, value):
        self.edtImpulsional_B.setValue(value)

    def getEdtImpulsionalBValue(self):
        return self.edtImpulsional_B.value()

    """
    ********************************************************************************************************************
    *                                        End Impulsional B Control Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                  Chart Functions                                                 *
    ********************************************************************************************************************
    """

    def setDataChannel1(self, xData, yData):
        self.myChartChannel1.setDataChart(xData, yData)

    def setDataChannel2(self, xData, yData):
        self.myChartChannel2.setDataChart(xData, yData)

    def setRangeYChannel1(self, yRange, autoscale):
        self.myChartChannel1.setRangeY(yRange, autoscale)

    def setRangeXChannel1(self, xRange):
        self.myChartChannel1.setRangeX(xRange)

    def getRangeXChannel1(self):
        return self.myChartChannel1.getRangeX()

    def setRangeYChannel2(self, yRange, autoscale):
        self.myChartChannel2.setRangeY(yRange, autoscale)

    def setRangeXChannel2(self, xRange):
        self.myChartChannel2.setRangeX(xRange)

    def getRangeXChannel2(self):
        return self.myChartChannel2.getRangeX()

    def setBtnAutoscaleYChannel1Status(self, status):
        self.btnAutoscaleYChannel1.setChecked(status)

    def getBtnAutoscaleYChannel1Status(self):
        return self.btnAutoscaleYChannel1.isChecked()

    def setBtnAutoscaleXChannel1Status(self, status):
        self.btnAutoscaleXChannel1.setChecked(status)

    def getBtnAutoscaleXChannel1Status(self):
        return self.btnAutoscaleXChannel1.isChecked()

    def setBtnChart1000Channel1Status(self, status):
        self.btnChart1000Channel1.setChecked(status)

    def getBtnChart1000Channel1Status(self):
        return self.btnChart1000Channel1.isChecked()

    def setBtnChart10000Channel1Status(self, status):
        self.btnChart10000Channel1.setChecked(status)

    def getBtnChart10000Channel1Status(self):
        return self.btnChart10000Channel1.isChecked()

    def setBtnAutoscaleYChannel2Status(self, status):
        self.btnAutoscaleYChannel2.setChecked(status)

    def getBtnAutoscaleYChannel2Status(self):
        return self.btnAutoscaleYChannel2.isChecked()

    def setBtnAutoscaleXChannel2Status(self, status):
        self.btnAutoscaleXChannel2.setChecked(status)

    def getBtnAutoscaleXChannel2Status(self):
        return self.btnAutoscaleXChannel2.isChecked()

    def setBtnChart1000Channel2Status(self, status):
        self.btnChart1000Channel2.setChecked(status)

    def getBtnChart1000Channel2Status(self):
        return self.btnChart1000Channel2.isChecked()

    def setBtnChart10000Channel2Status(self, status):
        self.btnChart10000Channel2.setChecked(status)

    def getBtnChart10000Channel2Status(self):
        return self.btnChart10000Channel2.isChecked()

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
        self.btnInitExperiment.setStyleSheet(Styles.buttonInit)
        self.btnInitExperiment.setCheckable(True)

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

        self.btnAutoscaleYChannel1.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleYChannel1.setCheckable(True)

        self.btnAutoscaleXChannel1.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleXChannel1.setCheckable(True)

        self.btnChart1000Channel1.setStyleSheet(Styles.buttonChart)
        self.btnChart1000Channel1.setCheckable(True)

        self.btnChart10000Channel1.setStyleSheet(Styles.buttonChart)
        self.btnChart10000Channel1.setCheckable(True)

        self.btnAutoscaleYChannel2.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleYChannel2.setCheckable(True)

        self.btnAutoscaleXChannel2.setStyleSheet(Styles.buttonChart)
        self.btnAutoscaleXChannel2.setCheckable(True)

        self.btnChart1000Channel2.setStyleSheet(Styles.buttonChart)
        self.btnChart1000Channel2.setCheckable(True)

        self.btnChart10000Channel2.setStyleSheet(Styles.buttonChart)
        self.btnChart10000Channel2.setCheckable(True)

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
        self.edtDataSampling.setStyleSheet(Styles.spinBoxGeneral)
        self.edtExperimentTime.setStyleSheet(Styles.spinBoxGeneral)
        self.edtPeristaltic.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_A.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_B.setStyleSheet(Styles.spinBoxGeneral)

        self.edtPeristaltic.setRange(0, 100)
        self.edtImpulsional_A.setRange(0, 100)
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

        self.lblLaser.setFixedWidth(50)
        self.lblLaser.setWordWrap(True)
        self.lblLaser.setAlignment(Qt.AlignCenter)

        self.lblPeristaltic.setFixedWidth(100)
        self.lblPeristaltic.setAlignment(Qt.AlignBottom)

        self.lblBack.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblBack.setAlignment(Qt.AlignCenter)

        self.lblStop.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblStop.setAlignment(Qt.AlignCenter)

        self.lblForward.setStyleSheet(Styles.labelBtnPeristaltic)
        self.lblForward.setAlignment(Qt.AlignCenter)

        self.lblImpulsional_A.setFixedWidth(100)
        self.lblImpulsional_A.setAlignment(Qt.AlignBottom)

        self.lblImpulsional_B.setFixedWidth(100)
        self.lblImpulsional_B.setAlignment(Qt.AlignBottom)

    """
    ********************************************************************************************************************
    *                                            End Labels Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)
