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

        self.calibrationLayout = QVBoxLayout(self)
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
        self.layoutGrid.addWidget(self.setCalibrationGroup(), 0, 0)

    def setLaserGroup(self):
        self.btnLaser.setStyleSheet(
            'QPushButton {'
            'font: bold;'
            'background-color: green;'
            'color: white;'
            'font-size: 20px;'
            'height:100px;'
            'width: 20px;'
            '}')
        self.laserLayout.addWidget(self.btnLaser, 0, Qt.AlignBottom)

        """
            Different border style:
                - dotted
                - dashed
                - solid
                - double
                - groove
                - ridge
                - inset
                - outset
                - none
                - hidden
        """

        self.laserBoxLayout.setStyleSheet("QGroupBox {"
                                          "border: 2px outset #948682;"
                                          "border-radius: 5px;"
                                          "margin-top: 7px;"
                                          "}"
                                          "QGroupBox:title {"
                                          "top: -7 ex;"
                                          "left: 10px;"
                                          "}")
        self.laserBoxLayout.setLayout(self.laserLayout)

        return self.laserBoxLayout

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
        self.gainLayout.setAlignment(Qt.AlignLeft)
        self.gainLayout.setAlignment(Qt.AlignTop)

        self.offsetALayout.addWidget(self.labelOffsetA)
        self.offsetALayout.addWidget(self.editOffsetA)
        self.offsetBLayout.addWidget(self.labelOffsetB)
        self.offsetBLayout.addWidget(self.editOffsetB)

        self.offsetLayout.addLayout(self.offsetALayout)
        self.offsetLayout.addLayout(self.offsetBLayout)
        self.offsetLayout.setAlignment(Qt.AlignLeft)
        self.offsetLayout.setAlignment(Qt.AlignTop)

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

        self.calibrationLayout.addWidget(self.gainBoxLayout)
        self.calibrationLayout.addWidget(self.offsetBoxLayout)

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

    def setExitGroup(self):
        self.exitLayout.addWidget(self.btnExit)
        self.exitBoxLayout.setLayout(self.exitLayout)

        return self.exitBoxLayout

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

    def setMessageExistsFile(self):
        loadFile = QMessageBox.question(self, "Question", "Load a configuration file?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if loadFile == QMessageBox.Yes:
            fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "/home", "*.cfg")

            return [True, fileName]

        else:
            return [False, None]

    def setMessageExit(self):
        exitApp = QMessageBox.question(self, "Question", "Are you sure you want to quit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False


