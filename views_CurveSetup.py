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
import styles as style


class ViewCurveSetup(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.lblGainA = QLabel("Gain A:")
        self.edtGainA = QSpinBox()
        self.edtGainA.setRange(0, 100)
        self.lblGainB = QLabel("Gain B:")
        self.edtGainB = QSpinBox()
        self.edtGainB.setRange(0, 100)
        self.lblOffsetA = QLabel("Offset A:")
        self.edtOffsetA = QSpinBox()
        self.edtOffsetA.setRange(0, 100)
        self.lblOffsetB = QLabel("Offset B:")
        self.edtOffsetB = QSpinBox()
        self.edtOffsetB.setRange(0, 100)

        self.btnCalibrate = QPushButton("Calibrate")
        self.btnLaser = QPushButton("Laser OFF")

        self.lblInitialAngle = QLabel("Initial Angle:")
        self.edtInitialAngle = QSpinBox()
        self.lblAngleLongitude = QLabel("Angle Longitude:")
        self.edtAngleLongitude = QSpinBox()
        self.lblAngleResolution = QLabel("Angle Resolution:")
        self.edtAngleResolution = QDoubleSpinBox()
        self.edtAngleResolution.setSingleStep(0.1)
        self.lblFinalAngle = QLabel("Final Angle:")
        self.edtFinalAngle = QLineEdit()
        self.edtFinalAngle.setReadOnly(True)
        self.lblPointsCurve = QLabel("Points of Curve:")
        self.edtPointsCurve = QLineEdit()
        self.edtPointsCurve.setReadOnly(True)

        self.btnResetValues = QPushButton("Reset")

        self.layoutGrid = QGridLayout(self)

        self.calibrationBoxLayout = QGroupBox("Calibration Parameters")
        self.gainBoxLayout = QGroupBox()
        self.offsetBoxLayout = QGroupBox()
        self.btnCalibrateBoxLayout = QGroupBox()
        self.btnLaserBoxLayout = QGroupBox()

        self.curveBoxLayout = QGroupBox("Curve Performance")

        self.filledBoxLayout_1 = QGroupBox()
        self.filledLayout_2 = QGroupBox()

        self.calibrationLayout = QGridLayout(self)

        self.curveLayout = QGridLayout(self)

        self.gainLayout = QVBoxLayout(self)
        self.offsetLayout = QVBoxLayout(self)
        self.btnCalibrateLayout = QVBoxLayout(self)
        self.btnLaserLayout = QVBoxLayout(self)

        self.gainALayout = QHBoxLayout(self)
        self.gainBLayout = QHBoxLayout(self)
        self.offsetALayout = QHBoxLayout(self)
        self.offsetBLayout = QHBoxLayout(self)

        self.setStyleButtons()
        self.setStyleSpinBox()
        self.setStyleLineEdit()

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setCalibrationGroup(), 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.setLaserGroup(), 0, 2, 1, 1)
        self.layoutGrid.addWidget(self.setCurveGroup(), 1, 0, 1, 2)
        self.layoutGrid.addWidget(self.setFilledGroup_1(), 2, 0, 5, 10)

    def setFilledGroup_1(self):
        self.filledBoxLayout_1.setStyleSheet(style.groupBoxFilled)

        return self.filledBoxLayout_1

    def setFilledGroup_2(self):
        self.filledLayout_2.setStyleSheet(style.groupBoxFilled)

        return self.filledLayout_2

    def setCalibrationGroup(self):
        self.lblGainA.setFixedWidth(50)
        self.lblGainB.setFixedWidth(50)
        self.lblOffsetA.setFixedWidth(50)
        self.lblOffsetB.setFixedWidth(50)
        self.edtGainA.setFixedWidth(100)
        self.edtGainB.setFixedWidth(100)
        self.edtOffsetA.setFixedWidth(100)
        self.edtOffsetB.setFixedWidth(100)

        self.gainALayout.addWidget(self.lblGainA)
        self.gainALayout.addWidget(self.edtGainA)
        self.gainBLayout.addWidget(self.lblGainB)
        self.gainBLayout.addWidget(self.edtGainB)

        self.gainLayout.addLayout(self.gainALayout)
        self.gainLayout.addLayout(self.gainBLayout)

        self.offsetALayout.addWidget(self.lblOffsetA)
        self.offsetALayout.addWidget(self.edtOffsetA)
        self.offsetBLayout.addWidget(self.lblOffsetB)
        self.offsetBLayout.addWidget(self.edtOffsetB)

        self.offsetLayout.addLayout(self.offsetALayout)
        self.offsetLayout.addLayout(self.offsetBLayout)

        self.gainBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.gainBoxLayout.setLayout(self.gainLayout)

        self.offsetBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.offsetBoxLayout.setLayout(self.offsetLayout)

        self.calibrationLayout.addWidget(self.gainBoxLayout, 0, 0)
        self.calibrationLayout.addWidget(self.offsetBoxLayout, 1, 0)
        self.calibrationLayout.addWidget(self.btnCalibrate, 1, 1, 1, 1)

        self.calibrationBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.calibrationBoxLayout.setLayout(self.calibrationLayout)

        return self.calibrationBoxLayout

    def setLaserGroup(self):
        self.btnLaserLayout.addWidget(self.btnLaser, 0, Qt.AlignBottom)

        self.btnLaserBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.btnLaserBoxLayout.setLayout(self.btnLaserLayout)

        return self.btnLaserBoxLayout

    def setCurveGroup(self):
        self.lblInitialAngle.setFixedWidth(100)
        self.lblAngleLongitude.setFixedWidth(100)
        self.lblAngleResolution.setFixedWidth(100)
        self.lblFinalAngle.setFixedWidth(100)
        self.lblPointsCurve.setFixedWidth(100)
        self.edtFinalAngle.setFixedWidth(100)
        self.edtPointsCurve.setFixedWidth(100)

        self.curveLayout.addWidget(self.lblInitialAngle, 0, 0)
        self.curveLayout.addWidget(self.edtInitialAngle, 0, 1)
        self.curveLayout.addWidget(self.lblAngleLongitude, 1, 0)
        self.curveLayout.addWidget(self.edtAngleLongitude, 1, 1)
        self.curveLayout.addWidget(self.lblAngleResolution, 2, 0)
        self.curveLayout.addWidget(self.edtAngleResolution, 2, 1)
        self.curveLayout.addWidget(self.lblFinalAngle, 3, 0)
        self.curveLayout.addWidget(self.edtFinalAngle, 3, 1)
        self.curveLayout.addWidget(self.lblPointsCurve, 4, 0)
        self.curveLayout.addWidget(self.edtPointsCurve, 4, 1)
        self.curveLayout.addWidget(self.btnResetValues, 3, 2, 2, 1)

        self.curveBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.curveBoxLayout.setLayout(self.curveLayout)

        return self.curveBoxLayout

    def setCalibrateDone(self):
        self.btnCalibrate.setStyleSheet(style.buttonCalibrateDone)
        self.btnCalibrate.setChecked(False)

    def setStyleButtons(self):
        self.btnLaser.setStyleSheet(style.buttonLaserSmall)
        self.btnLaser.setCheckable(True)

        self.btnCalibrate.setStyleSheet(style.buttonCalibrate)
        self.btnCalibrate.setCheckable(True)

        self.btnResetValues.setStyleSheet(style.buttonReset)
        self.btnResetValues.setCheckable(True)

    def setStyleSpinBox(self):
        self.edtGainA.setStyleSheet(style.spinBoxGeneral)
        self.edtGainB.setStyleSheet(style.spinBoxGeneral)
        self.edtOffsetA.setStyleSheet(style.spinBoxGeneral)
        self.edtOffsetB.setStyleSheet(style.spinBoxGeneral)
        self.edtInitialAngle.setStyleSheet(style.spinBoxGeneral)
        self.edtAngleLongitude.setStyleSheet(style.spinBoxGeneral)

        self.edtAngleResolution.setStyleSheet(style.doubleSpinBoxGeneral)

    def setStyleLineEdit(self):
        self.edtFinalAngle.setStyleSheet(style.lineEditGeneral)
        self.edtPointsCurve.setStyleSheet(style.lineEditGeneral)

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

