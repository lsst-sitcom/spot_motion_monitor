#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import os

from spot_motion_monitor.config import BaseConfig

__all__ = ['TelemetryConfig']

class TelemetryConfig(BaseConfig):
    """Class that handles the configuration of telemetry.

    Attributes
    ----------
    fullTelemetrySavePath : str
        The full path for where to save the telemetry files.
    removeTelemetryDir : bool
        Whether or not to remove the telemetry directory when ROI acquisition
        ends.
    removeTelemetryFiles : bool
        Whether or not to remove the telemetry files when ROI acquisition ends.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.fullTelemetrySavePath = None
        self.removeTelemetryDir = True
        self.removeTelemetryFiles = True

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        try:
            td = config["telemetry"]["directory"]
            self.fullTelemetrySavePath = os.path.abspath(os.path.expanduser(td))
        except KeyError:
            pass
        self.removeTelemetryDir = config["telemetry"]["cleanup"]["directory"]
        self.removeTelemetryFiles = config["telemetry"]["cleanup"]["files"]

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"telemetry": {}}
        if self.fullTelemetrySavePath is not None:
            config["telemetry"]["directory"] = self.fullTelemetrySavePath
        config["telemetry"]["cleanup"] = {}
        config["telemetry"]["cleanup"]["directory"] = self.removeTelemetryDir
        config["telemetry"]["cleanup"]["files"] = self.removeTelemetryFiles
        return config
