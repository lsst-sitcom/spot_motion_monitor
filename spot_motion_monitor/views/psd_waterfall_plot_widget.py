#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
from PyQt5 import QtCore
from pyqtgraph import GraphicsLayoutWidget, ImageItem

__all__ = ['PsdWaterfallPlotWidget']

class PsdWaterfallPlotWidget(GraphicsLayoutWidget):

    """This class manages and displays the power spectrum distribution (PSD)
       data in a waterfall plot.

    Attributes
    ----------
    arraySize : int
        The size of the data array to display.
    boundingRect : QtCore.QRectF
        The actual coordinate space base on frequency and time of acquisition.
    data : numpy.ndarray
        The 2D array for the PSD data.
    image : pyqtgraph.ImageItem
        The instance of the image item for display.
    timeScale : float
        The total time for the buffer to accumulate at the ROI FPS.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.plot = self.addPlot()
        self.plot.invertY()
        self.plot.setLabel('bottom', '&#969;', units='Hz')
        self.plot.setLabel('left', 'Time', units='s')

        self.image = ImageItem()
        self.image.setOpts(axisOrder='row-major')
        self.plot.addItem(self.image)

        self.data = None
        self.arraySize = None
        self.boundingRect = None
        self.timeScale = None

    def setup(self, arraySize, timeScale):
        """Setup the widget with the array size.

        Parameters
        ----------
        arraySize : int
            The size fo the data array to display in terms of history.
        timeScale : float
            The total time for the buffer to accumulate at the ROI FPS.
        """
        self.arraySize = arraySize
        self.timeScale = timeScale

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
        if self.boundingRect is None:
            self.boundingRect = QtCore.QRectF(0, 0, freqs[-1], self.arraySize * self.timeScale)
            self.image.setRect(self.boundingRect)