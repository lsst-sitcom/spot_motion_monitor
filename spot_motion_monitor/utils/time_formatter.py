#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from astropy.time import Time
import pytz

__all__ = ["TimeFormatter"]

class TimeFormatter():

    def __init__(self):
        self.timezone = "UTC"
        self.standard_format = '%Y%m%d_%H%M%S'

    def _getTime(self):
        now = Time.now()
        if self.timezone != "UTC":
            if self.timezone == "TAI":
                return now.tai.datetime.replace(tzinfo=pytz.utc)
            else:
                tz = pytz.timezone(self.timezone)
                return now.datetime.replace(tzinfo=pytz.utc).astimezone(tz)
        else:
            return now.datetime.replace(tzinfo=pytz.utc)

    def getFormattedTimeStamp(self):
        return self._getTime().strftime(self.standard_format)

    def getTimeStamp(self):
        return self._getTime().timestamp()
