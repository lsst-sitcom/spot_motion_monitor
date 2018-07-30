#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
from PyQt5.QtWidgets import QWidget
from pyqtgraph import mkBrush, ScatterPlotItem

from spot_motion_monitor.views.ui_scatter_plot import Ui_ScatterPlot

__all__ = ['CentroidScatterPlotWidget']

class CentroidScatterPlotWidget(QWidget, Ui_ScatterPlot):

    """This class handles managing the centroid scatter plot and the histogram
       projections for both x and y coordinates.

    Attributes
    ----------
    brushColor : tuple
        The common color for all brushes in the widget.
    brushes : list
        A set of brushes with varying alpha.
    dataCounter : int
        Number of times data arrays have been appended to up until array size.
    dataSize : int
        The requested size of the data arrays.
    histogramFillBrush : QtGui.QBrush
        Brush used to fill the projection histograms.
    maxAlpha : int
        The maximum transparency value for a brush
    minAlpha : int
        The minimum transparency value for a brush.
    numBins : int
        Number of histogram bins for the projections.
    pointBrush : QtGui.QBrush
        The brush for the scatter plot points.
    rollArray : bool
        Flag as to when to start rolling the data arrays of centroid values.
    scatterPlotItem : pyqtgraph.ScatterPlotItem
        Instance of the centroid scatter plot.
    xData : numpy.array
        Container for the x coordinate of the centroid.
    xHistogramItem : pyqtgraph.PlotItem
        Instance of the x coordinate histogram projection.
    yData : numpy.array
        Container for the y coordinate of the centroid.
    yHistogramItem : pyqtgraph.PlotItem
        Instance of the y coordinate histogram projection.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)

        p1 = self.scatterPlot.addPlot()
        self.scatterPlotItem = ScatterPlotItem()
        p1.addItem(self.scatterPlotItem)
        p1.setLabel('left', 'Y', units='pixel')
        p1.setLabel('bottom', 'X', units='pixel')

        self.yHistogramItem = None
        self.xHistogramItem = None
        self.numBins = 40

        self.dataSize = None
        self.xData = None
        self.yData = None
        self.rollArray = False
        self.dataCounter = 0
        self.brushes = None
        self.brushColor = (159, 159, 159)
        self.maxAlpha = 255
        self.minAlpha = 127
        self.histogramFillBrush = mkBrush(*self.brushColor, 200)
        self.pointBrush = mkBrush(*self.brushColor, self.maxAlpha)
        self.scatterPlotItem.setBrush(self.pointBrush)

    def makeBrushes(self):
        """Make brushes for spots with differnet alpha factors.
        """
        self.brushes = []
        deltaAlpha = self.maxAlpha - self.minAlpha
        slope = deltaAlpha / (self.dataSize - 1)
        for i in range(self.dataSize):
            alpha = slope * i + self.minAlpha
            self.brushes.append(mkBrush(*self.brushColor, int(alpha)))
            #c = int(alpha)
            #self.brushes.append(mkBrush(c, c, c, self.maxAlpha))

    def setup(self, arraySize):
        """Provide information for setting up the plot.

        Parameters
        ----------
        arraySize : The size for the plot data arrays.
            Description
        """
        self.dataSize = arraySize
        self.xData = np.array([])
        self.yData = np.array([])
        self.makeBrushes()
        p1 = self.yHistogram.addPlot()
        self.yHistogramItem = p1.plot(self.yData, self.yData)
        self.yHistogramItem.rotate(90)
        p2 = self.xHistogram.addPlot()
        self.xHistogramItem = p2.plot(self.xData, self.xData)

    def updatePlot(self, centroidX, centroidY):
        """Update the plot with a new centroid coordinate pair.

        Parameters
        ----------
        centroidX : float
            The current x coordinate of the centroid to plot.
        centroidY : float
            The current y coordinate of the centroid to plot.
        """
        if self.rollArray:
            self.xData[:-1] = self.xData[1:]
            self.xData[-1] = centroidX
            self.yData[:-1] = self.yData[1:]
            self.yData[-1] = centroidY
            #brushes = self.brushes
        else:
            # This does create copies of arrays, so watch performance.
            self.xData = np.append(self.xData, centroidX)
            self.yData = np.append(self.yData, centroidY)
            # Get brushes from end of array since that's where newer data is at.
            # Many brushes causes performance issues.
            #brushes = self.brushes[:self.xData.size]

        self.scatterPlotItem.setData(self.xData, self.yData, pen=None)  # , brush=brushes)

        xy, xx = np.histogram(self.xData,
                              bins=np.linspace(np.min(self.xData), np.max(self.xData), self.numBins))
        self.xHistogramItem.setData(xx, xy, stepMode=True, fillLevel=0, fillBrush=self.histogramFillBrush)
        yy, yx = np.histogram(self.yData,
                              bins=np.linspace(np.min(self.yData), np.max(self.yData), self.numBins))
        # Flip due to rotated plot
        yy *= -1
        self.yHistogramItem.setData(yx, yy, stepMode=True, fillLevel=0, fillBrush=self.histogramFillBrush)

        if self.dataCounter < self.dataSize:
            self.dataCounter += 1
            if self.dataCounter == self.dataSize:
                self.rollArray = True
