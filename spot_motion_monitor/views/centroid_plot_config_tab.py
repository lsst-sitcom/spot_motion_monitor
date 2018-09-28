#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTabWidget

import spot_motion_monitor.utils as utils
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

    def getConfiguration(self):
        """Get the current configuration parameters from the tab's widgets.

        Returns
        -------
        dict
            The current set of configuration parameters.
        """
        config = {}
        config['xCentroid'] = {}
        xAutoscale = utils.checkStateToBool(self.useAutoScaleXCheckBox.checkState())
        config['xCentroid']['autoscale'] = xAutoscale
        if not xAutoscale:
            xMin = utils.defaultToNoneOrValue(self.minXLimitLineEdit.text())
            config['xCentroid']['minimum'] = xMin if xMin is None else int(xMin)
            xMax = utils.defaultToNoneOrValue(self.maxXLimitLineEdit.text())
            config['xCentroid']['maximum'] = xMax if xMax is None else int(xMax)
        config['yCentroid'] = {}
        yAutoscale = utils.checkStateToBool(self.useAutoScaleYCheckBox.checkState())
        config['yCentroid']['autoscale'] = yAutoscale
        if not yAutoscale:
            yMin = utils.defaultToNoneOrValue(self.minYLimitLineEdit.text())
            config['yCentroid']['minimum'] = yMin if yMin is None else int(yMin)
            yMax = utils.defaultToNoneOrValue(self.maxYLimitLineEdit.text())
            config['yCentroid']['maximum'] = yMax if yMax is None else int(yMax)
        config['scatterPlot'] = {}
        config['scatterPlot']['numHistogramBins'] = int(self.numHistoBinsLineEdit.text())
        return config

    def setConfiguration(self, config):
        """Set the configuration parameters into the tab's widgets.

        Parameters
        ----------
        config : dict
            The current set of configuration parameters.
        """
        self.useAutoScaleXCheckBox.setChecked(utils.boolToCheckState(config['xCentroid']['autoscale']))
        self.minXLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config['xCentroid']['minimum'])))
        self.maxXLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config['xCentroid']['maximum'])))
        self.useAutoScaleYCheckBox.setChecked(utils.boolToCheckState(config['yCentroid']['autoscale']))
        self.minYLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config['yCentroid']['minimum'])))
        self.maxYLimitLineEdit.setText(str(utils.noneToDefaultOrValue(config['yCentroid']['maximum'])))
        value = utils.noneToDefaultOrValue(config['scatterPlot']['numHistogramBins'])
        self.numHistoBinsLineEdit.setText(str(value))
