#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import RoiFrameModelConfig

class TestRoiFrameModelConfig:

    def setup_class(cls):
        cls.config = RoiFrameModelConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.thresholdFactor == 0.3

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["roiFrame"]["thresholdFactor"] == 0.3

    def test_fromDict(self):
        config_dict = {"roiFrame": {}}
        config_dict["roiFrame"]["thresholdFactor"] = 0.5
        self.config.fromDict(config_dict)
        assert self.config.thresholdFactor == config_dict["roiFrame"]["thresholdFactor"]
