#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
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
            raise FrameCaptureFailed("Frame capture failed: {}".format(str(err)))

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
        return (self.cameraPtr.OffsetX, self.cameraPtr.OffsetY)

    def getRoiFrame(self):
        """Get the ROI frame from the CCD.

        Returns
        -------
        numpy.array
            The current ROI CCD frame.
        """
        return self.getFullFrame()

    def startup(self):
        """Handle the startup of the camera.
        """
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
        self.cameraPtr.StreamBytesPerSecond = 100000000
        self.height = self.cameraPtr.Height
        self.width = self.cameraPtr.Width
        self.cameraPtr.OffsetX = 0
        self.cameraPtr.OffsetY = 0
        self.cameraPtr.GainAuto = 'Off'
        self.cameraPtr.GainRaw = 0
        self.cameraPtr.ExposureAuto = 'Off'
        self.cameraPtr.AcquisitionMode = 'Continuous'
        self.cameraPtr.TriggerSource = 'Freerun'
        self.cameraPtr.PixelFormat = 'Mono12'
        self.cameraPtr.ExposureTimeAbs = 20000  # microseconds

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
