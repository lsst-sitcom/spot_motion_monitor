#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
from pyqtgraph import GraphicsLayoutWidget, ImageItem

class FftWaterfallPlotWidget(GraphicsLayoutWidget):

    """This class manages and displays the FFT data in a wterfall plot.

    Attributes
    ----------
    arraySize : int
        The size of the data array to display.
    data : numpy.ndarray
        The 2D array for the FFT data.
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
        p1.setAspectLocked(True)
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

    def updatePlot(self, fft, freqs):
        """Update the current plot with the given data.

        Parameters
        ----------
        fft : numpy.array
            The FFT data of a given centroid coordinate.
        freqs : numpy.array
            The frequency array associated with the FFT data.
        """
        if self.data is None:
            self.data = np.zeros((self.arraySize, fft.size))
            self.data[0, ...] = fft
        else:
            self.data[1:, ...] = self.data[:-1, ...]
            self.data[0, ...] = fft

        self.image.setImage(self.data)
