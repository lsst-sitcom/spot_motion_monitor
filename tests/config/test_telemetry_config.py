#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import TelemetryConfig

class TestTelemetryConfig:

    def setup_class(cls):
        cls.config = TelemetryConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.fullTelemetrySavePath is None
        assert self.config.removeTelemetryDir is True
        assert self.config.removeTelemetryFiles is True

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert ("directory" in config_dict["telemetry"]) is False
        assert config_dict["telemetry"]["cleanup"]["directory"] is True
        assert config_dict["telemetry"]["cleanup"]["files"] is True

    def test_fromDict(self):
        config_dict = {"telemetry": {}}
        config_dict["telemetry"]["directory"] = "/new/path/for/telemetry"
        config_dict["telemetry"]["cleanup"] = {}
        config_dict["telemetry"]["cleanup"]["directory"] = False
        config_dict["telemetry"]["cleanup"]["files"] = False
        self.config.fromDict(config_dict)
        assert self.config.fullTelemetrySavePath == config_dict["telemetry"]["directory"]
        assert self.config.removeTelemetryDir is config_dict["telemetry"]["cleanup"]["directory"]
        assert self.config.removeTelemetryFiles is config_dict["telemetry"]["cleanup"]["files"]
