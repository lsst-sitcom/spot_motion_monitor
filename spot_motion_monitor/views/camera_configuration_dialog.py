#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QDialog

import spot_motion_monitor.views
from spot_motion_monitor.views.ui_configuration_dialog import Ui_ConfigurationDialog

__all__ = ['CameraConfigurationDialog']

class CameraConfigurationDialog(QDialog, Ui_ConfigurationDialog):
    """Class that generates the dialog for handling camera configuration.

    Attributes
    ----------
    cameraConfigTab : GaussianCameraConfigTab or VimbaCameraConfigTab
        Instance of the appropriate camera configuration tab.
    """

    def __init__(self, camera, parent=None):
        """Summary

        Parameters
        ----------
        camera : str
            The name of the camera to get the configuration tab for.
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.cameraConfigTab = getattr(spot_motion_monitor.views, '{}ConfigTab'.format(camera))()

        self.tabWidget.addTab(self.cameraConfigTab, self.cameraConfigTab.name)
