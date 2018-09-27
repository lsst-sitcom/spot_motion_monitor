#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import CameraConfigurationDialog

class TestCameraConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'Gaussian'
