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

    def test_setParametersFromConfiguration(self, qtbot):
        gcConfigTab = VimbaCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        config = {'roiSize': 20, 'roiFluxMinimum': 1000, 'roiExposureTime': 5000}
        gcConfigTab.setConfiguration(config)

        assert int(gcConfigTab.roiSizeLineEdit.text()) == config['roiSize']
        assert int(gcConfigTab.roiFluxMinLineEdit.text()) == config['roiFluxMinimum']
        assert int(gcConfigTab.roiExposureTimeLineEdit.text()) == config['roiExposureTime']
