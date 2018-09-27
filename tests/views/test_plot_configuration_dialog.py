#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import PlotConfigurationDialog

class TestPlotConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        pcDialog = PlotConfigurationDialog()
        qtbot.addWidget(pcDialog)
        pcDialog.show()

        assert pcDialog.tabWidget.count() == 2
