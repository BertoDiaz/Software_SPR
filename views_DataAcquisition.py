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
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt, QRect
from lib.LedIndicatorWidget import LedIndicator
import styles as style


class ViewDataAcquisition(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.lblDataSampling = QLabel("Data Sampling:")
        self.edtDataSampling = QSpinBox()
        self.lblExperimentTime = QLabel("Experiment Time:")
        self.edtExperimentTime = QSpinBox()
        self.lblStatusLaser = QLabel("Status Laser")
        self.lblChannel_1 = QLabel("Channel 1")
        self.edtChannel_1 = QLineEdit()
        self.lblChannel_2 = QLabel("Channel 2")
        self.edtChannel_2 = QLineEdit()
        self.lblTime = QLabel("Time")
        self.edtTime = QLineEdit()
        self.lblBtnInit = QLabel("Experiment Start")

        self.btnInit = QPushButton()
        self.btnFreeRunning = QPushButton("Free Running")

        self.ledStatusLaser = LedIndicator(self)
        self.ledStatusLaser.setDisabled(True)

        self.layoutGrid = QGridLayout(self)

        self.timeBoxLayout = QGroupBox("Time Parameters")
        self.dataSamplingBoxLayout = QGroupBox()
        self.experimentTimeBoxLayout = QGroupBox()
        self.statusLaserBoxLayout = QGroupBox()

        self.filledBoxLayout_1 = QGroupBox()
        self.filledLayout_2 = QGroupBox()

        self.timeLayout = QGridLayout(self)
        self.dataSamplingLayout = QGridLayout(self)
        self.experimentTimeLayout = QGridLayout(self)
        self.statusLaserLayout = QGridLayout(self)

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
        self.layoutGrid.addWidget(self.setFilledGroup_1(), 1, 0, 5, 10)

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
        self.lblStatusLaser.setFixedWidth(50)
        self.lblStatusLaser.setWordWrap(True)
        self.lblStatusLaser.setAlignment(Qt.AlignCenter)
        self.lblBtnInit.setWordWrap(True)
        self.edtDataSampling.setFixedWidth(75)
        self.edtDataSampling.setAlignment(Qt.AlignRight)
        self.edtExperimentTime.setFixedWidth(75)
        self.edtExperimentTime.setAlignment(Qt.AlignRight)
        self.edtChannel_1.setFixedWidth(100)
        self.edtChannel_2.setFixedWidth(100)
        self.edtTime.setFixedWidth(100)

        self.dataSamplingLayout.setAlignment(Qt.AlignRight)
        self.experimentTimeLayout.setAlignment(Qt.AlignRight)

        self.btnInitLayout.addWidget(self.lblBtnInit)

        self.btnInit.setLayout(self.btnInitLayout)

        self.dataSamplingLayout.addWidget(self.lblDataSampling, 0, 0)
        self.dataSamplingLayout.addWidget(self.edtDataSampling, 0, 1)

        self.dataSamplingBoxLayout.setLayout(self.dataSamplingLayout)

        self.experimentTimeLayout.addWidget(self.lblExperimentTime, 0, 1)
        self.experimentTimeLayout.addWidget(self.edtExperimentTime, 0, 2)
        self.experimentTimeLayout.addWidget(self.btnFreeRunning, 1, 0, 1, 3)

        self.experimentTimeBoxLayout.setLayout(self.experimentTimeLayout)

        self.statusLaserLayout.addWidget(self.lblStatusLaser, 0, 0)
        self.statusLaserLayout.addWidget(self.ledStatusLaser, 1, 0)

        self.statusLaserBoxLayout.setLayout(self.statusLaserLayout)

        self.timeLayout.addWidget(self.btnInit, 0, 0, 5, 1)
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

    def setStyleButtons(self):
        self.btnInit.setStyleSheet(style.buttonInit)
        self.btnInit.setCheckable(True)

        self.btnFreeRunning.setStyleSheet(style.buttonFreeRunning)
        self.btnFreeRunning.setCheckable(True)

    def setStyleSpinBox(self):
        self.edtDataSampling.setStyleSheet(style.spinBoxGeneral)
        self.edtExperimentTime.setStyleSheet(style.spinBoxGeneral)

    def setStyleLineEdit(self):
        self.edtChannel_1.setStyleSheet(style.lineEditGeneral)
        self.edtChannel_2.setStyleSheet(style.lineEditGeneral)
        self.edtTime.setStyleSheet(style.lineEditGeneral)

    def setStyleLabels(self):
        self.lblBtnInit.setStyleSheet(style.labelBtnInit)
        self.lblBtnInit.setAlignment(Qt.AlignCenter)

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

