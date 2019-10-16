#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['VimbaCameraConfig']

class VimbaCameraConfig(BaseConfig):
    """Class that handles the configuration of the Vimba class cameras.

    Attributes
    ----------
    cameraIndex : int
        The current index of the camera if multiple present.
    fullExposureTime : int
        The exposure time (microseconds) in full frame mode.
    modelName : str
        A description of the camera model.
    roiExposureTime : int
        The exposure time (microseconds) in ROI mode.
    roiFluxMinimum : int
        The minimum flux allowed in an ROI.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.modelName = None
        self.roiSize = 50
        self.roiFluxMinimum = 2000
        self.roiExposureTime = 8000  # microseconds
        self.fullExposureTime = 8000  # microseconds
        self.cameraIndex = 0

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.modelName = config["modelName"]
        self.roiSize = config["roi"]["size"]
        self.roiFluxMinimum = config["roi"]["fluxMin"]
        self.roiExposureTime = config["roi"]["exposureTime"]
        self.fullExposureTime = config["full"]["exposureTime"]
        self.cameraIndex = config["cameraIndex"]

    def toDict(self, writeEmpty=False):
        """Translate class attributes to configuration dict.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roi": {}, "full": {}}
        if writeEmpty or self.modelName is not None:
            config["modelName"] = self.modelName
        config["roi"]["size"] = self.roiSize
        config["roi"]["fluxMin"] = self.roiFluxMinimum
        config["roi"]["exposureTime"] = self.roiExposureTime
        config["full"]["exposureTime"] = self.fullExposureTime
        return config
