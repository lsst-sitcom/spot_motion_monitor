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
        tf = TimeFormatter()
        tf.timezone == "UTC"
        assert tf.standard_format == "%Y%m%d_%H%M%S"

    @freeze_time("2019-11-26 13:45:23")
    def test_utc_timezone(self):
        tf = TimeFormatter()
        assert tf.getTimeStamp() == 1574775923
        assert tf.getFormattedTimeStamp() == "20191126_134523"

    @freeze_time("2019-11-26 13:45:23")
    def test_tai_timezone(self):
        tf = TimeFormatter()
        tf.timezone = "TAI"
        assert tf.getTimeStamp() == 1574775960
        assert tf.getFormattedTimeStamp() == "20191126_134600"

    @freeze_time("2019-11-26 13:45:23")
    def test_arizona_timezone(self):
        tf = TimeFormatter()
        tf.timezone = "US/Arizona"
        assert tf.getTimeStamp() == 1574775923
        assert tf.getFormattedTimeStamp() == "20191126_064523"

    @freeze_time("2019-11-26 13:45:23")
    def test_chile_timezone(self):
        tf = TimeFormatter()
        tf.timezone = "America/Santiago"
        assert tf.getTimeStamp() == 1574775923
        assert tf.getFormattedTimeStamp() == "20191126_104523"
