#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTabWidget

from spot_motion_monitor.utils import boolToCheckState, noneToDefaultOrValue
from spot_motion_monitor.views.ui_centroid_plots_config import Ui_CentroidPlotsConfigForm

__all__ = ['CentroidPlotConfigTab']

class CentroidPlotConfigTab(QTabWidget, Ui_CentroidPlotsConfigForm):
    """Class that handles the centroid plot configuration tab.

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
        self.minXLimitLineEdit.setValidator(QIntValidator(0, 10e10))
        self.maxXLimitLineEdit.setValidator(QIntValidator(0, sys.maxsize))
        self.minYLimitLineEdit.setValidator(QIntValidator(0, 10e10))
        self.maxYLimitLineEdit.setValidator(QIntValidator(0, sys.maxsize))
        self.name = 'Centroid'

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : dict
            The current set of configuration parameters.
        """
        self.useAutoScaleXCheckBox.setChecked(boolToCheckState(config['xCentroid']['autoscale']))
        self.minXLimitLineEdit.setText(str(noneToDefaultOrValue(config['xCentroid']['minimum'])))
        self.maxXLimitLineEdit.setText(str(noneToDefaultOrValue(config['xCentroid']['maximum'])))
        self.useAutoScaleYCheckBox.setChecked(boolToCheckState(config['yCentroid']['autoscale']))
        self.minYLimitLineEdit.setText(str(noneToDefaultOrValue(config['yCentroid']['minimum'])))
        self.maxYLimitLineEdit.setText(str(noneToDefaultOrValue(config['yCentroid']['maximum'])))
        value = noneToDefaultOrValue(config['scatterPlot']['numHistogramBins'])
        self.numHistoBinsLineEdit.setText(str(value))
