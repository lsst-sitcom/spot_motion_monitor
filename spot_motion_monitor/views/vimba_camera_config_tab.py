#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QTabWidget

from spot_motion_monitor.views.ui_vimba_camera_config import Ui_VimbaCameraConfigForm

__all__ = ['VimbaCameraConfigTab']

class VimbaCameraConfigTab(QTabWidget, Ui_VimbaCameraConfigForm):
    """Class that handles the Vimba camera configuration tab.

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
        self.name = 'Vimba'
