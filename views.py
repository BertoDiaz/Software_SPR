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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox, QProgressBar, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class View(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # self.splash = QSplashScreen(self, QPixmap(), Qt.WindowStaysOnTopHint)

        # self.progressBar = QProgressBar(self.splash)
        self.progressBar = QProgressBar(self)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.btnOpen = QPushButton('Connect')
        self.btnClose = QPushButton('Disconnect')
        self.btnClose.setDisabled(True)
        self.combo = QComboBox()
        self.textConnected = QLabel("Port Connected")
        self.textConnected.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.progressBar)
        # layout.addWidget(self.btnOpen)
        # layout.addWidget(self.btnClose)
        # layout.addWidget(self.combo)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')

    def mainWindow(self, connected):
        self.layout.removeWidget(self.progressBar)
        self.progressBar.deleteLater()

        if connected:
            self.textConnected.setStyleSheet('color: green')
            self.layout.addWidget(self.textConnected)

        else:
            self.textConnected.setText("Port do not found, please choose an available port.")
            self.textConnected.setFont(QFont("Times", 8, QFont.Bold))
            self.textConnected.setStyleSheet('color: red')
            self.layout.addWidget(self.textConnected)
            self.layout.addWidget(self.btnOpen)
            self.layout.addWidget(self.btnClose)
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
