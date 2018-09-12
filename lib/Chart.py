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

from PyQt5.QtChart import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt


class Chart(QChartView):

    def __init__(self, title):
        chart = QChart()

        QChartView.__init__(self, chart)

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.xRange = [0, 100]
        self.yRange = [0, 100]

        self.setRenderHint(QPainter.Antialiasing)
        chart.setTitle(title)
        chart.setTitleBrush(Qt.white)
        chart.setAnimationOptions(QChart.NoAnimation)
        chart.legend().setVisible(False)
        chart.setBackgroundBrush(Qt.black)

        self.curve = QLineSeries()
        pen = self.curve.pen()

        pen.setColor(Qt.green)
        pen.setWidthF(2)
        self.curve.setPen(pen)

        chart.addSeries(self.curve)

        penAxisGrid = QPen(QColor('#F2F2F2'))
        penAxisGrid.setWidthF(0.5)
        penAxisMinorGrid = QPen(QColor('#A4A4A4'))
        penAxisMinorGrid.setWidthF(0.3)

        self.axisX.setGridLinePen(penAxisGrid)
        self.axisX.setLinePen(penAxisGrid)
        self.axisY.setGridLinePen(penAxisGrid)
        self.axisY.setLinePen(penAxisGrid)

        self.axisX.setMinorGridLinePen(penAxisMinorGrid)
        self.axisY.setMinorGridLinePen(penAxisMinorGrid)

        self.axisX.setLabelsColor(Qt.white)
        self.axisY.setLabelsColor(Qt.white)

        self.axisX.setMinorTickCount(4)
        self.axisY.setMinorTickCount(1)

        self.axisX.setTitleBrush(Qt.white)
        self.axisY.setTitleBrush(Qt.white)

        self.axisX.setTitleText('Time')
        self.axisY.setTitleText('Signal Amplitude')

        self.axisX.setTickCount(5)
        self.axisY.setTickCount(6)
        self.axisX.setRange(self.xRange[0], self.xRange[1])
        self.axisY.setRange(self.yRange[0], self.yRange[1])

        chart.setAxisX(self.axisX, self.curve)
        chart.setAxisY(self.axisY, self.curve)

    def setDataChart(self, xData, yData):
        if xData > self.xRange[1]:
            addValue = xData - self.xRange[1]

            if self.xRange[0] is not 0:
                self.xRange[0] = self.xRange[0] + addValue

            self.xRange[1] = self.xRange[1] + addValue
            self.axisX.setRange(self.xRange[0], self.xRange[1])

        self.curve.append(xData, yData)

    def setRangeY(self, yRange, autoscale):
        if autoscale:
            self.axisY.setRange(yRange[0] - (yRange[0] * 0.10), yRange[1] * 1.10)

        else:
            self.axisY.setRange(yRange[0], yRange[1])

    def setRangeX(self, xRange):
        self.axisX.setRange(xRange[0], xRange[1])

    def getRangeX(self):
        return self.xRange
