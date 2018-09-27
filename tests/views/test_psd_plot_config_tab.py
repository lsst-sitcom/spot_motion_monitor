#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import PsdPlotConfigTab

class TestPsdPlotConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        configTab = PsdPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'PSD'
