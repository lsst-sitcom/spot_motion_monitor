#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from . import CameraConfig

__all__ = ['VimbaCameraConfig']

class VimbaCameraConfig(CameraConfig):
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
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.modelName = None
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
        self.roiFluxMinimum = config["roi"]["fluxMin"]
        self.roiExposureTime = config["roi"]["exposureTime"]
        self.fullExposureTime = config["full"]["exposureTime"]
        self.cameraIndex = config["cameraIndex"]
        super().fromDict(config)

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
        config = super().toDict(writeEmpty)
        if writeEmpty or self.modelName is not None:
            config["modelName"] = self.modelName
        config["roi"]["fluxMin"] = self.roiFluxMinimum
        config["roi"]["exposureTime"] = self.roiExposureTime
        config["full"]["exposureTime"] = self.fullExposureTime
        return config
