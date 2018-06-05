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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox


class View(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.btnOpen = QPushButton('Connect')
        self.btnClose = QPushButton('Disconnect')
        self.btnClose.setDisabled(True)
        self.combo = QComboBox()

        layout = QVBoxLayout(self)
        layout.addWidget(self.btnOpen)
        layout.addWidget(self.btnClose)
        layout.addWidget(self.combo)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')

    def setPorts(self, ports):
        self.combo.addItem("PORTS")

        for port in ports:
            self.combo.addItem(port["port"])

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)
