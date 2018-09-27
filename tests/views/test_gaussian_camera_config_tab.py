#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt

from spot_motion_monitor.views import GaussianCameraConfigTab

class TestGaussianCameraConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        assert gcConfigTab.name == 'Gaussian'
        assert gcConfigTab.spotOscillationCheckBox.isChecked() is False
        assert gcConfigTab.spotOscillationGroupBox.isEnabled() is False

    def test_setParametersFromConfiguration(self, qtbot):
        gcConfigTab = GaussianCameraConfigTab()
        qtbot.addWidget(gcConfigTab)

        config = {'roiSize': 30, 'doSpotOscillation': False,
                  'xAmplitude': 2, 'xFrequency': 50.0,
                  'yAmplitude': 7, 'yFrequency': 25.0,
                  'deltaTime': 300}

        gcConfigTab.setConfiguration(config)
        assert int(gcConfigTab.roiSizeLineEdit.text()) == config['roiSize']
        state = gcConfigTab.spotOscillationCheckBox.checkState()
        boolState = True if state == Qt.Checked else False
        assert boolState == config['doSpotOscillation']
        assert int(gcConfigTab.xAmpLineEdit.text()) == config['xAmplitude']
        assert float(gcConfigTab.xFreqLineEdit.text()) == config['xFrequency']
        assert int(gcConfigTab.yAmpLineEdit.text()) == config['yAmplitude']
        assert float(gcConfigTab.yFreqLineEdit.text()) == config['yFrequency']
        assert int(gcConfigTab.deltaTimeLineEdit.text()) == config['deltaTime']