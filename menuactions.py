# -*- coding: utf-8 -*-

"""
Module implementing MenuActions.
"""

from PyQt4.QtGui import QMainWindow, QDialog, QTreeView, QDirModel, QGraphicsScene, QGraphicsPixmapItem, QPixmap, QRubberBand
from PyQt4.QtCore import pyqtSignature, QRect,  QSize
from PyQt4 import QtCore, QtGui
from ui.Ui_prueba import Ui_MainWindow
from ui.Ui_confirm import Ui_Dialog
#from ui.Ui_save_rect import Ui_SaveRect
from save_rect import SaveRect
import sys

class ShowCloseDialog(QDialog):
  def __init__(self, parent=None):    
    QDialog.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)

  def reject(self):	
	self.done(0)
	
  def accept(self):	
	sys.exit()

#class ShowSaveRectDialog(QDialog):
#  def __init__(self, parent=None):    
#		QDialog.__init__(self, parent)
#		#self.ui = Ui_SaveRect()
#		self.ui = SaveRect()
#		self.ui.setupUi(self)


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
		self.popDialog=ShowCloseDialog(self)		
		self.saveDialog=SaveRect(self)		
		FillTreeview(self)
	
	@pyqtSignature("")
	def on_actionAbrir_triggered(self):
		raise NotImplementedError

	@pyqtSignature("")
	def on_actionSalir_triggered(self):
		"""
		Slot documentation goes here.
		"""
		self.popDialog.show()

	@pyqtSignature("QModelIndex")
	def on_treeView_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		#raise NotImplementedError
		FillTreeview2(self, index)
    
	@pyqtSignature("QModelIndex")
	def on_treeView2_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		#raise NotImplementedError
		filename = self.model2.filePath(index)		
		showimage(self, filename)

	@pyqtSignature("")
	def on_pushButton_released(self):
		"""
        Slot documentation goes here.
        """
        # TODO: not implemented yet        
		self.popDialog.show()
	
	def mousePressEvent(self,event):		
		self.origin = event.pos()				
		self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
		self.rubberBand.setGeometry(QRect(self.origin, QSize()))
		self.rubberBand.show()
		#print dir(self.rubberBand)
	
	def mouseMoveEvent(self,event):		
		self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
	
	def mouseReleaseEvent(self,event):				
		self.end=event.pos()
		self.rubberBand.hide();
		#determine selection, for example using QRect::intersects() and QRect::contains().
		print self.origin.x()		#punto x del origen en entero
		print self.end.y()			#punto x del final de la seleccion en entero
		self.saveDialog.show()	#muestro el dialogo para salvar los valores necesarios
		
		
def FillTreeview(self):
	"""
	LLeno el treview desde el directorio predeterminado
	"""
	self.model = QDirModel()
	self.tree = self.treeView
	self.tree.setModel(self.model)
	self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)		
	#self.tree.setSortingEnabled(True)
	self.tree.setRootIndex(self.model.index("/home/wasuaje/Documentos"))	
	self.tree.hideColumn(1)
	self.tree.hideColumn(2)
	self.tree.hideColumn(3)
	self.tree.show()
		
def FillTreeview2(self, index):
	self.model2 = QDirModel()
	self.tree2 = self.treeView2
	self.tree2.setModel(self.model2)
	ext=QtCore.QStringList()
	ext.append('*.jpg')
	ext.append('*.JPG')
	self.model2.setNameFilters(ext)
	self.model2.setFilter(QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)		
	newroot = self.model.filePath(index)
	self.tree2.setRootIndex(self.model2.index(newroot))
	self.tree2.hideColumn(1)
	self.tree2.hideColumn(2)
	self.tree2.hideColumn(3)
	self.tree2.show()

def showimage(self, filename):
	#print filename		
	self.scene = QGraphicsScene()
	#view=self.graphicsView(scene)
	self.item = QGraphicsPixmapItem(QPixmap(filename))	
	self.scene.addItem(self.item)
	self.graphicsView.setScene(self.scene)
	self.graphicsView.show()
    #self.graphicsView.setPixmap(QtGui.QPixmap(filename))

		
