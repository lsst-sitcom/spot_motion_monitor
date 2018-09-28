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

    def test_setPlotConfiguration(self, qtbot):
        pcDialog = PlotConfigurationDialog()
        qtbot.addWidget(pcDialog)
        pcDialog.show()

        centroidConfig = {'xCentroid': {'autoscale': False, 'minimum': 10, 'maximum': 1000},
                          'yCentroid': {'autoscale': True, 'minimum': None, 'maximum': None},
                          'scatterPlot': {'numHistogramBins': 50}}
        psdConfig = {'waterfall': {'numBins': 15, 'colorMap': None}}

        pcDialog.setPlotConfiguration(centroidConfig, psdConfig)
        assert pcDialog.centroidPlotConfigTab.minYLimitLineEdit.text() == ''
        value = int(pcDialog.psdPlotConfigTab.waterfallNumBinsLineEdit.text())
        assert value == psdConfig['waterfall']['numBins']
