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

from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort
from serial.tools.list_ports import comports


class SerialPort:
    def __init__(self):
        self.ports = []
        self.serialData = ""
        self.commands = {
            "CurveTemporal": '|'.encode().hex(),
            "GainOffset": ':'.encode().hex(),
            # "Laser": '#'.encode().hex(),
            "Laser": '#',
            "TimeAverage": '&'.encode().hex(),
            "StopTemporal": '['.encode().hex(),
            "StopTechnical": '.'.encode().hex(),
            "ControlPeris": '*'.encode().hex(),
            "ControlImpulA": '!'.encode().hex(),
            "ControlImpulB": '+'.encode().hex(),
            "BackPeris": '<'.encode().hex(),
            "StopPeris": '='.encode().hex(),
            "ForwardPeris": '>'.encode().hex(),
            "TimePulsesPumps": '_'.encode().hex(),
            "VolumePurge": 'a7',
            "PurgeImpulA": '{'.encode().hex(),
            "PurgeImpulB": '}'.encode().hex(),
            "IAmAlive": '?'.encode().hex(),
            "PowerDown": '/'.encode().hex()
        }

        self.serialPort = QSerialPort()

    def ask_for_port(self):
        """\
        Show a list of ports and ask the user for a choice. To make selection
        easier on systems with long device names, also allow the input of an
        index.
        """
        for n, (port, desc, hwid) in enumerate(sorted(comports()), 1):
            info = {"port": port, "desc": desc, "hwid": hwid}
            self.ports.append(info)

        return self.ports

    def open_port(self, numberOfItem):
        if numberOfItem != 0:
            item = self.ports[numberOfItem - 1]

            self.serialPort.setPortName(item["port"])
            portOpen = self.serialPort.open(QIODevice.ReadWrite)

            if portOpen:
                self.serialPort.setBaudRate(QSerialPort.Baud115200)
                self.serialPort.setDataBits(QSerialPort.Data8)
                self.serialPort.setParity(QSerialPort.NoParity)
                self.serialPort.setStopBits(QSerialPort.OneStop)
                self.serialPort.setFlowControl(QSerialPort.NoFlowControl)

                return True

            else:
                return False

    def close_port(self):
        self.serialPort.close()

    def receive_port(self):
        data = self.serialPort.readAll()
        self.serialData = data.data().decode('utf8')

        return self.serialData

    def write_port(self, data):
        self.serialPort.writeData(data.encode())

    def write_port_list(self, data):
        for value in data:
            self.serialPort.writeData(value.encode())

    def send_I_am_alive(self):
        self.write_port("?")

    def send_Gain_Offset(self, toSend):
        self.write_port(self.commands["GainOffset"])

        for value in toSend:
            self.write_port(f'{value:02x}')

    def send_Control_Impul_A(self, toSend):
        self.write_port(self.commands["ControlImpulA"])

        for value in toSend:
            self.write_port(f'{value:04x}')

    def send_Control_Impul_B(self, toSend):
        self.write_port(self.commands["ControlImpulB"])

        for value in toSend:
            self.write_port(f'{value:04x}')

    def send_Volume_Purges(self, toSend):
        self.write_port(self.commands["VolumePurge"])

        for value in toSend:
            self.write_port(f'{value:04x}')

    def send_Laser(self, toSend):
        self.write_port(self.commands["Laser"])

        self.write_port(f'{toSend:02x}')
