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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QGraphicsView
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt, QLocale
import pyqtgraph as pg
import numpy as np
import styles as style


class ViewCurveSetup(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.graphChannel_1PlotItem = None
        self.graphChannel_1Plot = None
        self.graphChannel_2PlotItem = None
        self.graphChannel_2Plot = None
        self.xd = None
        self.y1d = None
        self.y2d = None

        self.timeoutMessage = {
            'Calibrate': 'The device has not been calibrated, try again.',
            'Automatic': 'The device has not respond, try again.'
        }

        self.lblGainA = QLabel('Gain A:')
        self.edtGainA = QSpinBox()
        self.lblGainB = QLabel('Gain B:')
        self.edtGainB = QSpinBox()
        self.lblOffsetA = QLabel('Offset A:')
        self.edtOffsetA = QSpinBox()
        self.lblOffsetB = QLabel('Offset B:')
        self.edtOffsetB = QSpinBox()

        self.btnCalibrate = QPushButton('Calibrate')
        self.btnLaser = QPushButton('Laser OFF')

        self.lblInitialAngle = QLabel('Initial Angle:')
        self.edtInitialAngle = QSpinBox()
        self.lblAngleLongitude = QLabel('Angle Longitude:')
        self.edtAngleLongitude = QSpinBox()
        self.lblAngleResolution = QLabel('Angle Resolution:')
        self.edtAngleResolution = QDoubleSpinBox()
        self.lblFinalAngle = QLabel('Final Angle:')
        self.edtFinalAngle = QLineEdit()
        self.edtFinalAngle.setReadOnly(True)
        self.lblPointsCurve = QLabel('Points of Curve:')
        self.edtPointsCurve = QLineEdit()
        self.edtPointsCurve.setReadOnly(True)

        self.btnReset = QPushButton('Reset')

        self.edtAcquisition = QLineEdit()
        self.edtAcquisition.setReadOnly(True)
        self.lblDataSampling = QLabel('Data Sampling (seconds):')
        self.edtDataSampling = QSpinBox()
        self.lblACQChannel_1 = QLabel('Channel 1:')
        self.edtACQChannel_1 = QLineEdit()
        self.edtACQChannel_1.setReadOnly(True)
        self.lblACQChannel_2 = QLabel('Channel 2:')
        self.edtACQChannel_2 = QLineEdit()
        self.edtACQChannel_2.setReadOnly(True)

        self.btnAutoAcquisition = QPushButton('Automatic')

        self.graphChannel_1 = pg.PlotWidget(name='Channel 1')
        self.graphChannel_2 = pg.PlotWidget(name='Channel 2')
        self.graphicsViewChannel_1 = QGraphicsView(self)
        self.graphicsViewChannel_2 = QGraphicsView(self)

        self.layoutGrid = QGridLayout(self)

        self.calibrationBoxLayout = QGroupBox('Calibration Parameters')
        self.gainBoxLayout = QGroupBox()
        self.offsetBoxLayout = QGroupBox()
        self.btnCalibrateBoxLayout = QGroupBox()
        self.btnLaserBoxLayout = QGroupBox()

        self.curveBoxLayout = QGroupBox('Curve Performance')

        self.filledBoxLayout_1 = QGroupBox()
        self.filledLayout_2 = QGroupBox()

        self.acquisitionBoxLayout = QGroupBox('Acquisition Mode')
        self.autoACQBoxLayout = QGroupBox()

        self.graphCurveBoxLayout = QGroupBox('Graphs')
        self.graphCurveChannel1BoxLayout = QGroupBox('Channel 1')
        self.graphCurveChannel2BoxLayout = QGroupBox('Channel 2')

        self.calibrationLayout = QGridLayout(self)
        self.curveLayout = QGridLayout(self)
        self.acquisitionLayout = QGridLayout(self)
        self.autoACQLayout = QGridLayout(self)
        self.graphCurveLayout = QGridLayout(self)
        self.graphCurveChannel1Layout = QGridLayout(self)
        self.graphCurveChannel2Layout = QGridLayout(self)

        self.gainLayout = QVBoxLayout(self)
        self.offsetLayout = QVBoxLayout(self)
        self.btnCalibrateLayout = QVBoxLayout(self)
        self.btnLaserLayout = QVBoxLayout(self)

        self.gainALayout = QHBoxLayout(self)
        self.gainBLayout = QHBoxLayout(self)
        self.offsetALayout = QHBoxLayout(self)
        self.offsetBLayout = QHBoxLayout(self)

        self.graphChannel_1Layout = QHBoxLayout(self)
        self.graphChannel_2Layout = QHBoxLayout(self)

        self.setStyleButtons()
        self.setStyleSpinBox()
        self.setStyleLineEdit()

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('SPR v2')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setCalibrationGroup(), 0, 0, 1, 1)
        self.layoutGrid.addWidget(self.setLaserGroup(), 0, 1, 1, 1)
        self.layoutGrid.addWidget(self.setCurveGroup(), 1, 0, 1, 2)
        self.layoutGrid.addWidget(self.setAcquisitionGroup(), 2, 0, 1, 2)
        self.layoutGrid.addWidget(self.setGraphGroup(), 0, 2, 6, 8)
        # self.layoutGrid.addWidget(self.setFilledGroup_1(), 3, 0, 5, 10)

    def setFilledGroup_1(self):
        self.filledBoxLayout_1.setStyleSheet(style.groupBoxFilled)

        return self.filledBoxLayout_1

    def setFilledGroup_2(self):
        self.filledLayout_2.setStyleSheet(style.groupBoxFilled)

        return self.filledLayout_2

    def setCalibrationGroup(self):
        self.lblGainA.setFixedWidth(45)
        self.lblGainB.setFixedWidth(45)
        self.lblOffsetA.setFixedWidth(45)
        self.lblOffsetB.setFixedWidth(45)
        self.edtGainA.setFixedWidth(50)
        self.edtGainB.setFixedWidth(50)
        self.edtOffsetA.setFixedWidth(50)
        self.edtOffsetB.setFixedWidth(50)

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

        self.gainBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.gainBoxLayout.setLayout(self.gainLayout)

        self.offsetBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.offsetBoxLayout.setLayout(self.offsetLayout)

        self.calibrationLayout.addWidget(self.gainBoxLayout, 0, 0)
        self.calibrationLayout.addWidget(self.offsetBoxLayout, 1, 0)
        self.calibrationLayout.addWidget(self.btnCalibrate, 1, 1, 1, 1)

        self.calibrationBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.calibrationBoxLayout.setLayout(self.calibrationLayout)

        return self.calibrationBoxLayout

    def setLaserGroup(self):
        self.btnLaserLayout.addWidget(self.btnLaser, 0, Qt.AlignBottom)

        self.btnLaserBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.btnLaserBoxLayout.setLayout(self.btnLaserLayout)

        return self.btnLaserBoxLayout

    def setCurveGroup(self):
        self.lblInitialAngle.setFixedWidth(100)
        self.lblAngleLongitude.setFixedWidth(100)
        self.lblAngleResolution.setFixedWidth(100)
        self.lblFinalAngle.setFixedWidth(100)
        self.lblPointsCurve.setFixedWidth(100)
        self.edtFinalAngle.setFixedWidth(100)
        self.edtPointsCurve.setFixedWidth(100)

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

        self.curveBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.curveBoxLayout.setLayout(self.curveLayout)

        return self.curveBoxLayout

    def setAcquisitionGroup(self):
        self.lblDataSampling.setFixedWidth(75)
        self.lblDataSampling.setWordWrap(True)
        self.lblACQChannel_1.setFixedWidth(50)
        self.lblACQChannel_2.setFixedWidth(50)
        self.edtAcquisition.setFixedWidth(50)
        self.edtACQChannel_1.setFixedWidth(100)
        self.edtACQChannel_2.setFixedWidth(100)

        self.autoACQLayout.addWidget(self.edtAcquisition, 0, 1)
        self.autoACQLayout.addWidget(self.btnAutoAcquisition, 1, 0, 1, 3)

        self.autoACQBoxLayout.setStyleSheet(style.groupBoxAutoAcquisition)
        self.autoACQBoxLayout.setLayout(self.autoACQLayout)

        self.acquisitionLayout.addWidget(self.autoACQBoxLayout, 0, 0, 4, 1)
        self.acquisitionLayout.addWidget(self.lblDataSampling, 1, 1)
        self.acquisitionLayout.addWidget(self.edtDataSampling, 1, 2)
        self.acquisitionLayout.addWidget(self.lblACQChannel_1, 2, 1)
        self.acquisitionLayout.addWidget(self.edtACQChannel_1, 2, 2)
        self.acquisitionLayout.addWidget(self.lblACQChannel_2, 3, 1)
        self.acquisitionLayout.addWidget(self.edtACQChannel_2, 3, 2)

        self.acquisitionBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.acquisitionBoxLayout.setLayout(self.acquisitionLayout)

        return self.acquisitionBoxLayout

    def setGraphGroup(self):
        self.setGraphChannel1()
        self.setGraphChannel2()

        self.graphChannel_1Layout.addWidget(self.graphChannel_1)
        self.graphicsViewChannel_1.setLayout(self.graphChannel_1Layout)

        self.graphCurveChannel1Layout.addWidget(self.graphicsViewChannel_1, 0, 0)

        self.graphCurveChannel1BoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.graphCurveChannel1BoxLayout.setLayout(self.graphCurveChannel1Layout)

        self.graphChannel_2Layout.addWidget(self.graphChannel_2)
        self.graphicsViewChannel_2.setLayout(self.graphChannel_2Layout)

        self.graphCurveChannel2Layout.addWidget(self.graphicsViewChannel_2, 0, 0)

        self.graphCurveChannel2BoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.graphCurveChannel2BoxLayout.setLayout(self.graphCurveChannel2Layout)

        self.graphCurveLayout.addWidget(self.graphCurveChannel1BoxLayout, 0, 0)
        self.graphCurveLayout.addWidget(self.graphCurveChannel2BoxLayout, 1, 0)

        self.graphCurveBoxLayout.setStyleSheet(style.groupBoxGeneral)
        self.graphCurveBoxLayout.setLayout(self.graphCurveLayout)

        return self.graphCurveBoxLayout

    """
    ********************************************************************************************************************
    *                                         Calibration Parameters Functions                                         *
    ********************************************************************************************************************
    """

    def setBtnCalibrateStatus(self, done):
        if done:
            self.btnCalibrate.setStyleSheet(style.buttonCalibrateDone)
            self.btnCalibrate.setChecked(False)

        else:
            self.btnCalibrate.setStyleSheet(style.buttonCalibrate)
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
    *                                              Laser Button Functions                                              *
    ********************************************************************************************************************
    """

    def setBtnLaserStatus(self, status):
        if status:
            text = 'Laser ON'

        else:
            text = 'Laser OFF'

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
            self.btnAutoAcquisition.setStyleSheet(style.buttonAutoAcquisitionInProcess)

        else:
            self.btnAutoAcquisition.setStyleSheet(style.buttonAutoAcquisition)
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
    *                                                 Graph Functions                                                  *
    ********************************************************************************************************************
    """

    def setGraphChannel1(self):
        self.graphChannel_1PlotItem = self.graphChannel_1.plotItem
        self.graphChannel_1Plot = self.graphChannel_1PlotItem.plot()
        self.graphChannel_1Plot.setPen((200, 200, 100))
        self.graphChannel_1Plot.setSymbolBrush((255, 0, 0))
        self.graphChannel_1Plot.setSymbolPen('w')
        self.graphChannel_1Plot.setSymbol('o')
        self.graphChannel_1Plot.setSymbolSize(4)
        self.graphChannel_1PlotItem.setLabel('left', 'Signal Amplitude')
        self.graphChannel_1PlotItem.setLabel('bottom', 'Angle of Incidence')
        self.graphChannel_1PlotItem.showGrid(x=True, y=True)
        self.graphChannel_1.setXRange(58.00, 62.00)
        self.graphChannel_1.setYRange(0, 100)

    def setGraphChannel2(self):
        self.graphChannel_2PlotItem = self.graphChannel_2.plotItem
        self.graphChannel_2Plot = self.graphChannel_2PlotItem.plot()
        self.graphChannel_2Plot.setPen((200, 200, 100))
        self.graphChannel_2Plot.setSymbolBrush((255, 0, 0))
        self.graphChannel_2Plot.setSymbolPen('w')
        self.graphChannel_2Plot.setSymbol('o')
        self.graphChannel_2Plot.setSymbolSize(4)
        self.graphChannel_2PlotItem.setLabel('left', 'Signal Amplitude')
        self.graphChannel_2PlotItem.setLabel('bottom', 'Angle of Incidence')
        self.graphChannel_2PlotItem.showGrid(x=True, y=True)
        self.graphChannel_2.setXRange(58.00, 62.00)
        self.graphChannel_2.setYRange(0, 100)

    def updateData(self, valueX, valueY1, valueY2):
        if valueX == 58.00:
            self.xd = np.array([valueX])
            self.y1d = np.array([valueY1])
            self.y2d = np.array([valueY2])

        else:
            self.xd = np.append(self.xd, valueX)
            self.y1d = np.append(self.y1d, valueY1)
            self.y2d = np.append(self.y2d, valueY2)

        self.graphChannel_1Plot.setData(y=self.y1d, x=self.xd)
        self.graphChannel_2Plot.setData(y=self.y2d, x=self.xd)

    def calc_parabola_vertex(self, x1, y1, x2, y2, x3, y3):
        denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
        A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
        B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
        C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom

        return A, B, C

    """
    ********************************************************************************************************************
    *                                               End Graph Functions                                                *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                             Buttons Styles Functions                                             *
    ********************************************************************************************************************
    """

    def setStyleButtons(self):
        self.btnLaser.setStyleSheet(style.buttonLaserSmall)
        self.btnLaser.setCheckable(True)

        self.btnCalibrate.setStyleSheet(style.buttonCalibrate)
        self.btnCalibrate.setCheckable(True)

        self.btnReset.setStyleSheet(style.buttonReset)
        self.btnReset.setCheckable(True)

        self.btnAutoAcquisition.setStyleSheet(style.buttonAutoAcquisition)
        self.btnAutoAcquisition.setCheckable(True)

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
        self.edtGainA.setStyleSheet(style.spinBoxGeneral)
        self.edtGainB.setStyleSheet(style.spinBoxGeneral)
        self.edtOffsetA.setStyleSheet(style.spinBoxGeneral)
        self.edtOffsetB.setStyleSheet(style.spinBoxGeneral)
        self.edtInitialAngle.setStyleSheet(style.spinBoxGeneral)
        self.edtAngleLongitude.setStyleSheet(style.spinBoxGeneral)

        self.edtAngleResolution.setStyleSheet(style.doubleSpinBoxGeneral)
        """
        This method (QLocale) can change the format of the value, for example, if we have a float with a dot as
        separator with this method we can convert from dot to comma or vice versa.
        """
        self.edtAngleResolution.setLocale(QLocale('English'))

        self.edtDataSampling.setStyleSheet(style.spinBoxGeneral)

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
        self.edtFinalAngle.setStyleSheet(style.lineEditGeneral)
        self.edtPointsCurve.setStyleSheet(style.lineEditGeneral)

        self.edtAcquisition.setStyleSheet(style.lineEditGeneral)
        self.edtACQChannel_1.setStyleSheet(style.lineEditGeneral)
        self.edtACQChannel_2.setStyleSheet(style.lineEditGeneral)

    """
    ********************************************************************************************************************
    *                                          End Line Edits Styles Functions                                         *
    ********************************************************************************************************************
    """

    """
    ********************************************************************************************************************
    *                                                Messages Functions                                                *
    ********************************************************************************************************************
    """

    def setMessageCritical(self, typeMessage, message):
        QMessageBox.critical(self, typeMessage, message)

    """
    ********************************************************************************************************************
    *                                              End Messages Functions                                              *
    ********************************************************************************************************************
    """

