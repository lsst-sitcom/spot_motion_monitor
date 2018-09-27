#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtGui import QIntValidator
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
        self.roiSizeLineEdit.setValidator(QIntValidator(20, 1000))
        self.roiFluxMinLineEdit.setValidator(QIntValidator(100, 10000))
        self.roiExposureTimeLineEdit.setValidator(QIntValidator(500, 50000))
        self.name = 'Vimba'

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : dict
            The current set of configuration parameters.
        """
        self.roiSizeLineEdit.setText(str(config['roiSize']))
        self.roiFluxMinLineEdit.setText(str(config['roiFluxMinimum']))
        self.roiExposureTimeLineEdit.setText(str(config['roiExposureTime']))
