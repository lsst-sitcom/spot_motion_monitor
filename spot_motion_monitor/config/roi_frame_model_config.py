#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['RoiFrameModelConfig']

class RoiFrameModelConfig(BaseConfig):
    """Class that handles the configuration of the ROI frame model.

    Attributes
    ----------
    thresholdFactor : float
        The scale factor multiplied by the frame max and then subtracted from
        the frame.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.thresholdFactor = 0.3

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.thresholdFactor = config["roiFrame"]["thresholdFactor"]

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roiFrame": {}}
        config["roiFrame"]["thresholdFactor"] = self.thresholdFactor
        return config
