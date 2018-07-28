#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
from pyqtgraph import GraphicsLayoutWidget, ImageItem

__all__ = ['PsdWaterfallPlotWidget']

class PsdWaterfallPlotWidget(GraphicsLayoutWidget):

    """This class manages and displays the power spectrum distribution (PSD)
       data in a waterfall plot.

    Attributes
    ----------
    arraySize : int
        The size of the data array to display.
    data : numpy.ndarray
        The 2D array for the PSD data.
    image : pyqtgraph.ImageItem
        The instance of the image item for display.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        p1 = self.addPlot()
        p1.invertY()
        self.image = ImageItem()
        self.image.setOpts(axisOrder='row-major')
        p1.addItem(self.image)

        self.data = None
        self.arraySize = None

    def setup(self, arraySize):
        """Setup the widget with the array size.

        Parameters
        ----------
        arraySize : int
            The size fo the data array to display in terms of history.
        """
        self.arraySize = arraySize

    def updatePlot(self, psd, freqs):
        """Update the current plot with the given data.

        Parameters
        ----------
        psd : numpy.array
            The PSD data of a given centroid coordinate.
        freqs : numpy.array
            The frequency array associated with the PSD data.
        """
        if self.data is None:
            self.data = np.zeros((self.arraySize, psd.size))
            self.data[0, ...] = psd
        else:
            self.data[1:, ...] = self.data[:-1, ...]
            self.data[0, ...] = psd

        self.image.setImage(self.data)
