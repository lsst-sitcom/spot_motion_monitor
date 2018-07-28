#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.views import FftWaterfallPlotWidget

class TestFftWaterfallPlotWidget:

    def test_parametersAfterConstruction(self, qtbot):
        fwpw = FftWaterfallPlotWidget()
        qtbot.addWidget(fwpw)
        assert fwpw.image is not None
        assert fwpw.data is None
        assert fwpw.arraySize is None

    def test_parametersAfterSetup(self, qtbot):
        fwpw = FftWaterfallPlotWidget()
        qtbot.addWidget(fwpw)
        arraySize = 5
        fwpw.setup(arraySize)
        assert fwpw.arraySize == arraySize

    def test_parametersAfterUpdatePlot(self, qtbot, mocker):
        fwpw = FftWaterfallPlotWidget()
        qtbot.addWidget(fwpw)
        mockSetImage = mocker.patch.object(fwpw.image, 'setImage')
        arraySize = 3
        fwpw.setup(arraySize)
        f1 = np.arange(5, dtype=float)
        f2 = np.arange(5, 10, dtype=float)
        f3 = np.linspace(0.2, 1.2, 5)

        fwpw.updatePlot(f1, f3)
        assert fwpw.data.shape == (arraySize, f1.size)
        assert (fwpw.data[0, ...] == f1).all()
        assert mockSetImage.call_count == 1

        fwpw.updatePlot(f2, f3)
        assert (fwpw.data[0, ...] == f2).all()
        assert (fwpw.data[1, ...] == f1).all()
        assert mockSetImage.call_count == 2
