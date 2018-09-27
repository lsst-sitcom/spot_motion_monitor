#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QTabWidget

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
        self.name = 'Centroid'
