#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.views import PsdWaterfallPlotWidget

class TestPsdWaterfallPlotWidget:

    def test_parametersAfterConstruction(self, qtbot):
        pwpw = PsdWaterfallPlotWidget()
        qtbot.addWidget(pwpw)
        assert pwpw.image is not None
        assert pwpw.data is None
        assert pwpw.arraySize is None

    def test_parametersAfterSetup(self, qtbot):
        pwpw = PsdWaterfallPlotWidget()
        qtbot.addWidget(pwpw)
        arraySize = 5
        pwpw.setup(arraySize)
        assert pwpw.arraySize == arraySize

    def test_parametersAfterUpdatePlot(self, qtbot, mocker):
        pwpw = PsdWaterfallPlotWidget()
        qtbot.addWidget(pwpw)
        mockSetImage = mocker.patch.object(pwpw.image, 'setImage')
        arraySize = 3
        pwpw.setup(arraySize)
        p1 = np.arange(5, dtype=float)
        p2 = np.arange(5, 10, dtype=float)
        p3 = np.linspace(0.2, 1.2, 5)

        pwpw.updatePlot(p1, p3)
        assert pwpw.data.shape == (arraySize, p1.size)
        assert (pwpw.data[0, ...] == p1).all()
        assert mockSetImage.call_count == 1

        pwpw.updatePlot(p2, p3)
        assert (pwpw.data[0, ...] == p2).all()
        assert (pwpw.data[1, ...] == p1).all()
        assert mockSetImage.call_count == 2
