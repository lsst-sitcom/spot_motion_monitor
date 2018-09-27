#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QTabWidget

from spot_motion_monitor.views.ui_psd_plots_config import Ui_PsdPlotConfigForm

__all__ = ['PsdPlotConfigTab']

class PsdPlotConfigTab(QTabWidget, Ui_PsdPlotConfigForm):
    """Class that handles the Power Spectrum Distribution plot configuration
       tab.

    Attributes
    ----------
    name : str
        The name for the tab widget.
    """

    def __init__(self, parent=None):
        """Summary

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.name = 'PSD'