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

from views import View
from SerialPort import SerialPort
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from time import sleep
import sys
import codecs


class Controller:
    def __init__(self):
        self.portCOM = "COM4"
        self.numberOfItem = 0
        self.ports = []
        self.bufferReceive = ""
        self.connected = False
        self.progressBarValue = 0

        self.dataInit = {
            'PortNum': 0,
            'Gain1': 0,
            'Offset1': 0,
            'Gain2': 0,
            'Offset2': 0,
            'Impul1': 50,
            'DC1': 50,
            'PER1': 400,
            'Impul2': 50,
            'DC2': 50,
            'PER2': 400,
            'PURG1': 1000,
            'PURG2': 1000,
            'N_SERIE_SPR': "None"
        }

        self.serialPort = SerialPort()

        self.timer_disconnect_I_am_alive = QTimer()
        self.timer_send_I_am_alive = QTimer()

        self.view = View(None)
        self.ports = self.serialPort.ask_for_port()
        self.view.setPorts(self.ports)

        self.view.show()

        self.connect_USB()

    def connect_USB(self):
        port_found = []

        for foundCount in range(0, 5):

            port_found = self.find_port(foundCount)

            if port_found[0]:

                addValue = (80 - self.progressBarValue) / 5

                for i in range(0, 5):
                    self.progressBarValue = self.progressBarValue + addValue
                    self.load_progress_bar()

                self.connected = self.serialPort.open_port(port_found[1])
                self.view.setPortFound(port_found[1])

                self.serialPort.serialPort.readyRead.connect(self.receive_I_am_alive)

                self.numberOfItem = port_found[1]

                self.serialPort.send_I_am_alive()

                self.timer_disconnect_I_am_alive.timeout.connect(self.disconnect_receive_I_am_alive)
                self.timer_disconnect_I_am_alive.start(10000)

                self.timer_send_I_am_alive.timeout.connect(self.send_I_am_alive)
                self.timer_send_I_am_alive.start(1000)

                break

            sleep(2)

        if not port_found[0]:
            self.view.mainWindow(self.connected)

    def onActivated(self, numberItem):
        self.numberOfItem = numberItem

    def open_port(self):
        if self.serialPort.open_port(self.numberOfItem):
            self.view.btnOpen.setDisabled(True)
            self.view.btnClose.setDisabled(False)
            self.view.combo.setDisabled(True)

            self.serialPort.write_port("?")

        else:
            self.view.setMessageCritical("Error", "Port cannot be opened")

    def close_port(self):
        self.view.btnOpen.setDisabled(False)
        self.view.btnClose.setDisabled(True)
        self.view.combo.setDisabled(False)

        self.connected = False

        self.serialPort.close_port()

    def receive_port(self):
        self.bufferReceive = self.serialPort.receive_port()

    def receive_I_am_alive(self):
        while self.bufferReceive != "@":
            self.bufferReceive = self.serialPort.receive_port()

        self.timer_send_I_am_alive.stop()
        self.timer_disconnect_I_am_alive.stop()
        self.serialPort.serialPort.readyRead.disconnect(self.receive_I_am_alive)
        self.serialPort.serialPort.readyRead.connect(self.receive_port)

        addValue = (100 - self.progressBarValue) / 5

        for i in range(0, 5):
            self.progressBarValue = self.progressBarValue + addValue
            self.load_progress_bar()

        self.view.mainWindow(self.connected)

        self.load_file()

    def disconnect_receive_I_am_alive(self):
        self.timer_disconnect_I_am_alive.stop()
        self.timer_send_I_am_alive.stop()
        self.serialPort.serialPort.readyRead.disconnect(self.receive_I_am_alive)
        self.close_port()
        sleep(1)
        self.view.mainWindow(self.connected)

        self.view.combo.activated.connect(self.onActivated)
        self.view.btnOpen.clicked.connect(self.open_port)
        self.view.btnClose.clicked.connect(self.close_port)

    def send_I_am_alive(self):
        self.serialPort.send_I_am_alive()
        self.progressBarValue = self.progressBarValue + 2
        self.load_progress_bar()

    def find_port(self, foundCount):
        port_found = []
        i = 1
        found = False

        for port in self.ports:
            if port['port'] == self.portCOM:
                port_found.append(True)
                port_found.append(i)
                found = True

            self.progressBarValue = self.progressBarValue + foundCount + i
            self.load_progress_bar()
            i += 1

        if not found:
            port_found.append(False)
            port_found.append(0)

        return port_found

    def load_progress_bar(self):
        self.view.progressBar.setValue(self.progressBarValue)
        QApplication.processEvents()
        sleep(0.2)

    def load_file(self):
        numPortNum = 1
        numGain1 = 4
        numOffset1 = 5
        numGain2 = 6
        numOffset2 = 7
        numImpul1 = 8
        numDC1 = 9
        numPer1 = 10
        numImpul2 = 11
        numDC2 = 12
        numPer2 = 13
        numPurg1 = 14
        numPurg2 = 15
        num_n_serie_spr = 16

        loadFile = self.view.setMessageExistsFile()

        if loadFile[0]:
            print("Yes")
            print(loadFile[1])
            fileConfig = codecs.open(loadFile[1], 'r', encoding='utf-8')

            fileConfig_rows = fileConfig.readlines()

            print(self.dataInit)

            self.dataInit['PortNum'] = int(fileConfig_rows[numPortNum][fileConfig_rows[numPortNum].find('=') + 2:
                                                                       len(fileConfig_rows[numPortNum]) - 2])

            self.dataInit['Gain1'] = int(fileConfig_rows[numGain1][fileConfig_rows[numGain1].find('=') + 2:
                                                                   len(fileConfig_rows[numGain1]) - 2])

            self.dataInit['Offset1'] = int(fileConfig_rows[numOffset1][fileConfig_rows[numOffset1].find('=') + 2:
                                                                       len(fileConfig_rows[numOffset1]) - 2])

            self.dataInit['Gain2'] = int(fileConfig_rows[numGain2][fileConfig_rows[numGain2].find('=') + 2:
                                                                   len(fileConfig_rows[numGain2]) - 2])

            self.dataInit['Offset2'] = int(fileConfig_rows[numOffset2][fileConfig_rows[numOffset2].find('=') + 2:
                                                                       len(fileConfig_rows[numOffset2]) - 2])

            self.dataInit['Impul1'] = int(fileConfig_rows[numImpul1][fileConfig_rows[numImpul1].find('=') + 2:
                                                                     len(fileConfig_rows[numImpul1]) - 2])

            self.dataInit['DC1'] = int(fileConfig_rows[numDC1][fileConfig_rows[numDC1].find('=') + 2:
                                                               len(fileConfig_rows[numDC1]) - 2])

            self.dataInit['PER1'] = int(fileConfig_rows[numPer1][fileConfig_rows[numPer1].find('=') + 2:
                                                                 len(fileConfig_rows[numPer1]) - 2])

            self.dataInit['Impul2'] = int(fileConfig_rows[numImpul2][fileConfig_rows[numImpul2].find('=') + 2:
                                                                     len(fileConfig_rows[numImpul2]) - 2])

            self.dataInit['DC2'] = int(fileConfig_rows[numDC2][fileConfig_rows[numDC2].find('=') + 2:
                                                               len(fileConfig_rows[numDC2]) - 2])

            self.dataInit['PER2'] = int(fileConfig_rows[numPer2][fileConfig_rows[numPer2].find('=') + 2:
                                                                 len(fileConfig_rows[numPer2]) - 2])

            self.dataInit['PURG1'] = int(fileConfig_rows[numPurg1][fileConfig_rows[numPurg1].find('=') + 2:
                                                                   len(fileConfig_rows[numPurg1]) - 2])

            self.dataInit['PURG2'] = int(fileConfig_rows[numPurg2][fileConfig_rows[numPurg2].find('=') + 2:
                                                                   len(fileConfig_rows[numPurg2]) - 2])

            self.dataInit['N_SERIE_SPR'] = str(fileConfig_rows[num_n_serie_spr][fileConfig_rows[num_n_serie_spr].
                                               find('=') + 3:len(fileConfig_rows[num_n_serie_spr]) - 1])

            print(self.dataInit)

        else:
            print("No")


if __name__ == '__main__':
    app = QApplication([])

    window = Controller()
    sys.exit(app.exec_())
