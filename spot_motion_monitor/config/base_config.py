#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
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

    def toYaml(self):
        """Convert the stored configuration to YAML.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError
