#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['PsdPlotConfig']

class PsdPlotConfig(BaseConfig):
    """Class that handles the configuration of the Power Spectrum Distribution
       plots (1D and waterfall).

    Attributes
    ----------
    autoscaleX1d : bool
        Set autoscaling on the x component 1D PSD plot.
    autoscaleY1d : bool
        Set autoscaling on the y component 1D PSD plot.
    numWaterfallBins : int
        Set the number of vertical bins for the waterfall PSD plots.
    waterfallColorMap : str
        Set the color map for the waterfall PSD plots.
    x1dMaximum : int
        Set the maximum y axis value for on the x component 1D PSD plot.
    y1dMaximum : int
        Set the maximum y axis value for on the y component 1D PSD plot.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.autoscaleX1d = False
        self.x1dMaximum = 1000
        self.autoscaleY1d = False
        self.y1dMaximum = 1000
        self.numWaterfallBins = 25
        self.waterfallColorMap = 'viridis'
