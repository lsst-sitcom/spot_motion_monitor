#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.controller import Plot1dCentroidController
from spot_motion_monitor.views import Centroid1dPlotWidget

class TestPlot1dCentroidController:

    def setup_class(cls):
        cls.bufferSize = 3

    def test_parametersAfterConstruction(self, qtbot):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        cxp.setup(self.bufferSize)
        cyp.setup(self.bufferSize)

        p1cc = Plot1dCentroidController(cxp, cyp)
        assert p1cc.xplot is not None
        assert p1cc.yplot is not None

    def test_update(self, qtbot):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        cxp.setup(self.bufferSize)
        cyp.setup(self.bufferSize)

        p1cc = Plot1dCentroidController(cxp, cyp)
        centroidX = 253.543
        centroidY = 313.683
        p1cc.update(centroidX, centroidY)

        assert p1cc.xplot.data[0] == centroidX
        assert p1cc.yplot.data[0] == centroidY

    def test_badCentroidsUpdate(self, qtbot, mocker):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        cxp.setup(self.bufferSize)
        cyp.setup(self.bufferSize)
        mocker.patch('spot_motion_monitor.views.centroid_1d_plot_widget.Centroid1dPlotWidget.updatePlot')

        p1cc = Plot1dCentroidController(cxp, cyp)
        p1cc.update(None, None)
        assert p1cc.xplot.updatePlot.call_count == 0
        assert p1cc.yplot.updatePlot.call_count == 0
