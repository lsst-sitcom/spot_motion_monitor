#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import PsdPlotConfig

class TestPsdPlotConfig:

    def setup_class(cls):
        cls.config = PsdPlotConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.autoscaleX1d is False
        assert self.config.x1dMinimum == 0
        assert self.config.x1dMaximum == 1000
        assert self.config.autoscaleY1d is False
        assert self.config.y1dMinimum == 0
        assert self.config.y1dMaximum == 1000
        assert self.config.numWaterfallBins == 25
        assert self.config.waterfallColorMap == "viridis"

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["xPSD"]["autoscaleY"] is False
        assert config_dict["xPSD"]["maximumY"] == 1000
        assert config_dict["yPSD"]["autoscaleY"] is False
        assert config_dict["yPSD"]["maximumY"] == 1000
        assert config_dict["waterfall"]["numBins"] == 25
        assert config_dict["waterfall"]["colorMap"] == "viridis"

    def test_fromDict(self):
        config_dict = {"xPSD": {}, "yPSD": {}, "waterfall": {}}
        config_dict["xPSD"]["autoscaleY"] = True
        config_dict["xPSD"]["maximumY"] = 1e6
        config_dict["yPSD"]["autoscaleY"] = True
        config_dict["yPSD"]["maximumY"] = 1e6
        config_dict["waterfall"]["numBins"] = 50
        config_dict["waterfall"]["colorMap"] = "magma"
        self.config.fromDict(config_dict)
        assert self.config.autoscaleX1d is config_dict["xPSD"]["autoscaleY"]
        assert self.config.x1dMaximum == config_dict["xPSD"]["maximumY"]
        assert self.config.autoscaleY1d is config_dict["yPSD"]["autoscaleY"]
        assert self.config.y1dMaximum == config_dict["yPSD"]["maximumY"]
        assert self.config.numWaterfallBins == config_dict["waterfall"]["numBins"]
        assert self.config.waterfallColorMap == config_dict["waterfall"]["colorMap"]
