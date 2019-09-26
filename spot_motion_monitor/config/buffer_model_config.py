#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['BufferModelConfig']

class BufferModelConfig(BaseConfig):
    """Class that handles the configuration of the buffer model.

    Attributes
    ----------
    bufferSize : int
        Size of the buffer for data storage. Should be power of 2.
    pixelScale : float
        Pixel scale in arcseconds per pixel of the optical system in front of
        the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.bufferSize = 1024
        self.pixelScale = 1.0

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.bufferSize = config["buffer"]["size"]
        self.pixelScale = config["buffer"]["pixelScale"]

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"buffer": {}}
        config["buffer"]["size"] = self.bufferSize
        config["buffer"]["pixelScale"] = self.pixelScale
        return config
