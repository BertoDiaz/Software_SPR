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
from PyQt5.QtWidgets import QDesktopWidget, QDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class View(QDialog):

    def __init__(self, parent):
        super().__init__(parent)

        """Put the dialog window on top and block all windows."""
        self.setWindowModality(Qt.ApplicationModal)

        self.progressBar = QProgressBar(self)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setValue(0)

        self.btnOpen = QPushButton('Connect')
        self.btnClose = QPushButton('Disconnect')
        self.btnClose.setDisabled(True)
        self.btnExit = QPushButton('Exit')
        self.combo = QComboBox()

        self.textConnected = QLabel("Port Connected")
        self.textConnected.setAlignment(Qt.AlignCenter)
        self.textConnected.setFont(QFont("Times", 8, QFont.Bold))

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.progressBar)

        self.resize(300, 200)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self, connected, byConnectButton):
        if byConnectButton == 0:
            self.layout.removeWidget(self.progressBar)
            self.progressBar.deleteLater()

        elif byConnectButton == 1:
            self.layout.removeWidget(self.btnOpen)
            self.btnOpen.deleteLater()
            self.layout.removeWidget(self.btnClose)
            self.btnClose.deleteLater()
            self.layout.removeWidget(self.btnExit)
            self.btnExit.deleteLater()
            self.layout.removeWidget(self.combo)
            self.combo.deleteLater()

        if connected:
            self.textConnected.setText("Port Connected")
            self.textConnected.setStyleSheet('color: green')
            self.layout.addWidget(self.textConnected)

        else:
            self.textConnected.setText("Port do not found, please choose an available port.")
            self.textConnected.setStyleSheet('color: red')
            self.layout.addWidget(self.textConnected)
            self.layout.addWidget(self.btnOpen)
            self.layout.addWidget(self.btnClose)
            self.layout.addWidget(self.btnExit)
            self.layout.addWidget(self.combo)

    def setPorts(self, ports):
        self.combo.addItem("PORTS")

        for port in ports:
            self.combo.addItem(port["port"])

    def setPortFound(self, numberOfIndex):
        self.btnClose.setDisabled(False)
        self.btnOpen.setDisabled(True)
        self.combo.setCurrentIndex(numberOfIndex)
        self.combo.setDisabled(True)

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

    def setMessageExistsFile(self):
        loadFile = QMessageBox.question(self, "Question", "Load a configuration file?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if loadFile == QMessageBox.Yes:
            fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "/home", "*.cfg")

            if fileName:
                return [True, fileName]

            else:
                return [False, None]

        else:
            return [False, 'No']

    def setMessageExit(self):
        exitApp = QMessageBox.question(self, "Question", "Are you sure you want to quit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False

