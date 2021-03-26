from PyQt4 import QtCore, QtGui
from menuactions import MenuActions

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MenuActions()
    ui.show()
    sys.exit(app.exec_())
