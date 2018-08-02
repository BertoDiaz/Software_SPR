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
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit
from PyQt5.QtCore import Qt, QRect


class ViewCurveSetup(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.labelGainA = QLabel("Gain A:")
        self.editGainA = QLineEdit()
        self.labelGainB = QLabel("Gain B:")
        self.editGainB = QLineEdit()
        self.labelOffsetA = QLabel("Offset A:")
        self.editOffsetA = QLineEdit()
        self.labelOffsetB = QLabel("Offset B:")
        self.editOffsetB = QLineEdit()

        self.layoutGrid = QGridLayout(self)

        self.calibrationBoxLayout = QGroupBox("Calibration Parameters")
        self.gainBoxLayout = QGroupBox()
        self.offsetBoxLayout = QGroupBox()
        self.filledBoxLayout_1 = QGroupBox()
        self.filledLayout_2 = QGroupBox()

        self.calibrationLayout = QGridLayout(self)

        self.gainLayout = QVBoxLayout(self)
        self.offsetLayout = QVBoxLayout(self)

        self.gainALayout = QHBoxLayout(self)
        self.gainBLayout = QHBoxLayout(self)
        self.offsetALayout = QHBoxLayout(self)
        self.offsetBLayout = QHBoxLayout(self)

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
        self.layoutGrid.addWidget(self.setFilledGroup_1(), 1, 0, 5, 10)

    def setFilledGroup_1(self):
        self.filledBoxLayout_1.setStyleSheet("QGroupBox {"
                                             "border: 2px solid red;"
                                             "}")

        return self.filledBoxLayout_1

    def setFilledGroup_2(self):
        self.filledLayout_2.setStyleSheet("QGroupBox {"
                                          "border: 2px solid red;"
                                          "}")

        return self.filledLayout_2

    def setCalibrationGroup(self):
        self.labelGainA.setFixedWidth(50)
        self.labelGainB.setFixedWidth(50)
        self.labelOffsetA.setFixedWidth(50)
        self.labelOffsetB.setFixedWidth(50)
        self.editGainA.setFixedWidth(100)
        self.editGainB.setFixedWidth(100)
        self.editOffsetA.setFixedWidth(100)
        self.editOffsetB.setFixedWidth(100)

        self.gainALayout.addWidget(self.labelGainA)
        self.gainALayout.addWidget(self.editGainA)
        self.gainBLayout.addWidget(self.labelGainB)
        self.gainBLayout.addWidget(self.editGainB)

        self.gainLayout.addLayout(self.gainALayout)
        self.gainLayout.addLayout(self.gainBLayout)

        self.offsetALayout.addWidget(self.labelOffsetA)
        self.offsetALayout.addWidget(self.editOffsetA)
        self.offsetBLayout.addWidget(self.labelOffsetB)
        self.offsetBLayout.addWidget(self.editOffsetB)

        self.offsetLayout.addLayout(self.offsetALayout)
        self.offsetLayout.addLayout(self.offsetBLayout)

        self.gainBoxLayout.setStyleSheet("QGroupBox {"
                                         "border: 2px outset #948682;"
                                         "border-radius: 5px;"
                                         "margin-top: 7px;"
                                         "}"
                                         "QGroupBox:title {"
                                         "top: -7 ex;"
                                         "left: 10px;"
                                         "}")
        self.gainBoxLayout.setLayout(self.gainLayout)

        self.offsetBoxLayout.setStyleSheet("QGroupBox {"
                                           "border: 2px outset #948682;"
                                           "border-radius: 5px;"
                                           "margin-top: 7px;"
                                           "}"
                                           "QGroupBox:title {"
                                           "top: -7 ex;"
                                           "left: 10px;"
                                           "}")
        self.offsetBoxLayout.setLayout(self.offsetLayout)

        self.calibrationLayout.addWidget(self.gainBoxLayout, 0, 0)
        self.calibrationLayout.addWidget(self.offsetBoxLayout, 1, 0)

        self.calibrationBoxLayout.setStyleSheet("QGroupBox {"
                                                "border: 2px outset #948682;"
                                                "border-radius: 5px;"
                                                "margin-top: 7px;"
                                                "}"
                                                "QGroupBox:title {"
                                                "top: -7 ex;"
                                                "left: 10px;"
                                                "}")
        self.calibrationBoxLayout.setLayout(self.calibrationLayout)

        return self.calibrationBoxLayout
