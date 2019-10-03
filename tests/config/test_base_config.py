#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import pytest

from spot_motion_monitor.config import BaseConfig

class TestBaseConfig:

    def setup_class(cls):
        cls.baseConfig = BaseConfig()

    def test_noApiAfterConstruction(self):

        with pytest.raises(NotImplementedError):
            self.baseConfig.toDict()

        with pytest.raises(NotImplementedError):
            self.baseConfig.fromDict({})

    def test_equality(self):
        config1 = BaseConfig()
        config1.x = 10
        config2 = BaseConfig()
        config2.x = 4
        config3 = BaseConfig()
        config3.x = 10
        config4 = BaseConfig()
        config4.x = None
        config5 = BaseConfig()
        config5.x = None

        assert config1 != config2
        assert config1 == config3
        assert config1 != config4
        assert config4 == config5
