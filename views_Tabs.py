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

from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QDesktopWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QColor
from views_SystemControl import ViewSystemControl
from views_CurveSetup import ViewCurveSetup
from views_DataAcquisition import ViewDataAcquisition
from lib import Strings
from lib import Styles


class ViewTabs(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#D8D8D8'))
        self.setPalette(p)

        """---------------------------------------------- QPushButtons ----------------------------------------------"""
        self.btnExit = QPushButton(Strings.exitLC)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QVBoxLayout -----------------------------------------------"""
        self.layout = QVBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """----------------------------------------------- QTabWidget -----------------------------------------------"""
        self.tabs = QTabWidget(self)
        self.tab_SystemControl = ViewSystemControl(None)
        self.tab_CurveSetup = ViewCurveSetup(None)
        self.tab_DataAcquisition = ViewDataAcquisition(None)

        self.tabs.setStyleSheet(Styles.qTabBar)

        self.tabs.addTab(self.tab_SystemControl, Strings.systemControl)
        self.tabs.addTab(self.tab_CurveSetup, Strings.sprCurveSetup)
        self.tabs.addTab(self.tab_DataAcquisition, Strings.dataAcquisition)
        """----------------------------------------------------------------------------------------------------------"""

        width, height = self.calculateSizeWindow()

        self.resize(width, height)
        self.centerWindowOnScreen()
        self.setWindowTitle(Strings.sprV2)

    def centerWindowOnScreen(self):
        """Center the window of the app on the screen.

        Get the geometry of the app window, then, calculate the center of the screen and move the app window to the
        center of the screen.
        """
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    @staticmethod
    def calculateSizeWindow():
        """Calculate the size of the app window.

        Get the width and height of the screen and set the width of the app window to the 70% of the screen and the
        height to 80%.

        Returns:
            list: the width and height of the app window.
        """
        widthWindow = QDesktopWidget().availableGeometry().width()
        heightWindow = QDesktopWidget().availableGeometry().height()

        widthApp = widthWindow * 0.7
        heightApp = heightWindow * 0.8

        return widthApp, heightApp

    def mainWindow(self):
        """Add the main widgets to the main layout.

        Add the tabs of the app and the exit button to the layout of the app.
        """
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.btnExit)

    def setMessageExit(self):
        """Show a dialog with a question.

        Create a dialog with the question to exit of the app.

        Returns:
            bool: True, if the answer to the question is Yes, and False in the opposite case.
        """
        exitApp = QMessageBox.question(self, Strings.question, Strings.messageExit, QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False
