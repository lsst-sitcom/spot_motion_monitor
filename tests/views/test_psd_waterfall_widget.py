#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.views import PsdWaterfallPlotWidget

class TestPsdWaterfallPlotWidget:

    def setImage(*args):
        # args[0] is test class instance
        # args[1] is argument to ImageItem::setImage call
        args[0].pwpw1.image.image = args[1]

    def setup_class(cls):
        cls.pwpw1 = PsdWaterfallPlotWidget()
        cls.timeScale = 10

    def test_parametersAfterConstruction(self, qtbot):
        pwpw = PsdWaterfallPlotWidget()
        qtbot.addWidget(pwpw)
        assert pwpw.image is not None
        assert pwpw.data is None
        assert pwpw.arraySize is None
        assert pwpw.boundingRect is None
        assert pwpw.timeScale is None

    def test_parametersAfterSetup(self, qtbot):
        pwpw = PsdWaterfallPlotWidget()
        qtbot.addWidget(pwpw)
        arraySize = 5
        pwpw.setup(arraySize, self.timeScale)
        assert pwpw.arraySize == arraySize
        assert pwpw.timeScale == self.timeScale

    def test_parametersAfterUpdatePlot(self, qtbot, mocker):
        qtbot.addWidget(self.pwpw1)
        mockSetImage = mocker.patch.object(self.pwpw1.image, 'setImage')
        mockSetImage.side_effect = self.setImage
        arraySize = 3
        self.pwpw1.setup(arraySize, self.timeScale)
        p1 = np.arange(5, dtype=float)
        p2 = np.arange(5, 10, dtype=float)
        p3 = np.linspace(0.2, 1.2, 5)

        self.pwpw1.updatePlot(p1, p3)
        assert self.pwpw1.data.shape == (arraySize, p1.size)
        assert (self.pwpw1.data[0, ...] == p1).all()
        assert mockSetImage.call_count == 1
        rectCoords = self.pwpw1.boundingRect.getCoords()
        assert rectCoords[0] == 0
        assert rectCoords[1] == 0
        assert rectCoords[2] == 1.2
        assert rectCoords[3] == 30

        self.pwpw1.updatePlot(p2, p3)
        assert (self.pwpw1.data[0, ...] == p2).all()
        assert (self.pwpw1.data[1, ...] == p1).all()
        assert mockSetImage.call_count == 2