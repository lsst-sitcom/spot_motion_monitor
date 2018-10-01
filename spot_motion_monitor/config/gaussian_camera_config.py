#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['GaussianCameraConfig']

class GaussianCameraConfig(BaseConfig):
    """Class that handles the configuration of the Gaussian camera.

    Attributes
    ----------
    deltaTime : int
        The time segmentation over on oscillation period.
    doSpotOscillation : bool
        Flag tp make the generated spot oscillate.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    xAmplitude : int
        The amplitude of the x component of the spot oscillation.
    xFrequency : float
        The frequency of the x component of the spot oscillation.
    yAmplitude : int
        The amplitude of the y component of the spot oscillation.
    yFrequency : float
        The frequency of the y component of the spot oscillation.
    """

    def __init__(self):
        """Summary
        """
        super().__init__()
        self.roiSize = 50
        self.doSpotOscillation = False
        self.xAmplitude = 10
        self.xFrequency = 5.0
        self.yAmplitude = 5
        self.yFrequency = 10.0
        self.deltaTime = 200
