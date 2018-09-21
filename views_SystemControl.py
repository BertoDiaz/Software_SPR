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

from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QLabel, QSpinBox, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from lib import Strings
from lib import Styles
import getpass


class ViewSystemControl(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        """---------------------------------------------- QPushButtons ----------------------------------------------"""
        self.btnLaser = QPushButton(Strings.laserStart)
        self.btnPeristaltic = QPushButton(Strings.start)
        self.btnImpulsional_A = QPushButton(Strings.inject)
        self.btnImpulsional_B = QPushButton(Strings.inject)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QLabels -------------------------------------------------"""
        self.lblPeristaltic = QLabel(Strings.flowPeristaltic)
        self.lblImpulsional_A = QLabel(Strings.injectionImpulsionalA)
        self.lblImpulsional_B = QLabel(Strings.injectionImpulsionalB)
        self.lblImageLogo = QLabel(self)
        self.lblImageSPRDevice = QLabel(self)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QSpinBox ------------------------------------------------"""
        self.edtPeristaltic = QSpinBox()
        self.edtImpulsional_A = QSpinBox()
        self.edtImpulsional_B = QSpinBox()
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QPixmap -------------------------------------------------"""
        self.imageLogo = QPixmap(Strings.imageLogoHalf)
        self.imageSPRDevice = QPixmap(Strings.imageSPRDevice)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGroupBoxes -----------------------------------------------"""
        self.laserBoxLayout = QGroupBox(Strings.laserControl)
        self.dataBoxLayout = QGroupBox(Strings.pumpsControl)
        self.imageBoxLayout = QGroupBox()
        self.peristalticBoxLayout = QGroupBox(Strings.peristalticPumpControl)
        self.impulsionalABoxLayout = QGroupBox(Strings.impulsionalPumpAControl)
        self.impulsionalBBoxLayout = QGroupBox(Strings.impulsionalPumpBControl)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGridLayouts ----------------------------------------------"""
        self.layoutGrid = QGridLayout(self)
        self.dataLayout = QGridLayout(self)
        self.peristalticLayout = QGridLayout(self)
        self.impulsionalALayout = QGridLayout(self)
        self.impulsionalBLayout = QGridLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QVBoxLayouts ----------------------------------------------"""
        self.laserLayout = QVBoxLayout(self)
        self.imageLayout = QVBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """--------------------------------------------- Style Functions --------------------------------------------"""
        self.setStyleButtons()
        self.setStyleLabels()
        self.setStyleSpinBox()
        self.setStylePixmap()
        self.setStyleGroupBox()
        self.setStyleLayouts()
        """----------------------------------------------------------------------------------------------------------"""

    def mainWindow(self):
        """Add the main widgets to the main layout.

        Add the group box to the layout of the app.
        """
        self.layoutGrid.addWidget(self.setLaserGroup(), 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.setDataGroup(), 0, 2, 1, 3)
        self.layoutGrid.addWidget(self.setImageGroup(), 0, 7, 1, 1)
        self.layoutGrid.addWidget(self.setImageDeviceGroup(), 1, 0, 9, 10)

    def setLaserGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.laserLayout.addWidget(self.btnLaser, 0, Qt.AlignBottom)

        self.laserBoxLayout.setLayout(self.laserLayout)

        return self.laserBoxLayout

    def setDataGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.peristalticLayout.addWidget(self.lblPeristaltic, 0, 0)
        self.peristalticLayout.addWidget(self.edtPeristaltic, 1, 0)
        self.peristalticLayout.addWidget(self.btnPeristaltic, 0, 1, 2, 1)

        self.impulsionalALayout.addWidget(self.lblImpulsional_A, 0, 0)
        self.impulsionalALayout.addWidget(self.edtImpulsional_A, 1, 0)
        self.impulsionalALayout.addWidget(self.btnImpulsional_A, 0, 1, 2, 1)

        self.impulsionalBLayout.addWidget(self.lblImpulsional_B, 0, 0)
        self.impulsionalBLayout.addWidget(self.edtImpulsional_B, 1, 0)
        self.impulsionalBLayout.addWidget(self.btnImpulsional_B, 0, 1, 2, 1)

        self.peristalticBoxLayout.setLayout(self.peristalticLayout)

        self.impulsionalABoxLayout.setLayout(self.impulsionalALayout)

        self.impulsionalBBoxLayout.setLayout(self.impulsionalBLayout)

        self.dataLayout.addWidget(self.peristalticBoxLayout, 0, 0)
        self.dataLayout.addWidget(self.impulsionalABoxLayout, 0, 1)
        self.dataLayout.addWidget(self.impulsionalBBoxLayout, 0, 2)

        self.dataBoxLayout.setLayout(self.dataLayout)

        return self.dataBoxLayout

    def setImageGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.lblImageLogo.setPixmap(self.imageLogo)

        return self.lblImageLogo

    def setImageDeviceGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.lblImageSPRDevice.setPixmap(self.imageSPRDevice)

        self.imageLayout.addWidget(self.lblImageSPRDevice)

        self.imageBoxLayout.setLayout(self.imageLayout)

        return self.imageBoxLayout

    """
    ********************************************************************************************************************
    *                                              Laser Control Functions                                             *
    ********************************************************************************************************************
    """

    def setBtnLaserStatus(self, status):
        if status:
            text = Strings.laserStop

        else:
            text = Strings.laserStart

        self.btnLaser.setText(text)
        self.btnLaser.setChecked(status)

    def setBtnLaserDisable(self, disable):
        self.btnLaser.setDisabled(disable)

    """
    ********************************************************************************************************************
    *                                            End Laser Control Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                           Peristaltic Control Functions                                          *
    ********************************************************************************************************************
    """

    def setBtnPeristalticStatus(self, status):
        if status:
            text = Strings.stop

        else:
            text = Strings.start

        self.btnPeristaltic.setText(text)
        self.btnPeristaltic.setChecked(status)

    def getBtnPeristalticStatus(self):
        return self.btnPeristaltic.isChecked()

    def setBtnPeristalticDisable(self, disable):
        self.btnPeristaltic.setDisabled(disable)

    def setEdtPeristalticValue(self, value):
        self.edtPeristaltic.setValue(value)

    def getEdtPeristalticValue(self):
        return self.edtPeristaltic.value()

    """
    ********************************************************************************************************************
    *                                         End Peristaltic Control Functions                                        *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Impulsional A Control Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnImpulsionalAStatus(self, status):
        self.btnImpulsional_A.setChecked(status)
        self.setBtnImpulsionalADisable(status)

    def getBtnImpulsionalAStatus(self):
        return self.btnImpulsional_A.isChecked()

    def setBtnImpulsionalADisable(self, disable):
        self.btnImpulsional_A.setDisabled(disable)

    def setEdtImpulsionalAValue(self, value):
        self.edtImpulsional_A.setValue(value)

    def getEdtImpulsionalAValue(self):
        return self.edtImpulsional_A.value()

    """
    ********************************************************************************************************************
    *                                        End Impulsional A Control Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                          Impulsional B Control Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnImpulsionalBStatus(self, status):
        self.btnImpulsional_B.setChecked(status)
        self.setBtnImpulsionalBDisable(status)

    def getBtnImpulsionalBStatus(self):
        return self.btnImpulsional_B.isChecked()

    def setBtnImpulsionalBDisable(self, disable):
        self.btnImpulsional_B.setDisabled(disable)

    def setEdtImpulsionalBValue(self, value):
        self.edtImpulsional_B.setValue(value)

    def getEdtImpulsionalBValue(self):
        return self.edtImpulsional_B.value()

    """
    ********************************************************************************************************************
    *                                        End Impulsional B Control Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Buttons Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleButtons(self):
        self.btnLaser.setStyleSheet(Styles.buttonLaserBig)
        self.btnLaser.setCheckable(True)

        self.btnPeristaltic.setStyleSheet(Styles.buttonPeristaltic)
        self.btnPeristaltic.setCheckable(True)

        self.btnImpulsional_A.setStyleSheet(Styles.buttonImpulsional)
        self.btnImpulsional_A.setCheckable(True)

        self.btnImpulsional_B.setStyleSheet(Styles.buttonImpulsional)
        self.btnImpulsional_B.setCheckable(True)

    """
    ********************************************************************************************************************
    *                                           End Buttons Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Labels Styles Functions                                              *
    ********************************************************************************************************************
    """

    def setStyleLabels(self):
        self.lblPeristaltic.setFixedWidth(100)
        self.lblPeristaltic.setAlignment(Qt.AlignBottom)

        self.lblImpulsional_A.setFixedWidth(100)
        self.lblImpulsional_A.setAlignment(Qt.AlignBottom)

        self.lblImpulsional_B.setFixedWidth(100)
        self.lblImpulsional_B.setAlignment(Qt.AlignBottom)

    """
    ********************************************************************************************************************
    *                                           End Labels Styles Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Spin Boxes Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setStyleSpinBox(self):
        self.edtPeristaltic.setStyleSheet(Styles.spinBoxGeneral)
        self.edtPeristaltic.setRange(0, 100)

        self.edtImpulsional_A.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_A.setRange(0, 100)

        self.edtImpulsional_B.setStyleSheet(Styles.spinBoxGeneral)
        self.edtImpulsional_B.setRange(0, 100)

    """
    ********************************************************************************************************************
    *                                          End Spin Boxes Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Pixmap Styles Functions                                              *
    ********************************************************************************************************************
    """

    def setStylePixmap(self):
        self.imageLogo = self.imageLogo.scaledToHeight(100)

        self.imageSPRDevice = self.imageSPRDevice.scaledToHeight(500)

    """
    ********************************************************************************************************************
    *                                           End Pixmap Styles Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Group Box Styles Functions                                            *
    ********************************************************************************************************************
    """

    def setStyleGroupBox(self):
        self.laserBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.peristalticBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.impulsionalABoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.impulsionalBBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.dataBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.imageBoxLayout.setStyleSheet(Styles.groupBoxGeneralWithoutBorder)

    """
    ********************************************************************************************************************
    *                                          End Group Box Styles Functions                                          *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Layouts Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleLayouts(self):
        self.imageLayout.setAlignment(Qt.AlignCenter)

    """
    ********************************************************************************************************************
    *                                           End Layouts Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                Messages Functions                                                *
    ********************************************************************************************************************
    """

    def setMessageCritical(self, message):
        QMessageBox.critical(self, Strings.error, message, QMessageBox.Ok, QMessageBox.Ok)

    def setMessageExistsFile(self):
        loadFile = QMessageBox.question(self, Strings.question, Strings.messageLoadConfigurationFile,
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if loadFile == QMessageBox.Yes:
            fileName, _ = QFileDialog.getOpenFileName(self, Strings.openFile, 'C:/Users/' + getpass.getuser() +
                                                      '/Documents/', 'Config File(*.cfg)')

            return [True, fileName]

        else:
            return [False, None]

    """
    ********************************************************************************************************************
    *                                              End Messages Functions                                              *
    ********************************************************************************************************************
    """
