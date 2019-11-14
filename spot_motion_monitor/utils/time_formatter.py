#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from astropy.time import Time

__all__ = ["TimeFormatter"]

class TimeFormatter():

    def __init__(self):
        self.timezone = "UTC"
        self.standard_format = '%Y%m%d_%H%M%S'

    def getTimeStamp(self):
        now = Time.now()
        return now.strftime(self.standard_format)
