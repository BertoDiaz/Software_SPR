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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox, QProgressBar, QLabel, QFileDialog
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit, QSpinBox, QStylePainter
from PyQt5.QtCore import Qt
from lib.LedIndicatorWidget import LedIndicator
from lib.TriangleButton import TriangleButton
from lib.RectangleButton import RectangleButton
import styles as style


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

        self.ledLaser = LedIndicator(self)

        self.layoutGrid = QGridLayout(self)

        self.timeBoxLayout = QGroupBox('Time Parameters')
        self.dataSamplingBoxLayout = QGroupBox()
        self.experimentTimeBoxLayout = QGroupBox()
        self.statusLaserBoxLayout = QGroupBox()

        self.fluidicBoxLayout = QGroupBox('Fluidic Parameters')
        self.peristalticControlBoxLayout = QGroupBox('Peristaltic Pump Control')
        self.injectControlBoxLayout = QGroupBox('Injection Pump Control')
        self.peristalticBoxLayout = QGroupBox()

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
        self.layoutGrid.addWidget(self.setFluidicGroup(), 1, 0, 1, 3)
        self.layoutGrid.addWidget(self.setFilledGroup_1(), 2, 0, 5, 10)

    def setFilledGroup_1(self):
        self.filledBoxLayout_1.setStyleSheet(style.groupBoxFilled)

        return self.filledBoxLayout_1

    def setFilledGroup_2(self):
        self.filledLayout_2.setStyleSheet(style.groupBoxFilled)

        return self.filledLayout_2

    def setTimeGroup(self):
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
        self.lblBtnInit.setWordWrap(True)
        self.edtDataSampling.setFixedWidth(75)
        self.edtDataSampling.setAlignment(Qt.AlignRight)
        self.edtExperimentTime.setFixedWidth(75)
        self.edtExperimentTime.setAlignment(Qt.AlignRight)
        self.edtChannel_1.setFixedWidth(100)
        self.edtChannel_2.setFixedWidth(100)
        self.edtTime.setFixedWidth(100)

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

        self.timeBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.timeBoxLayout.setLayout(self.timeLayout)

        return self.timeBoxLayout

    def setFluidicGroup(self):
        self.lblPeristaltic.setFixedWidth(100)
        self.lblPeristaltic.setAlignment(Qt.AlignBottom)
        self.lblImpulsional_A.setFixedWidth(100)
        self.lblImpulsional_A.setAlignment(Qt.AlignBottom)
        self.lblImpulsional_B.setFixedWidth(100)
        self.lblImpulsional_B.setAlignment(Qt.AlignBottom)

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

        self.peristalticBoxLayout.setStyleSheet(style.groupBoxGeneralWithoutBorder)
        self.peristalticBoxLayout.setLayout(self.peristalticLayout)

        self.peristalticControlLayout.addWidget(self.peristalticBoxLayout, 2, 0, 1, 3)

        self.peristalticControlBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.peristalticControlBoxLayout.setLayout(self.peristalticControlLayout)

        self.injectControlLayout.addWidget(self.lblImpulsional_A, 0, 0)
        self.injectControlLayout.addWidget(self.lblImpulsional_B, 0, 1)
        self.injectControlLayout.addWidget(self.edtImpulsional_A, 1, 0)
        self.injectControlLayout.addWidget(self.edtImpulsional_B, 1, 1)
        self.injectControlLayout.addWidget(self.btnInject_A, 2, 0)
        self.injectControlLayout.addWidget(self.btnInject_B, 2, 1)
        self.injectControlLayout.addWidget(self.btnPurge_A, 3, 0)
        self.injectControlLayout.addWidget(self.btnPurge_B, 3, 1)

        self.injectControlBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.injectControlBoxLayout.setLayout(self.injectControlLayout)

        self.fluidicLayout.addWidget(self.peristalticControlBoxLayout, 0, 0)
        self.fluidicLayout.addWidget(self.injectControlBoxLayout, 0, 1)

        self.fluidicBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.fluidicBoxLayout.setLayout(self.fluidicLayout)

        return self.fluidicBoxLayout

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
    *                                             Buttons Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleButtons(self):
        self.btnInitExperiment.setStyleSheet(style.buttonInit)
        self.btnInitExperiment.setCheckable(True)

        self.btnFreeRunning.setStyleSheet(style.buttonFreeRunning)
        self.btnFreeRunning.setCheckable(True)

        self.btnPeristaltic.setStyleSheet(style.buttonPeristaltic)
        self.btnPeristaltic.setCheckable(True)

        self.btnInject_A.setStyleSheet(style.buttonImpulsionalSmall)
        self.btnInject_A.setCheckable(True)

        self.btnInject_B.setStyleSheet(style.buttonImpulsionalSmall)
        self.btnInject_B.setCheckable(True)

        self.btnPurge_A.setStyleSheet(style.buttonImpulsionalSmall)
        self.btnPurge_A.setCheckable(True)

        self.btnPurge_B.setStyleSheet(style.buttonImpulsionalSmall)
        self.btnPurge_B.setCheckable(True)

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
        self.edtDataSampling.setStyleSheet(style.spinBoxGeneral)
        self.edtExperimentTime.setStyleSheet(style.spinBoxGeneral)
        self.edtPeristaltic.setStyleSheet(style.spinBoxGeneral)
        self.edtImpulsional_A.setStyleSheet(style.spinBoxGeneral)
        self.edtImpulsional_B.setStyleSheet(style.spinBoxGeneral)

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
        self.edtChannel_1.setStyleSheet(style.lineEditGeneral)
        self.edtChannel_2.setStyleSheet(style.lineEditGeneral)
        self.edtTime.setStyleSheet(style.lineEditGeneral)

        self.edtChannel_1.setAlignment(Qt.AlignRight)
        self.edtChannel_2.setAlignment(Qt.AlignRight)
        self.edtTime.setAlignment(Qt.AlignRight)

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
        self.lblBtnInit.setStyleSheet(style.labelBtnInit)
        self.lblBtnInit.setAlignment(Qt.AlignCenter)
        self.lblBack.setStyleSheet(style.labelBtnPeristaltic)
        self.lblBack.setAlignment(Qt.AlignCenter)
        self.lblStop.setStyleSheet(style.labelBtnPeristaltic)
        self.lblStop.setAlignment(Qt.AlignCenter)
        self.lblForward.setStyleSheet(style.labelBtnPeristaltic)
        self.lblForward.setAlignment(Qt.AlignCenter)

    """
    ********************************************************************************************************************
    *                                            End Labels Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

