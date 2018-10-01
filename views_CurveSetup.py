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

from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QSpinBox, QDoubleSpinBox, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QPixmap, QColor
from lib.LedIndicatorWidget import LedIndicator
from lib.Chart import Chart
from lib import Strings
from lib import Styles
import getpass


class ViewCurveSetup(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        """---------------------------------------------- QPushButtons ----------------------------------------------"""
        self.btnCalibrate = QPushButton(Strings.calibrate)
        self.btnLaser = QPushButton(Strings.laserStart)
        self.btnReset = QPushButton(Strings.reset)
        self.btnAutoAcquisition = QPushButton(Strings.automatic)
        self.btnSaveFile = QPushButton(Strings.saveFileUC)
        """----------------------------------------------------------------------------------------------------------"""

        """--------------------------------------------- Led Indicator ----------------------------------------------"""
        self.ledLaser = LedIndicator(self)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QLabels -------------------------------------------------"""
        self.lblImageLogo = QLabel(self)
        self.lblGainA = QLabel(Strings.gainA)
        self.lblGainB = QLabel(Strings.gainB)
        self.lblOffsetA = QLabel(Strings.offsetA)
        self.lblOffsetB = QLabel(Strings.offsetB)
        self.lblInitialAngle = QLabel(Strings.initialAngle)
        self.lblAngleLongitude = QLabel(Strings.angleLongitude)
        self.lblAngleResolution = QLabel(Strings.angleResolution)
        self.lblFinalAngle = QLabel(Strings.finalAngle)
        self.lblPointsCurve = QLabel(Strings.pointsOfCurve)
        self.lblDataSampling = QLabel(Strings.dataSamplingSeconds)
        self.lblACQChannel_1 = QLabel(Strings.channel1dots)
        self.lblACQChannel_2 = QLabel(Strings.channel2dots)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QLineEdit -----------------------------------------------"""
        self.edtFinalAngle = QLineEdit()
        self.edtPointsCurve = QLineEdit()
        self.edtAcquisition = QLineEdit()
        self.edtACQChannel_1 = QLineEdit()
        self.edtACQChannel_2 = QLineEdit()
        self.edtSaveFile = QLineEdit()
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QSpinBox ------------------------------------------------"""
        self.edtGainA = QSpinBox()
        self.edtGainB = QSpinBox()
        self.edtOffsetA = QSpinBox()
        self.edtOffsetB = QSpinBox()
        self.edtInitialAngle = QSpinBox()
        self.edtAngleLongitude = QSpinBox()
        self.edtDataSampling = QSpinBox()
        """----------------------------------------------------------------------------------------------------------"""

        """--------------------------------------------- QDoubleSpinBox ---------------------------------------------"""
        self.edtAngleResolution = QDoubleSpinBox()
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------ QPixmap -------------------------------------------------"""
        self.imageLogo = QPixmap(Strings.imageLogoFull)
        """----------------------------------------------------------------------------------------------------------"""

        """------------------------------------------------- Charts -------------------------------------------------"""
        # self.myChartChannel1 = Chart(Strings.channel1UC)
        # self.myChartChannel2 = Chart(Strings.channel2UC)
        self.myChartChannel = Chart()
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGroupBoxes -----------------------------------------------"""
        self.calibrationBoxLayout = QGroupBox(Strings.calibrationParameters)
        self.gainBoxLayout = QGroupBox()
        self.offsetBoxLayout = QGroupBox()
        self.btnCalibrateBoxLayout = QGroupBox()
        self.btnLaserBoxLayout = QGroupBox()
        self.curveBoxLayout = QGroupBox(Strings.curvePerformance)
        self.acquisitionBoxLayout = QGroupBox(Strings.acquisitionMode)
        self.autoACQBoxLayout = QGroupBox()
        self.saveFileBoxLayout = QGroupBox(Strings.saveFileLC)
        self.imageBoxLayout = QGroupBox()
        self.chartBoxLayout = QGroupBox()
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QGridLayouts ----------------------------------------------"""
        self.layoutGrid = QGridLayout(self)
        self.calibrationLayout = QGridLayout(self)
        self.curveLayout = QGridLayout(self)
        self.acquisitionLayout = QGridLayout(self)
        self.autoACQLayout = QGridLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QVBoxLayouts ----------------------------------------------"""
        self.gainLayout = QVBoxLayout(self)
        self.offsetLayout = QVBoxLayout(self)
        self.btnCalibrateLayout = QVBoxLayout(self)
        self.btnLaserLayout = QVBoxLayout(self)
        self.saveFileLayout = QVBoxLayout(self)
        self.imageLayout = QVBoxLayout(self)
        self.chartLayout = QVBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """---------------------------------------------- QHBoxLayouts ----------------------------------------------"""
        self.gainALayout = QHBoxLayout(self)
        self.gainBLayout = QHBoxLayout(self)
        self.offsetALayout = QHBoxLayout(self)
        self.offsetBLayout = QHBoxLayout(self)
        """----------------------------------------------------------------------------------------------------------"""

        """--------------------------------------------- Style Functions --------------------------------------------"""
        self.setStyleButtons()
        self.setStyleSpinBox()
        self.setStyleLineEdit()
        self.setStyleLabels()
        self.setStyleLed()
        self.setStylePixmap()
        self.setStyleGroupBox()
        self.setStyleLayouts()
        """----------------------------------------------------------------------------------------------------------"""

    def mainWindow(self):
        """Add the main widgets to the main layout.

        Add the group box to the layout of the app.
        """
        self.layoutGrid.addWidget(self.setCalibrationGroup(), 0, 0, 1, 1)
        self.layoutGrid.addWidget(self.setLaserGroup(), 0, 1, 1, 1)
        self.layoutGrid.addWidget(self.setCurveGroup(), 1, 0, 1, 2)
        self.layoutGrid.addWidget(self.setAcquisitionGroup(), 2, 0, 1, 2)
        self.layoutGrid.addWidget(self.setSaveFileGroup(), 3, 0, 1, 2)
        self.layoutGrid.addWidget(self.setImageGroup(), 4, 0, 1, 2)
        self.layoutGrid.addWidget(self.setChartGroup(), 0, 2, 5, 8)

    def setCalibrationGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.gainALayout.addWidget(self.lblGainA)
        self.gainALayout.addWidget(self.edtGainA)
        self.gainBLayout.addWidget(self.lblGainB)
        self.gainBLayout.addWidget(self.edtGainB)

        self.gainLayout.addLayout(self.gainALayout)
        self.gainLayout.addLayout(self.gainBLayout)

        self.offsetALayout.addWidget(self.lblOffsetA)
        self.offsetALayout.addWidget(self.edtOffsetA)
        self.offsetBLayout.addWidget(self.lblOffsetB)
        self.offsetBLayout.addWidget(self.edtOffsetB)

        self.offsetLayout.addLayout(self.offsetALayout)
        self.offsetLayout.addLayout(self.offsetBLayout)

        self.gainBoxLayout.setLayout(self.gainLayout)

        self.offsetBoxLayout.setLayout(self.offsetLayout)

        self.calibrationLayout.addWidget(self.gainBoxLayout, 0, 0)
        self.calibrationLayout.addWidget(self.offsetBoxLayout, 1, 0)
        self.calibrationLayout.addWidget(self.btnCalibrate, 1, 1, 1, 1)

        self.calibrationBoxLayout.setLayout(self.calibrationLayout)

        return self.calibrationBoxLayout

    def setLaserGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.btnLaserLayout.addWidget(self.ledLaser, 0, Qt.AlignCenter)
        self.btnLaserLayout.addWidget(self.btnLaser, 0, Qt.AlignBottom)

        self.btnLaserBoxLayout.setLayout(self.btnLaserLayout)

        return self.btnLaserBoxLayout

    def setCurveGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.curveLayout.addWidget(self.lblInitialAngle, 0, 0)
        self.curveLayout.addWidget(self.edtInitialAngle, 0, 1)
        self.curveLayout.addWidget(self.lblAngleLongitude, 1, 0)
        self.curveLayout.addWidget(self.edtAngleLongitude, 1, 1)
        self.curveLayout.addWidget(self.lblAngleResolution, 2, 0)
        self.curveLayout.addWidget(self.edtAngleResolution, 2, 1)
        self.curveLayout.addWidget(self.lblFinalAngle, 3, 0)
        self.curveLayout.addWidget(self.edtFinalAngle, 3, 1)
        self.curveLayout.addWidget(self.lblPointsCurve, 4, 0)
        self.curveLayout.addWidget(self.edtPointsCurve, 4, 1)
        self.curveLayout.addWidget(self.btnReset, 3, 2, 2, 1)

        self.curveBoxLayout.setLayout(self.curveLayout)

        return self.curveBoxLayout

    def setAcquisitionGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.autoACQLayout.addWidget(self.edtAcquisition, 0, 1)
        self.autoACQLayout.addWidget(self.btnAutoAcquisition, 1, 0, 1, 3)

        self.autoACQBoxLayout.setLayout(self.autoACQLayout)

        self.acquisitionLayout.addWidget(self.autoACQBoxLayout, 0, 0, 4, 1)
        self.acquisitionLayout.addWidget(self.lblDataSampling, 1, 1)
        self.acquisitionLayout.addWidget(self.edtDataSampling, 1, 2)
        self.acquisitionLayout.addWidget(self.lblACQChannel_1, 2, 1)
        self.acquisitionLayout.addWidget(self.edtACQChannel_1, 2, 2)
        self.acquisitionLayout.addWidget(self.lblACQChannel_2, 3, 1)
        self.acquisitionLayout.addWidget(self.edtACQChannel_2, 3, 2)

        self.acquisitionBoxLayout.setLayout(self.acquisitionLayout)

        return self.acquisitionBoxLayout

    def setSaveFileGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.saveFileLayout.addWidget(self.edtSaveFile)
        self.saveFileLayout.addWidget(self.btnSaveFile)

        self.saveFileBoxLayout.setLayout(self.saveFileLayout)

        return self.saveFileBoxLayout

    def setImageGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.lblImageLogo.setPixmap(self.imageLogo)

        self.imageLayout.addWidget(self.lblImageLogo)

        self.imageBoxLayout.setLayout(self.imageLayout)

        return self.imageBoxLayout

    def setChartGroup(self):
        """Add the rest of the widgets to its layout.

        Add the buttons, labels, line edits, etc. to its layout.

        Returns:
            QGroupBox: return the main group box of this step.
        """
        self.setCharts('CHANNEL 1', '#FF9933', 'CHANNEL 2', '#33CCFF')
        self.chartLayout.addWidget(self.myChartChannel)
        # self.chartLayout.addWidget(self.myChartChannel1)
        # self.chartLayout.addWidget(self.myChartChannel2)

        self.chartBoxLayout.setLayout(self.chartLayout)

        return self.chartBoxLayout

    """
    ********************************************************************************************************************
    *                                         Calibration Parameters Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnCalibrateStatus(self, done):
        if done:
            self.btnCalibrate.setStyleSheet(Styles.buttonCalibrateDone)

        else:
            self.btnCalibrate.setStyleSheet(Styles.buttonCalibrate)

        self.btnCalibrate.setChecked(False)

    def setBtnCalibrateDisable(self, disable):
        self.btnCalibrate.setDisabled(disable)

    def setEdtGainAValue(self, value):
        self.edtGainA.setValue(value)

    def getEdtGainAValue(self):
        return self.edtGainA.value()

    def setEdtGainBValue(self, value):
        self.edtGainB.setValue(value)

    def getEdtGainBValue(self):
        return self.edtGainB.value()

    def setEdtOffsetAValue(self, value):
        self.edtOffsetA.setValue(value)

    def getEdtOffsetAValue(self):
        return self.edtOffsetA.value()

    def setEdtOffsetBValue(self, value):
        self.edtOffsetB.setValue(value)

    def getEdtOffsetBValue(self):
        return self.edtOffsetB.value()

    """
    ********************************************************************************************************************
    *                                       End Calibration Parameters Functions                                       *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                               Laser Led Functions                                                *
    ********************************************************************************************************************
    """

    def setLedLaserStatus(self, status):
        """Change the status of the led laser.

        Args:
            status (bool): the status of the button.
        """
        self.ledLaser.setChecked(status)

    def getLedLaserStatus(self):
        """Return the status of the led laser.

        Returns:
            bool: the status of the led, if the led is enabled or disabled.
        """
        return self.ledLaser.isChecked()

    def setLedLaserDisable(self, disable):
        """Enable or disable the led laser.

        Args:
            disable (bool): if the value is True, the led will be disabled, in the opposite case, the led will be
            enabled.
        """
        self.ledLaser.setDisabled(disable)

    """
    ********************************************************************************************************************
    *                                             End Laser Led Functions                                              *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                              Laser Button Functions                                              *
    ********************************************************************************************************************
    """

    def setBtnLaserStatus(self, status):
        if status:
            text = Strings.laserStop

        else:
            text = Strings.laserStart

        self.btnLaser.setText(text)
        self.btnLaser.setChecked(status)

    def getBtnLaserStatus(self):
        return self.btnLaser.isChecked()

    def setBtnLaserDisable(self, disable):
        self.btnLaser.setDisabled(disable)

    """
    ********************************************************************************************************************
    *                                            End Laser Button Functions                                            *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                           Curve Performance Functions                                            *
    ********************************************************************************************************************
    """

    def setBtnResetStatus(self, status):
        self.btnReset.setChecked(status)

    def getBtnResetStatus(self):
        return self.btnReset.isChecked()

    def setBtnResetDisable(self, disable):
        self.btnReset.setDisabled(disable)

    def setEdtInitialAngleValue(self, value):
        self.edtInitialAngle.setValue(value)

    def getEdtInitialAngleValue(self):
        return self.edtInitialAngle.value()

    def setEdtAngleLongitudeValue(self, value):
        self.edtAngleLongitude.setValue(value)

    def getEdtAngleLongitudeValue(self):
        return self.edtAngleLongitude.value()

    def setEdtAngleResolutionValue(self, value):
        self.edtAngleResolution.setValue(value)

    def getEdtAngleResolutionValue(self):
        return self.edtAngleResolution.value()

    def setEdtFinalAngleValue(self, text):
        self.edtFinalAngle.setText(str(text))

    def getEdtFinalAngleValue(self):
        return int(self.edtFinalAngle.text())

    def setEdtPointsCurveValue(self, text):
        self.edtPointsCurve.setText(str(text))

    def getEdtPointsCurveValue(self):
        return int(self.edtPointsCurve.text())

    """
    ********************************************************************************************************************
    *                                          End Curve Performance Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                           Acquisition Mode Functions                                             *
    ********************************************************************************************************************
    """

    def setBtnAutoAcquisitionStatus(self, status):
        self.btnAutoAcquisition.setChecked(status)

    def getBtnAutoAcquisitionStatus(self):
        return self.btnAutoAcquisition.isChecked()

    def setBtnAutoAcquisitionDisable(self, disable):
        self.btnAutoAcquisition.setDisabled(disable)

    def setBtnAutoAcquisitionInProcess(self, inProcess):
        if inProcess:
            self.btnAutoAcquisition.setStyleSheet(Styles.buttonAutoAcquisitionInProcess)

        else:
            self.btnAutoAcquisition.setStyleSheet(Styles.buttonAutoAcquisition)
            self.setEdtDataSamplingDisable(False)

        self.setBtnAutoAcquisitionStatus(inProcess)
        self.setBtnAutoAcquisitionDisable(False)

    def setEdtDataSamplingValue(self, value):
        self.edtDataSampling.setValue(value)

    def getEdtDataSamplingValue(self):
        return self.edtDataSampling.value()

    def setEdtDataSamplingDisable(self, disable):
        self.edtDataSampling.setDisabled(disable)

    def setEdtAcquisitionText(self, text):
        self.edtAcquisition.setText(str(text))

    def getEdtAcquisitionText(self):
        return int(self.edtAcquisition.text())

    def setEdtACQChannel1Text(self, text):
        self.edtACQChannel_1.setText(str(text))

    def getEdtACQChannel1Text(self):
        return int(self.edtACQChannel_1.text())

    def setEdtACQChannel2Text(self, text):
        self.edtACQChannel_2.setText(str(text))

    def getEdtACQChannel2Text(self):
        return int(self.edtACQChannel_2.text())

    """
    ********************************************************************************************************************
    *                                         End Acquisition Mode Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                               Save File Functions                                                *
    ********************************************************************************************************************
    """

    def setEdtSaveFileText(self, text):
        self.edtSaveFile.setText(text)

    def getEdtSaveFileText(self):
        return self.edtSaveFile.text()

    """
    ********************************************************************************************************************
    *                                             End Save File Functions                                              *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                 Chart Functions                                                  *
    ********************************************************************************************************************
    """

    def setCharts(self, name1, color1, name2, color2):
        self.myChartChannel.setAxisXName(Strings.angleOfIncidence)
        self.myChartChannel.setAxisYName(Strings.signalAmplitude)
        self.myChartChannel.setRangeX([58.00, 62.00])
        self.myChartChannel.setRangeY([0, 100])
        self.myChartChannel.setAxisXTickCount(9)

        # self.myChartChannel1.setAxisXName(Strings.angleOfIncidence)
        # self.myChartChannel1.setAxisYName(Strings.signalAmplitude)
        # self.myChartChannel1.setRangeX([58.00, 62.00])
        # self.myChartChannel1.setAxisXTickCount(9)

        # self.myChartChannel2.setAxisXName(Strings.angleOfIncidence)
        # self.myChartChannel2.setAxisYName(Strings.signalAmplitude)
        # self.myChartChannel2.setRangeX([58.00, 62.00])
        # self.myChartChannel2.setAxisXTickCount(9)

        self.myChartChannel.setAddSerie(name1, color1)
        self.myChartChannel.setAddSerie(name2, color2)

    def setDataChannel(self, xData, yData1, yData2):
        self.myChartChannel.setDataChart(xData, yData1, yData2)

    def initSerieChannel(self):
        self.myChartChannel.initSeries()

    # def setDataChannel1(self, xData, yData):
    #     self.myChartChannel1.setDataChart(xData, yData)
    #
    # def setDataChannel2(self, xData, yData):
    #     self.myChartChannel2.setDataChart(xData, yData)
    #
    # def initSerieChannel1(self):
    #     self.myChartChannel1.initSerie()
    #
    # def initSerieChannel2(self):
    #     self.myChartChannel2.initSerie()

    """
    ********************************************************************************************************************
    *                                               End Chart Functions                                                *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Buttons Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleButtons(self):
        self.btnLaser.setStyleSheet(Styles.buttonLaserSmall)
        self.btnLaser.setCheckable(True)

        self.btnCalibrate.setStyleSheet(Styles.buttonCalibrate)
        self.btnCalibrate.setCheckable(True)

        self.btnReset.setStyleSheet(Styles.buttonReset)
        self.btnReset.setCheckable(True)

        self.btnAutoAcquisition.setStyleSheet(Styles.buttonAutoAcquisition)
        self.btnAutoAcquisition.setCheckable(True)

        self.btnSaveFile.setStyleSheet(Styles.buttonSaveFile)

    """
    ********************************************************************************************************************
    *                                           End Buttons Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Spin Boxes Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setStyleSpinBox(self):
        self.edtGainA.setStyleSheet(Styles.spinBoxGeneral)
        self.edtGainB.setStyleSheet(Styles.spinBoxGeneral)
        self.edtOffsetA.setStyleSheet(Styles.spinBoxGeneral)
        self.edtOffsetB.setStyleSheet(Styles.spinBoxGeneral)
        self.edtInitialAngle.setStyleSheet(Styles.spinBoxGeneral)
        self.edtAngleLongitude.setStyleSheet(Styles.spinBoxGeneral)

        self.edtAngleResolution.setStyleSheet(Styles.doubleSpinBoxGeneral)
        """
        This method (QLocale) can change the format of the value, for example, if we have a float with a dot as
        separator with this method we can convert from dot to comma or vice versa.
        """
        self.edtAngleResolution.setLocale(QLocale(Strings.formatEnglish))

        self.edtDataSampling.setStyleSheet(Styles.spinBoxGeneral)

        self.edtGainA.setRange(0, 100)
        self.edtGainB.setRange(0, 100)
        self.edtOffsetA.setRange(0, 100)
        self.edtOffsetB.setRange(0, 100)

        self.edtAngleResolution.setSingleStep(0.1)

    """
    ********************************************************************************************************************
    *                                          End Spin Boxes Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                            Line Edits Styles Functions                                           *
    ********************************************************************************************************************
    """

    def setStyleLineEdit(self):
        self.edtFinalAngle.setStyleSheet(Styles.lineEditGeneral)
        self.edtFinalAngle.setReadOnly(True)
        self.edtFinalAngle.setFixedWidth(100)

        self.edtPointsCurve.setStyleSheet(Styles.lineEditGeneral)
        self.edtPointsCurve.setReadOnly(True)
        self.edtPointsCurve.setFixedWidth(100)

        self.edtAcquisition.setStyleSheet(Styles.lineEditGeneral)
        self.edtAcquisition.setReadOnly(True)
        self.edtAcquisition.setFixedWidth(50)

        self.edtACQChannel_1.setStyleSheet(Styles.lineEditGeneral)
        self.edtACQChannel_1.setReadOnly(True)
        self.edtACQChannel_1.setFixedWidth(100)

        self.edtACQChannel_2.setStyleSheet(Styles.lineEditGeneral)
        self.edtACQChannel_2.setReadOnly(True)
        self.edtACQChannel_2.setFixedWidth(100)

        self.edtSaveFile.setStyleSheet(Styles.lineEditGeneral)

        self.edtGainA.setFixedWidth(50)

        self.edtGainB.setFixedWidth(50)

        self.edtOffsetA.setFixedWidth(50)

        self.edtOffsetB.setFixedWidth(50)

    """
    ********************************************************************************************************************
    *                                          End Line Edits Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                              Labels Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleLabels(self):
        self.lblGainA.setFixedWidth(45)

        self.lblGainB.setFixedWidth(45)

        self.lblOffsetA.setFixedWidth(45)

        self.lblOffsetB.setFixedWidth(45)

        self.lblInitialAngle.setFixedWidth(100)

        self.lblAngleLongitude.setFixedWidth(100)

        self.lblAngleResolution.setFixedWidth(100)

        self.lblFinalAngle.setFixedWidth(100)

        self.lblPointsCurve.setFixedWidth(100)

        self.lblDataSampling.setFixedWidth(75)
        self.lblDataSampling.setWordWrap(True)

        self.lblACQChannel_1.setFixedWidth(50)

        self.lblACQChannel_2.setFixedWidth(50)

    """
    ********************************************************************************************************************
    *                                            End Labels Styles Functions                                           *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                               Led Styles Functions                                               *
    ********************************************************************************************************************
    """

    def setStyleLed(self):
        """Change the style of the led to the custom style."""
        self.setLedLaserDisable(True)
        self.ledLaser.setFixedWidth(50)
        self.ledLaser.setFixedHeight(50)
        self.ledLaser.on_color_1 = QColor(255, 0, 0)
        self.ledLaser.on_color_2 = QColor(192, 0, 0)
        self.ledLaser.off_color_1 = QColor(28, 0, 0)
        self.ledLaser.off_color_2 = QColor(128, 0, 0)

    """
    ********************************************************************************************************************
    *                                            End Led Styles Functions                                              *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Pixmap Styles Functions                                              *
    ********************************************************************************************************************
    """

    def setStylePixmap(self):
        self.imageLogo = self.imageLogo.scaledToHeight(50)

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
        self.gainBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.offsetBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.calibrationBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.btnLaserBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.curveBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.autoACQBoxLayout.setStyleSheet(Styles.groupBoxAutoAcquisition)

        self.acquisitionBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.saveFileBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

        self.imageBoxLayout.setStyleSheet(Styles.groupBoxGeneralWithoutBorder)

        self.chartBoxLayout.setStyleSheet(Styles.groupBoxGeneral)

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
        QMessageBox.critical(self, Strings.error, message)

    def setMessageQuestion(self, message):
        saveFile = QMessageBox.question(self, Strings.question, message, QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)

        if saveFile == QMessageBox.Yes:
            return True

        else:
            return False

    def setDialogSaveFile(self, myNameFile):
        fileName, _ = QFileDialog.getSaveFileName(self, Strings.saveFileLC, 'C:/Users/' + getpass.getuser() +
                                                  '/Documents/' + myNameFile, '*.DAT')

        return fileName

    """
    ********************************************************************************************************************
    *                                              End Messages Functions                                              *
    ********************************************************************************************************************
    """
