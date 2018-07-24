#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.views import CentroidScatterPlotWidget

class TestCentroidScatterPlotWidget:

    def test_parametersAfterConstruction(self, qtbot):
        cspw = CentroidScatterPlotWidget()
        cspw.show()
        qtbot.addWidget(cspw)
        assert cspw.scatterPlot is not None
        assert cspw.dataSize is None
        assert cspw.xData is None
        assert cspw.yData is None
        assert cspw.rollArray is False
        assert cspw.dataCounter == 0

    def test_parametersAfterSetup(self, qtbot):
        cspw = CentroidScatterPlotWidget()
        qtbot.addWidget(cspw)
        arraySize = 1000
        cspw.setup(arraySize)
        assert cspw.scatterPlot is not None
        assert cspw.dataSize == arraySize
        assert cspw.xData is not None
        assert cspw.yData is not None
        assert cspw.rollArray is False
        assert cspw.dataCounter == 0

    def test_updatePlot(self, qtbot, mocker):
        cspw = CentroidScatterPlotWidget()
        cspw.show()
        qtbot.addWidget(cspw)
        arraySize = 3
        cspw.setup(arraySize)
        mockSetData = mocker.patch.object(cspw.scatterPlot, 'setData')
        valuesX = [254.43, 254.86, 253.91, 254.21]
        valuesY = [355.25, 355.10, 354.89, 355.57]
        cspw.updatePlot(valuesX[0], valuesY[0])
        assert cspw.xData.tolist() == [valuesX[0]]
        assert cspw.yData.tolist() == [valuesY[0]]
        assert cspw.dataCounter == 1
        cspw.updatePlot(valuesX[1], valuesY[1])
        cspw.updatePlot(valuesX[2], valuesY[2])
        assert cspw.xData.tolist() == valuesX[:-1]
        assert cspw.yData.tolist() == valuesY[:-1]
        assert cspw.dataCounter == arraySize
        assert cspw.rollArray is True
        cspw.updatePlot(valuesX[3], valuesY[3])
        assert cspw.xData.tolist() == valuesX[1:]
        assert cspw.yData.tolist() == valuesY[1:]
        assert cspw.dataCounter == arraySize
        assert cspw.rollArray is True
        assert mockSetData.call_count == len(valuesX)
