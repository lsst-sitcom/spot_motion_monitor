#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from datetime import datetime
import time

import numpy as np
import pymba as pv

from spot_motion_monitor.camera import BaseCamera
from spot_motion_monitor.utils import CameraNotFound, FrameCaptureFailed

__all__ = ['VimbaCamera']

class VimbaCamera(BaseCamera):

    def __init__(self):
        """Initalize the class.
        """
        super().__init__()
        self.vimba = None
        self.cameraPtr = None
        self.frame = None
        self.fpsFullFrame = 24
        self.fpsRoiFrame = 40
        self.roiSize = 50
        self.fluxMinRoi = 5000
        self.offsetUpdateTimeout = 30
        self.offsetX = 0
        self.offsetY = 0

    def checkFullFrame(self, flux, maxAdc, comX, comY):
        """Use the provided quantities to check frame validity.

        Parameters
        ----------
        flux : float
            The flux of the frame.
        maxAdc : float
            The maximum ADC of the frame.
        comX : float
            The x component of the center-of-mass.
        comY : float
            The y component of the center-of-mass.

        Returns
        -------
        bool
            True if frame is valid, False if not.
        """
        return flux > 100 and maxAdc > 0 and comX > 0 and comY > 0

    def checkRoiFrame(self, flux):
        """Use the provided quantities to check frame validity

        Parameters
        ----------
        flux : float
            The flux of the frame.

        Returns
        -------
        bool
            True if frame is valid, False if not.
        """
        return flux > self.fluxMinRoi

    def getFullFrame(self):
        """Get the full frame from the CCD.

        Returns
        -------
        numpy.array
            The current full CCD frame.
        """
        try:
            self.frame.queueFrameCapture()
        except pv.VimbaException as err:
            raise FrameCaptureFailed("{} Full frame capture failed: {}".format(datetime.now(), str(err)))

        self.cameraPtr.runFeatureCommand('AcquisitionStart')
        #self.cameraPtr.runFeatureCommand('AcquisitionStop')
        self.frame.waitFrameCapture(1000)
        frameData = self.frame.getBufferByteData()

        img = np.ndarray(buffer=frameData, dtype=np.uint16, shape=(self.height, self.width))
        return img

    def getOffset(self):
        """Get the offset for the CCD frame.

        Returns
        -------
        (int, int)
            The current offset of the CCD frame.
        """
        return (self.offsetX, self.offsetY)

    def getRoiFrame(self):
        """Get the ROI frame from the CCD.

        Returns
        -------
        numpy.array
            The current ROI CCD frame.
        """
        self.totalFrames += 1
        try:
            self.frame.queueFrameCapture()
        except pv.VimbaException as err:
            self.badFrames += 1
            raise FrameCaptureFailed("{} ROI frame capture failed: {}".format(datetime.now(), str(err)))
        self.goodFrames += 1
        self.cameraPtr.runFeatureCommand('AcquisitionStart')
        self.cameraPtr.runFeatureCommand('AcquisitionStop')
        self.frame.waitFrameCapture(1)
        frameData = self.frame.getBufferByteData()

        img = np.ndarray(buffer=frameData, dtype=np.uint16, shape=(self.roiSize, self.roiSize))
        return img

    def resetOffset(self):
        """Reset the camera offsets back to zero.
        """
        self.cameraPtr.OffsetX = 0
        self.cameraPtr.OffsetY = 0
        self.offsetX = 0
        self.offsetY = 0
        self.cameraPtr.Height = self.height
        self.cameraPtr.Width = self.width

    def showFrameStatus(self):
        print("{} {}, {}, {}".format(datetime.now(), self.goodFrames, self.badFrames, self.totalFrames))

    def startup(self):
        """Handle the startup of the camera.
        """
        self.goodFrames = 0
        self.badFrames = 0
        self.totalFrames = 0
        self.vimba = pv.Vimba()
        self.vimba.startup()
        system = self.vimba.getSystem()
        system.runFeatureCommand('GeVDiscoveryAllOnce')
        time.sleep(0.2)
        cameraIds = self.vimba.getCameraIds()
        try:
            self.cameraPtr = self.vimba.getCamera(cameraIds[0])
        except IndexError:
            raise CameraNotFound('Camera not found ... check power or connection!')

        self.cameraPtr.openCamera()
        self.cameraPtr.GevSCPSPacketSize = 1500
        self.cameraPtr.StreamBytesPerSecond = 124000000
        self.height = self.cameraPtr.HeightMax
        self.width = self.cameraPtr.WidthMax
        self.cameraPtr.Height = self.height
        self.cameraPtr.Width = self.width
        self.cameraPtr.OffsetX = 0
        self.cameraPtr.OffsetY = 0
        self.cameraPtr.GainAuto = 'Off'
        self.cameraPtr.GainRaw = 0
        self.cameraPtr.ExposureAuto = 'Off'
        self.cameraPtr.AcquisitionMode = 'Continuous'
        self.cameraPtr.TriggerSource = 'Freerun'
        self.cameraPtr.PixelFormat = 'Mono12'
        self.cameraPtr.ExposureTimeAbs = 8000  # microseconds

        self.frame = self.cameraPtr.getFrame()
        self.frame.announceFrame()
        self.cameraPtr.startCapture()

    def shutdown(self):
        """Handle the shutdown of the camera.
        """
        try:
            self.cameraPtr.endCapture()
            self.cameraPtr.revokeAllFrames()
            self.cameraPtr.closeCamera()
        except pv.VimbaException:
            pass
        self.vimba.shutdown()

    def updateOffset(self, centroidX, centroidY):
        """Update the camera's internal offset values from the provided centroid.

        For the Gaussian camera, this is a no-op, but helps test the mechanism.

        Parameters
        ----------
        centroidX : float
            The x component of the centroid for offset update.
        centroidY : float
            The y component of the centroid for offset update.
        """
        self.offsetX = int(centroidX - self.roiSize / 2)
        self.offsetY = int(centroidY - self.roiSize / 2)
        self.cameraPtr.OffsetX = self.offsetX
        self.cameraPtr.OffsetY = self.offsetY
        self.cameraPtr.Height = self.roiSize
        self.cameraPtr.Width = self.roiSize

    def waitOnRoi(self):
        while True:
            if self.cameraPtr.Height == self.roiSize and self.cameraPtr.Width == self.roiSize:
                break
