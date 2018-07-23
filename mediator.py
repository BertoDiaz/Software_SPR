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

from controller_connect import ControllerConnect
from controller_initPage import ControllerInit
from PyQt5.QtWidgets import QApplication
import sys


class Mediator:
    def __init__(self):

        self._controllerConnect = ControllerConnect(self)

        # self._controllerInit = ControllerInit(self)

    def finish_ControllerConnection(self):

        self._controllerInit.run()

        self._controllerConnect.close_App()


def main():
    mediator = Mediator()


if __name__ == '__main__':
    # app = QApplication([])
    #
    # window = Mediator()
    # sys.exit(app.exec_())
    main()
