#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import GeneralConfig

class TestGeneralConfig:

    def setup_class(cls):
        cls.config = GeneralConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.configVersion is None
        assert self.config.site is None
        assert self.config.autorun is False
        assert self.config.timezone == "UTC"

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert ("configVersion" in config_dict["general"]) is False
        assert ("site" in config_dict["general"]) is False
        assert config_dict["general"]["autorun"] is False
        assert config_dict["general"]["timezone"] == "UTC"

    def test_fromDict(self):
        config_dict = {"general": {}}
        config_dict["general"]["configVersion"] = "1.3.3"
        config_dict["general"]["site"] = "Cerro Pachon"
        config_dict["general"]["autorun"] = True
        config_dict["general"]["timezone"] = "CLT"
        self.config.fromDict(config_dict)
        assert self.config.configVersion == config_dict["general"]["configVersion"]
        assert self.config.site == config_dict["general"]["site"]
        assert self.config.autorun is config_dict["general"]["autorun"]
        assert self.config.timezone == config_dict["general"]["timezone"]
