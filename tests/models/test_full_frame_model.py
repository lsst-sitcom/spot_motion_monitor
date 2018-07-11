#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.models import FullFrameModel

class TestFullFrameModel():

    def setup_class(cls):
        cls.model = FullFrameModel()

    def test_parametersAfterConstruction(self):
        assert self.model.sigmaScale == 5.0
