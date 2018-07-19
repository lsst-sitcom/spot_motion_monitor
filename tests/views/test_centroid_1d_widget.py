#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import Centroid1dPlotWidget

class TestCentroid1dPlotWidget():

    def test_parametersAfterConstruction(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        qtbot.addWidget(c1dpw)
        assert c1dpw.curve is None
        assert c1dpw.dataSize is None
        assert c1dpw.data is None
        assert c1dpw.dataCounter == 0
        assert c1dpw.rollArray is False

    def test_parametersAfterSetup(self, qtbot):
        c1dpw = Centroid1dPlotWidget()
        qtbot.addWidget(c1dpw)
        arraySize = 1000
        c1dpw.setup(arraySize)
        assert c1dpw.curve is not None
        assert c1dpw.dataSize is arraySize
        assert c1dpw.data is not None
        assert c1dpw.rollArray is False

    def test_updatePlot(self, qtbot, mocker):
        c1dpw = Centroid1dPlotWidget()
        c1dpw.show()
        qtbot.addWidget(c1dpw)
        arraySize = 3
        c1dpw.setup(arraySize)
        mockSetData = mocker.patch.object(c1dpw.curve, 'setData')
        values = [254.43, 254.86, 253.91, 254.21]
        c1dpw.updatePlot(values[0])
        assert c1dpw.data.tolist() == [values[0]]
        assert c1dpw.dataCounter == 1
        c1dpw.updatePlot(values[1])
        c1dpw.updatePlot(values[2])
        assert c1dpw.data.tolist() == values[:-1]
        assert c1dpw.dataCounter == arraySize
        assert c1dpw.rollArray is True
        c1dpw.updatePlot(values[3])
        assert c1dpw.data.tolist() == values[1:]
        assert c1dpw.dataCounter == arraySize
        assert c1dpw.rollArray is True
        assert mockSetData.call_count == len(values)
