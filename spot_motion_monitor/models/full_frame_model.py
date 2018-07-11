#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------

__all__ = ["FullFrameModel"]

class FullFrameModel():

    """This class handles the calculations necessary to fill out a GenericFrameInformation instance.

    Attributes
    ----------
    sigmaScale : float
        Multiplier for the frame standard deviation
    """

    def __init__(self):
        """Initialize the class
        """
        self.sigmaScale = 5.0
