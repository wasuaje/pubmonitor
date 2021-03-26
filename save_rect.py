# -*- coding: utf-8 -*-

"""
Module implementing SaveRect.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from ui.Ui_save_rect import Ui_SaveRect

class SaveRect(QDialog, Ui_SaveRect):
	"""
	Class documentation goes here.
	"""	
	def __init__(self, parent = None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.FillCombo()		
		
	def reject(self):	
		self.done(0)

	def accept(self):	
		self.done(0)
		#sys.exit()
		
	def FillCombo(self):		
		self.comboBox.addItem('Juan')
		self.comboBox.addItem('Maria')
		self.comboBox.addItem('Petra')
		self.comboBox.addItem('Wuelfhis')
		
		print self.comboBox.currentIndex()
		print self.comboBox.currentText()
		print self.comboBox.count()
		
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = SaveRect()
    ui.show()
    sys.exit(app.exec_())
