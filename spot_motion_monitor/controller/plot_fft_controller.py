#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['PlotFftController']

class PlotFftController:

    """Summary

    Attributes
    ----------
    fftXPlot : FftWaterfallPlotWidget
        The instance of the waterfall plot for the FFT x coordinates.
    fftYPlot : FftWaterfallPlotWidget
        The instance of the waterfall plot for the FFT y coordinates.
    """

    def __init__(self, fftx, ffty):
        """Initialize the class.

        Parameters
        ----------
        fftx : FftWaterfallPlotWidget
            The instance of the waterfall plot for the FFT x coordinates.
        ffty : FftWaterfallPlotWidget
            The instance of the waterfall plot for the FFT y coordinates.
        """
        self.fftXPlot = fftx
        self.fftYPlot = ffty

    def setup(self, arraySize):
        """Setup the controller's internal information.

        Parameters
        ----------
        arraySize : int
            The vertical dimension of the FFT waterfall plot data.
        """
        self.fftXPlot.setup(arraySize)
        self.fftYPlot.setup(arraySize)

    def update(self, fftDataX, fftDataY, frequencies):
        """Update the controller's plot widgets with the data provided.

        NOTE: If NoneType data is provided, the updatePlot methods are not called.

        Parameters
        ----------
        fftDataX : numpy.array
            The array of the FFT x coordinate data.
        fftDataY : numpy.array
            The array of the FFT y coordinate data.
        frequencies : numpy.array
            The frequency array associated with the FFT data.
        """
        if fftDataX is None or fftDataY is None or frequencies is None:
            return

        self.fftXPlot.updatePlot(fftDataX, frequencies)
        self.fftYPlot.updatePlot(fftDataY, frequencies)
