#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import VimbaCameraConfigTab

class TestVimbaCameraConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        gcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'Vimba'
