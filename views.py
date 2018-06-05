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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox, QApplication
from PyQt5.QtSerialPort import QSerialPort
from SerialPort import SerialPort
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.numberOfItem = 0
        self.item = {}
        self.connected = False
        self.portOpen = None
        self.editData = None
        self.serialData = ''

        self.btnOpen = QPushButton('Connect')
        self.btnClose = QPushButton('Disconnect')
        self.btnClose.setDisabled(True)
        self.combo = QComboBox()

        self.serialPort = QSerialPort()

        self.ports = SerialPort.ask_for_port(self)

        self.combo.addItem("PORTS")

        for port in self.ports:
            self.combo.addItem(port["port"])

        layout = QVBoxLayout(self)
        layout.addWidget(self.btnOpen)
        layout.addWidget(self.btnClose)
        layout.addWidget(self.combo)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')

        self.run()

    def run(self):

        self.combo.activated.connect(self.onActivated)
        self.btnOpen.clicked.connect(self.open_port)
        self.btnClose.clicked.connect(self.close_port)

        self.show()

    def onActivated(self, numberItem):
        self.numberOfItem = numberItem

    def open_port(self):
        if SerialPort.open_port(self):
            self.btnOpen.setDisabled(True)
            self.btnClose.setDisabled(False)

            self.serialPort.readyRead.connect(SerialPort.receive_port)

            SerialPort.write_port(self)

        else:
            QMessageBox.critical(self, "Error", "Port cannot be opened")

    def close_port(self):
        SerialPort.close_port(self)
        self.btnClose.setDisabled(True)
        self.btnOpen.setDisabled(False)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    sys.exit(app.exec_())
