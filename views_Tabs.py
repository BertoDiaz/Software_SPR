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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtWidgets import QDesktopWidget, QTabWidget
from views_SystemControl import ViewSystemControl
from views_CurveSetup import ViewCurveSetup
from views_DataAcquisition import ViewDataAcquisition


class ViewTabs(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.btnExit = QPushButton('Exit')

        self.tabs = QTabWidget(self)
        self.tab_SystemControl = ViewSystemControl(None)
        self.tab_CurveSetup = ViewCurveSetup(None)
        self.tab_DataAcquisition = ViewDataAcquisition(None)

        self.tabs.addTab(self.tab_SystemControl, "System Control")
        self.tabs.addTab(self.tab_CurveSetup, "SPR Curve Setup")
        self.tabs.addTab(self.tab_DataAcquisition, "Data Acquisition")

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.btnExit)

    def setMessageExit(self):
        exitApp = QMessageBox.question(self, "Question", "Are you sure you want to quit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False
