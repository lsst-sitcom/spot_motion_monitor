#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['CentroidPlotConfig']

class CentroidPlotConfig(BaseConfig):
    """Class for handling the configuration of the centroid plots (1D line,
       scatter and 1D histogram)

    Attributes
    ----------
    autoscaleX : bool
        Set autoscaling on the x component 1D centroid line plot.
    autoscaleY : bool
        Set autoscaling on the y component 1D centroid line plot.
    maximumX : int
        Set the maximum y axis value for on the x component 1D centroid line
        plot.
    maximumY : int
        Set the maximum y axis value for on the y component 1D centroid line
        plot.
    minimumX : int
        Set the minimum y axis value for on the x component 1D centroid line
        plot.
    minimumY : int
        Set the minimum y axis value for on the y component 1D centroid line
        plot.
    numHistogramBins : int
        Set the number of histogram bins on the 1D centroid histogram plots.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.autoscaleX = False
        self.minimumX = 0
        self.maximumX = 100
        self.autoscaleY = False
        self.minimumY = 0
        self.maximumY = 100
        self.numHistogramBins = 40
