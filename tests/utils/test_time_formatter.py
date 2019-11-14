#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from freezegun import freeze_time

from spot_motion_monitor.utils import TimeFormatter

class TestTimeFormatter():

    def setup_class(cls):
        cls.tf = TimeFormatter()

    def test_parametersAfterConstruction(self):
        assert self.tf.timezone == "UTC"
        assert self.tf.standard_format == "%Y%m%d_%H%M%S"

    @freeze_time("2019-11-26 13:45:23")
    def test_timeFormatting(self):
        assert self.tf.getTimeStamp() == "20191126_134523"
