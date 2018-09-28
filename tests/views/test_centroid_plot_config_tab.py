#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt

from spot_motion_monitor.views import CentroidPlotConfigTab
from spot_motion_monitor.utils import checkStateToBool

class TestCentroidPlotConfigTab:

    def test_parametersAfterConstruction(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        assert configTab.name == 'Centroid'

    def test_setParametersFromConfiguration(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)

        config = {'xCentroid': {'autoscale': False, 'minimum': 10, 'maximum': 1000},
                  'yCentroid': {'autoscale': True, 'minimum': None, 'maximum': None},
                  'scatterPlot': {'numHistogramBins': 50}}

        configTab.setConfiguration(config)
        xState = checkStateToBool(configTab.useAutoScaleXCheckBox.checkState())
        assert xState is config['xCentroid']['autoscale']
        assert int(configTab.minXLimitLineEdit.text()) == config['xCentroid']['minimum']
        assert int(configTab.maxXLimitLineEdit.text()) == config['xCentroid']['maximum']
        yState = checkStateToBool(configTab.useAutoScaleYCheckBox.checkState())
        assert yState is config['yCentroid']['autoscale']
        assert configTab.minYLimitLineEdit.text() == ''
        assert configTab.maxYLimitLineEdit.text() == ''
        assert int(configTab.numHistoBinsLineEdit.text()) == config['scatterPlot']['numHistogramBins']

    def test_getParametersFromConfiguration(self, qtbot):
        configTab = CentroidPlotConfigTab()
        qtbot.addWidget(configTab)
        configTab.show()

        truthConfig = {'xCentroid': {'autoscale': False, 'minimum': 10, 'maximum': 1000},
                       'yCentroid': {'autoscale': True},
                       'scatterPlot': {'numHistogramBins': 30}}

        configTab.useAutoScaleXCheckBox.setChecked(Qt.Unchecked)
        configTab.minXLimitLineEdit.setText(str(truthConfig['xCentroid']['minimum']))
        configTab.maxXLimitLineEdit.setText(str(truthConfig['xCentroid']['maximum']))
        configTab.useAutoScaleYCheckBox.setChecked(Qt.Checked)
        configTab.numHistoBinsLineEdit.setText(str(truthConfig['scatterPlot']['numHistogramBins']))
        config = configTab.getConfiguration()
        assert config == truthConfig
