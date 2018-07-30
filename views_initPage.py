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
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox
from PyQt5.QtCore import Qt, QRect


class View(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.btnLaser = QPushButton('Laser OFF')
        # self.btnLaser.setStyleSheet('QPushButton {background-color: green; color: white;}')
        self.btnExit = QPushButton('Exit')
        self.btnData = QPushButton('Data')

        self.layoutGrid = QGridLayout(self)

        self.laserBoxLayout = QGroupBox("Laser Layout")
        self.dataBoxLayout = QGroupBox("Data Layout")
        self.exitBoxLayout = QGroupBox("Exit Layout")

        self.laserLayout = QVBoxLayout(self)
        # self.laserLayout.setGeometry(QRect(0, 0, 1, 2))

        self.dataLayout = QGridLayout(self)

        self.exitLayout = QHBoxLayout(self)

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
        self.layoutGrid.addWidget(self.setDataGroup(), 0, 1, 1, 5)
        self.layoutGrid.addWidget(self.setExitGroup(), 1, 0, 1, 6)

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
        self.laserBoxLayout.setLayout(self.laserLayout)

        return self.laserBoxLayout

    def setDataGroup(self):
        self.dataLayout.addWidget(self.btnData)
        self.dataBoxLayout.setLayout(self.dataLayout)

        return self.dataBoxLayout

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


