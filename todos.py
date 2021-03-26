# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication, QRubberBand, QWidget
from PyQt4.QtCore import QPoint, QRect, QSize
from sys import argv
  
class mw(QWidget):
    def __init__(self):
        QWidget.__init__(self)
  
    def mousePressEvent(self,event):
        self.p_initial = event.globalPos()
        self.p_rb = QRubberBand(QRubberBand.Rectangle, self)
