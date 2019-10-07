#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['FullFrameModelConfig']

class FullFrameModelConfig(BaseConfig):
    """Class that handles the configuration of the full frame model.

    Attributes
    ----------
    minimumNumPixels : int
        The minimum number of pixels that must be in an object.
    sigmaScale : float
        Multiplier for the frame standard deviation.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.sigmaScale = 5.0
        self.minimumNumPixels = 10

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.check("sigmaScale", config["fullFrame"], "sigmaScale")
        self.check("minimumNumPixels", config["fullFrame"], "minimumNumPixels")

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"fullFrame": {}}
        config["fullFrame"]["sigmaScale"] = self.sigmaScale
        config["fullFrame"]["minimumNumPixels"] = self.minimumNumPixels
        return config
