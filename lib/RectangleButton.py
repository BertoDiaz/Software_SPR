from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RectangleButton(QAbstractButton):

    def __init__(self, size, parent=None):
        QAbstractButton.__init__(self, parent)

        self.size = size

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

        rectanglePointsF = [
            QPointF(self.size * 0.05, self.size * 0.05),
            QPointF(self.size - (self.size * 0.05), self.size * 0.05),
            QPointF(self.size - (self.size * 0.05), self.size - (self.size * 0.05)),
            QPointF(self.size * 0.05, self.size - (self.size * 0.05))
        ]

        gradient = QLinearGradient(0, 0, 100, 100)

        pen.setWidth(self.size * 0.04)

        painter.setRenderHint(QPainter.Antialiasing)

        if self.isChecked():
            color = QColor(110, 110, 110)

            gradient.setColorAt(0, self.on_color_1)
            gradient.setColorAt(1, self.on_color_2)

        else:
            color = QColor(189, 189, 189)

            gradient.setColorAt(0, self.off_color_1)
            gradient.setColorAt(1, self.off_color_2)

        pen.setBrush(QBrush(color))
        painter.setPen(pen)

        painter.setBrush(gradient)

        triangleF = QPolygonF(rectanglePointsF)

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
