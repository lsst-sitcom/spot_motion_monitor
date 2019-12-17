#------------------------------------------------------------------------------
# Copyright LSST Systems Engineering
# See LICENSE for more information.
#------------------------------------------------------------------------------
import os

from PyQt5.QtWidgets import QDialog

from .forms.ui_camera_info_dialog import Ui_CameraInformationDialog

__all__ = ['CameraInformationDialog']

class CameraInformationDialog(QDialog, Ui_CameraInformationDialog):
    """Class that generates the dialog for showing camera information.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        camera : str
            The name of the camera to get the configuration tab for.
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)

    def setCameraInformation(self, cameraInfo):
        """Take the camera information, format and display it.

        Parameters
        ----------
        cameraInfo : OrderedDict
            The set of camera information to display.
        """
        lines = []
        for key, value in cameraInfo.items():
            lines.append(f'<p><b>{key}</b>: {value}</p>')

        self.cameraInfoTextBrowser.setHtml(os.linesep.join(lines))
