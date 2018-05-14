#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from unittest import mock

from PyQt5.QtWidgets import QMainWindow

from spot_motion_monitor.views.main_window import SpotMotionMonitor

class TestMainWindow():

    def test_main_window_exit(self, qtbot):
        with mock.patch.object(QMainWindow, 'close') as mock_method:
            mw = SpotMotionMonitor()
            mw.show()
            qtbot.addWidget(mw)
            mw.actionExit.trigger()
            assert mock_method.call_count == 1
