#------------------------------------------------------------------------------
# See LICENSE for more information.
#------------------------------------------------------------------------------
from . import BaseConfig

__all__ = ("CameraConfig")

class CameraConfig(BaseConfig):
    """Class that handles the general configuration of cameras.

    Attributes
    ----------
    fpsFullFrame : int
        The acquisition frame rate for full frames.
    fpsRoiFrame : int
        The acquisition frame rate for ROI frames.
    modelName : str or None
        The model name of the camera.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.roiSize = 50
        self.fpsFullFrame = 24
        self.fpsRoiFrame = 40
        self.modelName = None

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.check("roiSize", config["roi"], "size")
        self.check("fpsRoiFrame", config["roi"], "fps")
        try:
            self.check("fpsFullFrame", config["full"], "fps")
        except KeyError:
            pass
        self.check("modelName", config, "modelName")

    def toDict(self, writeEmpty=False):
        """Translate class attributes to configuration dict.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roi": {}, "full": {}}
        config["roi"]["size"] = self.roiSize
        config["roi"]["fps"] = self.fpsRoiFrame
        config["full"]["fps"] = self.fpsFullFrame
        if writeEmpty or self.modelName is not None:
            config["modelName"] = self.modelName
        return config
