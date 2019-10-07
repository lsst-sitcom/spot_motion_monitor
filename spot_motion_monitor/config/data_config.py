#------------------------------------------------------------------------------
# See LICENSE for more information.
#------------------------------------------------------------------------------
from .base_config import BaseConfig
from .buffer_model_config import BufferModelConfig
from .full_frame_model_config import FullFrameModelConfig
from .roi_frame_model_config import RoiFrameModelConfig

__all__ = ["DataConfig"]

class DataConfig(BaseConfig):

    """Class that handles the configuration of data configuration.

    Attributes
    ----------
    buffer : `config.BufferModelConfig`
        Instance containing the buffer model configuration.
    fullFrame : `config.FullFrameModelConfig`
        Instance containing the full frame model configuration.
    roiFrame : `config.RoiFrameModelConfig`
        Instance containing the ROI frame model configuration.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.buffer = BufferModelConfig()
        self.fullFrame = FullFrameModelConfig()
        self.roiFrame = RoiFrameModelConfig()

    def __eq__(self, other):
        """Check equality.

        Parameters
        ----------
        other : `config.DataConfig`
            Other instance to check.

        Returns
        -------
        bool
            True is objects are equal, False if not
        """
        if type(other) is type(self):
            return other.buffer == self.buffer and \
                other.fullFrame == self.fullFrame and \
                other.roiFrame == self.roiFrame
        return False

    def __str__(self):
        """Print the object contents.

        Returns
        -------
        str
            The object string representation.
        """
        odict = {"buffer": str(self.buffer), "fullFrame": str(self.fullFrame),
                 "roiFrame": str(self.roiFrame)}
        return str(odict)

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.buffer.fromDict(config)
        self.fullFrame.fromDict(config)
        self.roiFrame.fromDict(config)

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        bufferDict = self.buffer.toDict()
        fullFrameDict = self.fullFrame.toDict()
        roiFrameDict = self.roiFrame.toDict()
        config = {**bufferDict, **fullFrameDict, **roiFrameDict}
        return config
