#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import sys

from PyQt5 import QtWidgets

from views import ui_main_window

class SpotMotionMonitor(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):

    def __init__(self, parent=None):
        super(SpotMotionMonitor, self).__init__(parent)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.close)

def main():
    """
    This is the entrance point of the program
    """
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName("LSST-Systems-Engineering")
    app.setOrganizationDomain("lsst.org")
    app.setApplicationName("Spot Motion Monitor")
    form = SpotMotionMonitor()
    form.show()
    app.exec_()
