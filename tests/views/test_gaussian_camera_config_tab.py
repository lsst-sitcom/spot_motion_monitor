#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import GaussianCameraConfigTab

class TestGaussianCameraConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'Gaussian'
        assert gcConfigTab.spotOscillationCheckBox.isChecked() is False
        assert gcConfigTab.spotOscillationGroupBox.isEnabled() is False
