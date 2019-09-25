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
