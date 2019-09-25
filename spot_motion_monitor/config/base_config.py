#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['BaseConfig']

class BaseConfig:

    """Base class of the configuration information.
    """

    def __init__(self):
        """Initialize the class.
        """
        pass

    def fromDict(self, config):
        """Convert the stored configuration to a dictionary.

        Parameters
        ----------
        config : dict
            The configuration to translate.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def toDict(self):
        """Convert the stored configuration to a dictionary.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError
