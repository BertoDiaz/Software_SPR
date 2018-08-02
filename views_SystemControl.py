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


class ViewSystemControl(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.btnLaser = QPushButton('Laser OFF')
        # self.btnExit = QPushButton('Exit')

        self.labelPeristaltic = QLabel("Flow Peristaltic")
        self.editPeristaltic = QLineEdit()
        self.labelImpulsional_A = QLabel("Injection Impulsional A:")
        self.editImpulsional_A = QLineEdit()
        self.labelImpulsional_B = QLabel("Injection Impulsional B:")
        self.editImpulsional_B = QLineEdit()

        self.layoutGrid = QGridLayout(self)

        self.laserBoxLayout = QGroupBox("Laser Control")
        self.dataBoxLayout = QGroupBox("Data Layout")
        self.otherBoxLayout = QGroupBox("Other Layout")
        self.peristalticBoxLayout = QGroupBox("Peristaltic Pump Control")
        self.impulsionalABoxLayout = QGroupBox("Impulsional Pump A Control")
        self.impulsionalBBoxLayout = QGroupBox("Impulsional Pump B Control")

        self.laserLayout = QVBoxLayout(self)
        self.dataLayout = QGridLayout(self)
        self.peristalticLayout = QVBoxLayout(self)
        self.impulsionalALayout = QVBoxLayout(self)
        self.impulsionalBLayout = QVBoxLayout(self)
        self.otherLayout = QHBoxLayout(self)

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setLaserGroup(), 0, 0)
        self.layoutGrid.addWidget(self.setDataGroup(), 0, 1, 1, 3)
        self.layoutGrid.addWidget(self.setOtherGroup(), 1, 0, 5, 6)

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

    def setDataGroup(self):
        # self.dataLayout.setAlignment(Qt.AlignLeft)

        self.labelPeristaltic.setFixedWidth(100)
        self.labelImpulsional_A.setFixedWidth(100)
        self.labelImpulsional_B.setFixedWidth(100)
        self.editPeristaltic.setFixedWidth(100)
        self.editImpulsional_A.setFixedWidth(100)
        self.editImpulsional_B.setFixedWidth(100)

        # self.dataLayout.addWidget(self.labelPeristaltic, 0, 0,)
        # self.dataLayout.addWidget(self.editPeristaltic, 0, 1)
        # self.dataLayout.addWidget(self.labelImpulsional_A, 1, 0)
        # self.dataLayout.addWidget(self.editImpulsional_A, 1, 1)
        # self.dataLayout.addWidget(self.labelImpulsional_B, 2, 0)
        # self.dataLayout.addWidget(self.editImpulsional_B, 2, 1)

        self.peristalticLayout.addWidget(self.labelPeristaltic)
        self.peristalticLayout.addWidget(self.editPeristaltic)

        self.impulsionalALayout.addWidget(self.labelImpulsional_A)
        self.impulsionalALayout.addWidget(self.editImpulsional_A)

        self.impulsionalBLayout.addWidget(self.labelImpulsional_B)
        self.impulsionalBLayout.addWidget(self.editImpulsional_B)

        self.peristalticBoxLayout.setStyleSheet("QGroupBox {"
                                                "border: 2px outset #948682;"
                                                "border-radius: 5px;"
                                                "margin-top: 7px;"
                                                "}"
                                                "QGroupBox:title {"
                                                "top: -7 ex;"
                                                "left: 10px;"
                                                "}")
        self.peristalticBoxLayout.setLayout(self.peristalticLayout)

        self.impulsionalABoxLayout.setStyleSheet("QGroupBox {"
                                                 "border: 2px outset #948682;"
                                                 "border-radius: 5px;"
                                                 "margin-top: 7px;"
                                                 "}"
                                                 "QGroupBox:title {"
                                                 "top: -7 ex;"
                                                 "left: 10px;"
                                                 "}")
        self.impulsionalABoxLayout.setLayout(self.impulsionalALayout)

        self.impulsionalBBoxLayout.setStyleSheet("QGroupBox {"
                                                 "border: 2px outset #948682;"
                                                 "border-radius: 5px;"
                                                 "margin-top: 7px;"
                                                 "}"
                                                 "QGroupBox:title {"
                                                 "top: -7 ex;"
                                                 "left: 10px;"
                                                 "}")
        self.impulsionalBBoxLayout.setLayout(self.impulsionalBLayout)

        self.dataLayout.addWidget(self.peristalticBoxLayout, 0, 0)
        self.dataLayout.addWidget(self.impulsionalABoxLayout, 0, 1)
        self.dataLayout.addWidget(self.impulsionalBBoxLayout, 0, 2)

        self.dataBoxLayout.setStyleSheet("QGroupBox {"
                                         "border: 2px outset #948682;"
                                         "border-radius: 5px;"
                                         "margin-top: 7px;"
                                         "}"
                                         "QGroupBox:title {"
                                         "top: -7 ex;"
                                         "left: 10px;"
                                         "}")
        self.dataBoxLayout.setLayout(self.dataLayout)

        return self.dataBoxLayout

    def setOtherGroup(self):
        # self.otherLayout.addWidget(self.btnExit)
        self.otherBoxLayout.setLayout(self.otherLayout)

        return self.otherBoxLayout

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
