#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from freezegun import freeze_time

from spot_motion_monitor.utils import TimeHandler

class TestTimeHandler():

    def test_parametersAfterConstruction(self):
        th = TimeHandler()
        th.timezone == "UTC"
        assert th.standard_format == "%Y%m%d_%H%M%S"

    @freeze_time("2019-11-26 13:45:23")
    def test_utc_timezone(self):
        th = TimeHandler()
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_134523"

    @freeze_time("2019-11-26 13:45:23")
    def test_tai_timezone(self):
        th = TimeHandler()
        th.timezone = "TAI"
        assert th.getTimeStamp() == 1574775960
        assert th.getFormattedTimeStamp() == "20191126_134600"

    @freeze_time("2019-11-26 13:45:23")
    def test_arizona_timezone(self):
        th = TimeHandler()
        th.timezone = "US/Arizona"
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_064523"

    @freeze_time("2019-11-26 13:45:23")
    def test_chile_timezone(self):
        th = TimeHandler()
        th.timezone = "America/Santiago"
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_104523"
