# -*- coding: utf-8 -*-

"""
Module implementing MenuActions.
"""

from PyQt4.QtGui import QMainWindow, QDialog
from PyQt4.QtCore import pyqtSignature
from ui.Ui_prueba import Ui_MainWindow
from ui.Ui_confirm import Ui_Dialog
import sys

class CloseDialog(QDialog):
  def __init__(self, parent=None):    
    QDialog.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)

  def reject(self):	
	self.done(0)
	
  def accept(self):	
	sys.exit()

class MenuActions(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
		"""
		Constructor
		"""
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.popDialog=CloseDialog(self)
		
    @pyqtSignature("")
    def on_actionAbrir_triggered(self):
        """
        Slot documentation goes here.
        """
        #print prueba
        # TODO: not implemented yet
        raise NotImplementedError
    	
    def on_actionSalir_triggered(self):
		"""
		Slot documentation goes here.
		"""
		self.popDialog.show()
