#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import CentroidPlotConfigTab

class TestCentroidPlotConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'Centroid'
