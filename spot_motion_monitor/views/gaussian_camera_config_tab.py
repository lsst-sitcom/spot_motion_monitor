#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QTabWidget

from spot_motion_monitor.views.ui_gaussian_camera_config import Ui_GaussianCameraConfigForm

__all__ = ['GaussianCameraConfigTab']

class GaussianCameraConfigTab(QTabWidget, Ui_GaussianCameraConfigForm):
    """Class that handles the Gaussian camera configuration tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.name = 'Gaussian'
        self.spotOscillationCheckBox.toggled.connect(self.changeGroupBoxState)

    def changeGroupBoxState(self, checked):
        """Adjust the oscillation parameters group box based on check box
           state.

        Parameters
        ----------
        checked : bool
            The current state of the check box.
        """
        self.spotOscillationGroupBox.setEnabled(checked)
