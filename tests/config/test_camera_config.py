#------------------------------------------------------------------------------
# See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import CameraConfig

class TestCameraConfig:

    def setup_class(cls):
        cls.config = CameraConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.roiSize == 50
        assert self.config.fpsRoiFrame == 40
        assert self.config.fpsFullFrame == 24
        assert self.config.modelName is None

    def test_toDict(self):
        config_dict = self.config.toDict()

        assert config_dict["roi"]["size"] == 50
        assert config_dict["roi"]["fps"] == 40
        assert config_dict["full"]["fps"] == 24
        assert "modelName" not in config_dict

        config_dict = self.config.toDict(True)

        assert config_dict["modelName"] is None

    def test_fromDict(self):
        config_dict = {"roi": {}, "full": {}}
        config_dict["roi"]["size"] = 100
        config_dict["roi"]["fps"] = 120
        config_dict["full"]["fps"] = 30
        config_dict["modelName"] = "Test"

        self.config.fromDict(config_dict)

        assert self.config.roiSize == config_dict["roi"]["size"]
        assert self.config.fpsRoiFrame == config_dict["roi"]["fps"]
        assert self.config.fpsFullFrame == config_dict["full"]["fps"]
        assert self.config.modelName == config_dict["modelName"]
