#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
from pyqtgraph import GraphicsLayoutWidget, ScatterPlotItem

__all__ = ['CentroidScatterPlotWidget']

class CentroidScatterPlotWidget(GraphicsLayoutWidget):

    """Summary

    Attributes
    ----------
    dataCounter : int
        Number of times data arrays have been appended to up until array size.
    dataSize : TYPE
        The requested size of the data arrays.
    rollArray : bool
        Flag as to when to start rolling the data arrays of centroid values.
    scatterPlot : TYPE
        Instance of the centroid scatter plot.
    xData : numpy.array
        Container for the x coordinate of the centroid.
    yData : TYPE
        Container for the y coordinate of the centroid.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)

        p2 = self.addPlot()
        self.scatterPlot = ScatterPlotItem()
        p2.addItem(self.scatterPlot)

        self.dataSize = None
        self.xData = None
        self.yData = None
        self.rollArray = False
        self.dataCounter = 0

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
        else:
            # This does create copies of arrays, so watch performance.
            self.xData = np.append(self.xData, centroidX)
            self.yData = np.append(self.yData, centroidY)

        self.scatterPlot.setData(self.xData, self.yData)

        if self.dataCounter < self.dataSize:
            self.dataCounter += 1
            if self.dataCounter == self.dataSize:
                self.rollArray = True
