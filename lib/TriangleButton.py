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

from PyQt5.QtCore import QPointF, pyqtProperty
from PyQt5.QtGui import QColor, QPainter, QPen, QLinearGradient, QBrush, QPolygonF
from PyQt5.QtWidgets import QAbstractButton


class TriangleButton(QAbstractButton):

    def __init__(self, size, direction, parent=None):
        QAbstractButton.__init__(self, parent)

        self.size = size
        self.direction = direction

        self.setMinimumSize(24, 24)
        self.setCheckable(True)
        self.setFixedWidth(size)
        self.setFixedHeight(size)

        # Green
        self.on_color_1 = QColor(0, 255, 0)
        self.on_color_2 = QColor(0, 192, 0)
        self.off_color_1 = QColor(0, 28, 0)
        self.off_color_2 = QColor(0, 128, 0)

    def resizeEvent(self, QResizeEvent):
        self.update()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        pen = QPen()

        if self.direction == 'forward':
            trianglePointsF = [
                QPointF(self.size * 0.05, self.size * 0.05),
                QPointF(self.size - (self.size * 0.05), self.size / 2),
                QPointF(self.size * 0.05, self.size - (self.size * 0.05))
            ]

            # gradientPen = QLinearGradient(QPointF(0, 0), QPointF(100, 100))
            gradient = QLinearGradient(0, 0, 100, 100)

        else:
            trianglePointsF = [
                QPointF(self.size - (self.size * 0.05), self.size * 0.05),
                QPointF(self.size * 0.05, self.size / 2),
                QPointF(self.size - (self.size * 0.05), self.size - (self.size * 0.05))
            ]

            # gradientPen = QLinearGradient(100, 0, 0, 100)
            gradient = QLinearGradient(100, 0, 0, 100)

        pen.setWidth(self.size * 0.04)

        painter.setRenderHint(QPainter.Antialiasing)

        if self.isChecked():
            # gradientPen.setColorAt(0, QColor(189, 189, 189))
            # gradientPen.setColorAt(1, QColor(110, 110, 110))
            color = QColor(110, 110, 110)

            gradient.setColorAt(0, self.on_color_1)
            gradient.setColorAt(1, self.on_color_2)

        else:
            # gradientPen.setColorAt(1, QColor(189, 189, 189))
            # gradientPen.setColorAt(0, QColor(110, 110, 110))
            color = QColor(189, 189, 189)

            gradient.setColorAt(0, self.off_color_1)
            gradient.setColorAt(1, self.off_color_2)

        pen.setBrush(QBrush(color))
        painter.setPen(pen)

        painter.setBrush(gradient)

        triangleF = QPolygonF(trianglePointsF)

        basePoly = QPolygonF(triangleF)
        painter.drawPolygon(basePoly)

    @pyqtProperty(QColor)
    def onColor1(self):
        return self.on_color_1

    @onColor1.setter
    def onColor1(self, color):
        self.on_color_1 = color

    @pyqtProperty(QColor)
    def onColor2(self):
        return self.on_color_2

    @onColor2.setter
    def onColor2(self, color):
        self.on_color_2 = color

    @pyqtProperty(QColor)
    def offColor1(self):
        return self.off_color_1

    @offColor1.setter
    def offColor1(self, color):
        self.off_color_1 = color

    @pyqtProperty(QColor)
    def offColor2(self):
        return self.off_color_2

    @offColor2.setter
    def offColor2(self, color):
        self.off_color_2 = color
