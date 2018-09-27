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

from PyQt5.QtChart import QChartView, QChart, QValueAxis, QLineSeries, QLegend
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class Chart(QChartView):

    def __init__(self):
        self.chart = QChart()

        QChartView.__init__(self, self.chart)

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.xRange = [0, 100]
        self.yRange = [-100, 100]

        self.curve = []

        self.setBackgroundBrush(QColor('#D8D8D8'))

        self.setRenderHint(QPainter.Antialiasing)
        # self.chart.setTitle(title)
        # self.chart.setTitleBrush(Qt.white)
        self.chart.setAnimationOptions(QChart.NoAnimation)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.legend().setLabelColor(Qt.white)
        self.chart.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.chart.setBackgroundBrush(QColor('#00004D'))

        # self.curve = QLineSeries()
        # pen = self.curve.pen()
        #
        # pen.setColor(QColor('#FF9933'))
        # pen.setWidthF(2)
        # self.curve.setPen(pen)
        #
        # self.chart.addSeries(self.curve)

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
        self.axisY.setMinorTickCount(4)

        self.axisX.setTitleBrush(Qt.white)
        self.axisY.setTitleBrush(Qt.white)

        self.axisX.setTitleText('Time')
        self.axisY.setTitleText('Signal Amplitude')

        self.axisX.setTickCount(11)
        self.axisY.setTickCount(11)
        self.axisX.setRange(self.xRange[0], self.xRange[1])
        self.axisY.setRange(self.yRange[0], self.yRange[1])

        # self.chart.setAxisX(self.axisX, self.curve)
        # self.chart.setAxisY(self.axisY, self.curve)

    def setAddSerie(self, name, color):
        self.curve.append(QLineSeries())
        pen = self.curve[len(self.curve)-1].pen()

        pen.setColor(QColor(color))
        pen.setWidthF(2)
        self.curve[len(self.curve)-1].setPen(pen)

        self.curve[len(self.curve) - 1].setName(name)

        self.chart.addSeries(self.curve[len(self.curve)-1])

        self.chart.setAxisX(self.axisX, self.curve[len(self.curve)-1])
        self.chart.setAxisY(self.axisY, self.curve[len(self.curve)-1])

    # def setDataChart(self, xData, yData):
    #     if xData > self.xRange[1]:
    #         addValue = xData - self.xRange[1]
    #
    #         if self.xRange[0] is not 0:
    #             self.xRange[0] = self.xRange[0] + addValue
    #
    #         self.xRange[1] = self.xRange[1] + addValue
    #         self.axisX.setRange(self.xRange[0], self.xRange[1])
    #
    #     self.curve.append(xData, yData)

    def setDataChart(self, xData, yData1, yData2):
        if xData > self.xRange[1]:
            addValue = xData - self.xRange[1]

            if self.xRange[0] is not 0:
                self.xRange[0] = self.xRange[0] + addValue

            self.xRange[1] = self.xRange[1] + addValue
            self.axisX.setRange(self.xRange[0], self.xRange[1])

        self.curve[0].append(xData, yData1)
        self.curve[1].append(xData, yData2)

    def setRangeY(self, yRange, autoscale):
        if autoscale:

            if yRange[0] == 0 and yRange[1] == 0:
                yRange[0] = -0.50
                yRange[1] = 0.50

            elif yRange[0] == 0:
                yRange[0] = -0.10
                yRange[1] = yRange[1] * 1.10

            elif yRange[1] == 0:
                yRange[0] = yRange[0] * 1.10
                yRange[1] = 0.10

            else:

                if yRange[0] < 0:
                    yRange[0] = yRange[0] * 1.10

                else:
                    yRange[0] = yRange[0] - (yRange[0] * 0.10)

                if yRange[1] < 0:
                    yRange[1] = yRange[1] - (yRange[1] * 0.10)

                else:
                    yRange[1] = yRange[1] * 1.10

            self.axisY.setRange(yRange[0], yRange[1])

        else:
            self.axisY.setRange(yRange[0], yRange[1])

    def setRangeX(self, xRange):
        self.axisX.setRange(xRange[0], xRange[1])

    def getRangeX(self):
        return self.xRange

    def setAxisXName(self, name):
        self.axisX.setTitleText(name)

    def setAxisYName(self, name):
        self.axisY.setTitleText(name)

    def setAxisXTickCount(self, tick):
        self.axisX.setTickCount(tick)

    def setAxisYTickCount(self, tick):
        self.axisY.setTickCount(tick)

    def initSerie(self):
        self.curve.clear()

    def initSeries(self):
        self.curve[0].clear()
        self.curve[1].clear()
