#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['PlotCentroidController']

class PlotCentroidController():

    """This class handles the interactions between the main program and the
       1D centroid plots.

    Attributes
    ----------
    xplot : .GraphicsLayoutWidget
        The 1D plot of the x pixel coordinate of the centroid.
    yplot : .GraphicsLayoutWidget
        The 1D plot of the y pixel coordinate of the centroid.
    """

    def __init__(self, cxp, cyp):
        """Initialize the class.

        Parameters
        ----------
        cxp : .GraphicsLayoutWidget
            The instance of the x centroid plot.
        cyp : .GraphicsLayoutWidget
            The instance of the y centroid plot.
        """
        self.xplot = cxp
        self.yplot = cyp

    def update(self, cx, cy):
        """Update the x and y centroid plots with current values.

        Parameters
        ----------
        cx : float
            The x pixel coordinate of the centroid.
        cy : float
            The y pixel coordinate of the centroid.
        """
        if cx is None or cy is None:
            return
        self.xplot.updatePlot(cx)
        self.yplot.updatePlot(cy)
