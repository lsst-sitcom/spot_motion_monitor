#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
__all__ = ['PlotPsdController']

class PlotPsdController:

    """This class handles the interactions between the main program and the
       power spectrum distribution (PSD) waterfall plots.

    Attributes
    ----------
    psdXPlot : FftWaterfallPlotWidget
        The instance of the waterfall plot for the PSD x coordinates.
    psdYPlot : FftWaterfallPlotWidget
        The instance of the waterfall plot for the PSD y coordinates.
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
        self.psdXPlot = fftx
        self.psdYPlot = ffty

    def setup(self, arraySize):
        """Setup the controller's internal information.

        Parameters
        ----------
        arraySize : int
            The vertical dimension of the PSD waterfall plot data.
        """
        self.psdXPlot.setup(arraySize)
        self.psdYPlot.setup(arraySize)

    def update(self, psdDataX, psdDataY, frequencies):
        """Update the controller's plot widgets with the data provided.

        NOTE: If NoneType data is provided, the updatePlot methods are not called.

        Parameters
        ----------
        psdDataX : numpy.array
            The array of the PSD x coordinate data.
        psdDataY : numpy.array
            The array of the PSD y coordinate data.
        frequencies : numpy.array
            The frequency array associated with the PSD data.
        """
        if psdDataX is None or psdDataY is None or frequencies is None:
            return

        self.psdXPlot.updatePlot(psdDataX, frequencies)
        self.psdYPlot.updatePlot(psdDataY, frequencies)
