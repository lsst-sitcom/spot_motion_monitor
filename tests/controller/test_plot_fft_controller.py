#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.controller import PlotFftController
from spot_motion_monitor.views import FftWaterfallPlotWidget

class TestPlotFftController:

    def test_parametersAfterContruction(self, qtbot):
        fftx = FftWaterfallPlotWidget()
        ffty = FftWaterfallPlotWidget()
        qtbot.addWidget(fftx)
        qtbot.addWidget(ffty)

        pfc = PlotFftController(fftx, ffty)
        assert pfc.fftXPlot is not None
        assert pfc.fftYPlot is not None

    def test_parametersAfterSetup(self, qtbot):
        fftx = FftWaterfallPlotWidget()
        ffty = FftWaterfallPlotWidget()
        qtbot.addWidget(fftx)
        qtbot.addWidget(ffty)

        arraySize = 5
        pfc = PlotFftController(fftx, ffty)
        pfc.setup(arraySize)
        assert pfc.fftXPlot.arraySize == arraySize
        assert pfc.fftYPlot.arraySize == arraySize

    def test_update(self, qtbot, mocker):
        fftx = FftWaterfallPlotWidget()
        ffty = FftWaterfallPlotWidget()
        qtbot.addWidget(fftx)
        qtbot.addWidget(ffty)

        arraySize = 5
        pfc = PlotFftController(fftx, ffty)
        pfc.setup(arraySize)

        np.random.seed(3000)
        fftDataX = np.random.random(7)
        fftDataY = np.random.random(7)
        freqs = np.random.random(7)

        mockFftXPlotUpdatePlot = mocker.patch.object(pfc.fftXPlot, 'updatePlot')
        mockFftYPlotUpdatePlot = mocker.patch.object(pfc.fftYPlot, 'updatePlot')
        pfc.update(fftDataX, fftDataY, freqs)

        assert mockFftXPlotUpdatePlot.call_count == 1
        assert mockFftYPlotUpdatePlot.call_count == 1

    def test_badFftData(self, qtbot, mocker):
        fftx = FftWaterfallPlotWidget()
        ffty = FftWaterfallPlotWidget()
        qtbot.addWidget(fftx)
        qtbot.addWidget(ffty)

        arraySize = 5
        pfc = PlotFftController(fftx, ffty)
        pfc.setup(arraySize)

        mockFftXPlotUpdatePlot = mocker.patch.object(pfc.fftXPlot, 'updatePlot')
        mockFftYPlotUpdatePlot = mocker.patch.object(pfc.fftYPlot, 'updatePlot')
        pfc.update(None, None, None)

        assert mockFftXPlotUpdatePlot.call_count == 0
        assert mockFftYPlotUpdatePlot.call_count == 0
