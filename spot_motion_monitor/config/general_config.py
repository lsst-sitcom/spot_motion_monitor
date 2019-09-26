#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['GeneralConfig']

class GeneralConfig(BaseConfig):
    """Class that handles the configuration of general information.

    Attributes
    ----------
    autorun : bool
        Run application in ROI mode at launch.
    configVersion : str
        The current version of the configuration, if applicable.
    site : str
        The location the program is used.
    timezone : str
        The timezone to use for all dates and times.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.configVersion = None
        self.site = None
        self.autorun = False
        self.timezone = "UTC"

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.configVersion = config["general"]["configVersion"]
        self.site = config["general"]["site"]
        self.autorun = config["general"]["autorun"]
        self.timezone = config["general"]["timezone"]

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"general": {}}
        if self.configVersion is not None:
            config["general"]["configVersion"] = self.configVersion
        if self.site is not None:
            config["general"]["site"] = self.site
        config["general"]["autorun"] = self.autorun
        config["general"]["timezone"] = self.timezone
        return config
