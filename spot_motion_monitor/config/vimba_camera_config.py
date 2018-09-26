#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['VimbaCameraConfig']

class VimbaCameraConfig(BaseConfig):
    """Class that handles the configuration of the Vimba class cameras.

    Attributes
    ----------
    roiExposureTime : int
        The exposure time (microseconds) in ROI mode.
    roiFluxMinimum : int
        The mimium flux allowed in an ROI.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.roiSize = 50
        self.roiFluxMinimum = 2000
        self.roiExposureTime = 3000  # microseconds
