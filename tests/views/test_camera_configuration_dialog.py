#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt

from spot_motion_monitor.views import CameraConfigurationDialog

class TestCameraConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'Gaussian'

    def test_setCameraConfiguration(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        config = {'roiSize': 30, 'doSpotOscillation': True,
                  'xAmplitude': 2, 'xFrequency': 50.0,
                  'yAmplitude': 7, 'yFrequency': 25.0,
                  'deltaTime': 300}

        ccDialog.setCameraConfiguration(config)
        assert int(ccDialog.cameraConfigTab.roiSizeLineEdit.text()) == config['roiSize']
        state = ccDialog.cameraConfigTab.spotOscillationCheckBox.checkState()
        boolState = True if state == Qt.Checked else False
        assert boolState == config['doSpotOscillation']