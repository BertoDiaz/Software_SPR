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
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class View(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.btnLaser = QPushButton('Connect')
        self.btnLaser.setCheckable(True)
        self.btnLaser.toggle()
        self.btnExit = QPushButton('Exit')

        self.layout = QVBoxLayout(self)

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layout.addWidget(self.btnLaser)
        self.layout.addWidget(self.btnExit)

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


