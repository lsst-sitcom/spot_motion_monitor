#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt

import spot_motion_monitor.utils as utils

class TestConfigHelpers:

    def test_boolToCheckState(self):
        assert utils.boolToCheckState(False) == Qt.Unchecked
        assert utils.boolToCheckState(True) == Qt.Checked

    def test_checkStateToBool(self):
        assert utils.checkStateToBool(Qt.Checked) is True
        assert utils.checkStateToBool(Qt.Unchecked) is False

    def test_noneToDefault(self):
        value = None
        assert utils.noneToDefaultOrValue(value) == ''
        default = 'None'
        assert utils.noneToDefaultOrValue(value, default=default) == default
        value = 100
        assert utils.noneToDefaultOrValue(value) == value
