#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import os

from . import BaseConfig

__all__ = ['GeneralConfig']

class GeneralConfig(BaseConfig):
    """Class that handles the configuration of general information.

    Attributes
    ----------
    autorun : bool
        Run application in ROI mode at launch.
    configVersion : str
        The current version of the configuration, if applicable.
    fullTelemetrySavePath : str
        The full path for where to save the telemetry files.
    removeTelemetryDir : bool
        Whether or not to remove the telemetry directory when ROI acquisition
        ends.
    removeTelemetryFiles : bool
        Whether or not to remove the telemetry files when ROI acquisition ends.
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
        self.configVersion = config["general"]["configVersion"]
        self.site = config["general"]["site"]
        self.autorun = config["general"]["autorun"]
        self.timezone = config["general"]["timezone"]
        try:
            td = config["general"]["telemetry"]["directory"]
            if td is not None:
                self.fullTelemetrySavePath = os.path.abspath(os.path.expanduser(td))
            else:
                self.fullTelemetrySavePath = td
        except KeyError:
            pass
        self.removeTelemetryDir = config["general"]["telemetry"]["cleanup"]["directory"]
        self.removeTelemetryFiles = config["general"]["telemetry"]["cleanup"]["files"]

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
        config = {"general": {}}
        if writeEmpty or self.configVersion is not None:
            config["general"]["configVersion"] = self.configVersion
        if writeEmpty or self.site is not None:
            config["general"]["site"] = self.site
        config["general"]["autorun"] = self.autorun
        config["general"]["timezone"] = self.timezone
        config["general"]["telemetry"] = {}
        if writeEmpty or self.fullTelemetrySavePath is not None:
            config["general"]["telemetry"]["directory"] = self.fullTelemetrySavePath
        config["general"]["telemetry"]["cleanup"] = {}
        config["general"]["telemetry"]["cleanup"]["directory"] = self.removeTelemetryDir
        config["general"]["telemetry"]["cleanup"]["files"] = self.removeTelemetryFiles
        return config
