# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wasuaje/Documentos/desarrollo/pubmonitor/ui/save_rect.ui'
#
# Created: Tue May 24 13:30:37 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SaveRect(object):
    def setupUi(self, SaveRect):
        SaveRect.setObjectName(_fromUtf8("SaveRect"))
        SaveRect.resize(453, 342)
        self.buttonBox = QtGui.QDialogButtonBox(SaveRect)
        self.buttonBox.setGeometry(QtCore.QRect(260, 290, 181, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBox = QtGui.QComboBox(SaveRect)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 241, 27))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(SaveRect)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveRect.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveRect.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveRect)

    def retranslateUi(self, SaveRect):
        SaveRect.setWindowTitle(QtGui.QApplication.translate("SaveRect", "Guardar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SaveRect = QtGui.QDialog()
    ui = Ui_SaveRect()
    ui.setupUi(SaveRect)
    SaveRect.show()
    sys.exit(app.exec_())

