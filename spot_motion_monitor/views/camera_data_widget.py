#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QWidget

from spot_motion_monitor.views.ui_camera_data import Ui_CameraData

__all__ = ["CameraDataWidget"]

class CameraDataWidget(QWidget, Ui_CameraData):

    """This class handles the interactions from the Camera Data Widget on
       the MainWindow.
    """

    def __init__(self, parent=None):
        """Initalize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
