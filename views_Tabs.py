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
from lib import Strings


class ViewTabs(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.btnExit = QPushButton(Strings.exitLC)

        self.tabs = QTabWidget(self)
        self.tab_SystemControl = ViewSystemControl(None)
        self.tab_CurveSetup = ViewCurveSetup(None)
        self.tab_DataAcquisition = ViewDataAcquisition(None)

        self.tabs.addTab(self.tab_SystemControl, Strings.systemControl)
        self.tabs.addTab(self.tab_CurveSetup, Strings.sprCurveSetup)
        self.tabs.addTab(self.tab_DataAcquisition, Strings.dataAcquisition)

        width, height = self.calculateSizeWindow()

        self.resize(width, height)
        self.centerWindowOnScreen()
        self.setWindowTitle(Strings.sprV2)

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    @staticmethod
    def calculateSizeWindow():
        widthWindow = QDesktopWidget().availableGeometry().width()
        heightWindow = QDesktopWidget().availableGeometry().height()

        widthApp = widthWindow * 0.7
        heightApp = heightWindow * 0.8

        return widthApp, heightApp

    def mainWindow(self):
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.btnExit)

    def setMessageExit(self):
        exitApp = QMessageBox.question(self, Strings.question, Strings.messageExit, QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False
