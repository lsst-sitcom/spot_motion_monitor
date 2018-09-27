#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
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
        self.roiSizeLineEdit.setValidator(QIntValidator(20, 1000))
        self.xAmpLineEdit.setValidator(QIntValidator(1, 20))
        self.xFreqLineEdit.setValidator(QDoubleValidator(0.1, 100.0, 1))
        self.yAmpLineEdit.setValidator(QIntValidator(1, 20))
        self.yFreqLineEdit.setValidator(QDoubleValidator(0.1, 100.0, 1))
        self.deltaTimeLineEdit.setValidator(QIntValidator(10, 1000))
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

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : dict
            The current set of configuration parameters.
        """
        self.roiSizeLineEdit.setText(str(config['roiSize']))
        state = Qt.Checked if config['doSpotOscillation'] else Qt.Unchecked
        self.spotOscillationCheckBox.setCheckState(state)
        self.xAmpLineEdit.setText(str(config['xAmplitude']))
        self.xFreqLineEdit.setText(str(config['xFrequency']))
        self.yAmpLineEdit.setText(str(config['yAmplitude']))
        self.yFreqLineEdit.setText(str(config['yFrequency']))
        self.deltaTimeLineEdit.setText(str(config['deltaTime']))
