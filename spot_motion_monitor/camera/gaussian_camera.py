#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.camera import BaseCamera

__all__ = ['GaussianCamera']

class GaussianCamera(BaseCamera):

    """This class creates a camera that produces a frame with random Poisson
       noise and a Gaussian spot placed at random within the frame.

    Attributes
    ----------
    fpsFullFrame : int
        The Frames per Second rate in full frame mode.
    fpsRoiFrame : int
        The Frames per Second rate in ROI frame mode.
    height : int
        The pixel height of the CCD.
    postageStamp : numpy.array
        The array containing the Gaussian postage stamp.
    roiSize : int
        The size of a (square) ROI region in pixels.
    seed : int
        The seed for the random number generator.
    spotSize : int
        The box size in pixels for the Gaussian spot.
    width : int
        The pixel width of the CCD.
    xPoint : int
        The x-coordinate of the Gaussian postage stamp insertion point.
    yPoint : int
        The y-coordinate of the Gaussian postage stamp insertion point.
    """

    seed = None
    spotSize = None

    def __init__(self):
        """Initalize the class.
        """
        super().__init__()

    def findInsertionPoint(self):
        """Determine the Gaussian spot insertion point.
        """
        percentage = 0.2
        xRange = percentage * self.width
        yRange = percentage * self.height
        # Pick lower left corner for insertion
        xHalfwidth = self.width / 2
        yHalfwidth = self.height / 2
        self.xPoint = np.random.randint(xHalfwidth - xRange, xHalfwidth + xRange + 1)
        self.yPoint = np.random.randint(yHalfwidth - yRange, yHalfwidth + yRange + 1)

    def getFrame(self):
        """Get the frame from the CCD.

        Returns
        -------
        numpy.array
            The current CCD frame.
        """
        # Create base CCD frame
        ccd = np.random.poisson(20.0, (self.height, self.width))

        # Merge CCD frame and postage stamp
        ccd[self.yPoint:self.yPoint + self.postageStamp.shape[0],
            self.xPoint:self.xPoint + self.postageStamp.shape[1]] += self.postageStamp

        return ccd

    def getFullFrame(self):
        """Get the full frame from the CCD.

        Returns
        -------
        numpy.array
            The current full CCD frame.
        """
        return self.getFrame()

    def getRoiFrame(self):
        """Get the ROI frame from the CCD.

        Returns
        -------
        numpy.array
            The current ROI CCD frame.
        """
        ccd = self.getFullFrame()
        # Offset is same for both axes since spot and ROI are square.
        offset = (self.roiSize - self.spotSize) // 2
        xStart = self.xPoint - offset
        yStart = self.yPoint - offset
        print(self.xPoint, self.yPoint)
        print(xStart, yStart)
        roi = ccd[yStart:yStart + self.roiSize, xStart:xStart + self.roiSize]
        return roi

    def makePostageStamp(self):
        """Create the Gaussian spot.
        """
        linear_space = np.linspace(-2, 2, self.spotSize)
        x, y = np.meshgrid(linear_space, linear_space)
        d = np.sqrt(x * x + y * y)
        sigma, mu = 0.5, 0.0
        a = 200.0 / (sigma * np.sqrt(2.0 * np.pi))
        self.postageStamp = a * np.exp(-((d - mu)**2 / (2.0 * sigma**2)))
        self.postageStamp = self.postageStamp.astype(np.int64)

    def startup(self):
        """Handle the startup of the camera.
        """
        self.spotSize = 20
        self.height = 480
        self.width = 640
        self.fpsFullFrame = 24
        self.fpsRoiFrame = 40
        self.roiSize = 50
        np.random.seed(self.seed)
        self.makePostageStamp()
        self.findInsertionPoint()

    def shutdown(self):
        """Handle the shutdown of the camera.
        """
        pass
