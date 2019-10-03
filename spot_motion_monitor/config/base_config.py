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

    def __eq__(self, other):
        """Check equality.

        Parameters
        ----------
        other : Any derived `BaseConfig`
            Other instance to check.

        Returns
        -------
        bool
            True is objects are equal, False if not
        """
        print("Other: ", other.__dict__)
        print("Self : ", self.__dict__)
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

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
