#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from datetime import datetime

import numpy as np
import pandas as pd

from spot_motion_monitor.models import BufferModel, FullFrameModel, RoiFrameModel
from spot_motion_monitor.utils import FrameRejected, FullFrameInformation
from spot_motion_monitor.utils import InformationUpdater, STATUSBAR_FAST_TIMEOUT

__all__ = ["DataController"]

class DataController():

    """This class manages the interactions between the information calculated
       by a particular frame model and the CameraDataWidget.

    Attributes
    ----------
    bufferModel : .BufferModel
        An instance of the buffer model.
    cameraDataWidget : .CameraDataWidget
        An instance of the camera data widget.
    centroidFilename : str
        The current name for the centroid output file.
    filesCreated : bool
        Whether or not the output files have been created.
    fullFrameModel : .FullFrameModel
        An instance of the full frame calculation model.
    psdFilename : str
        The current name for the PSD output file.
    roiFrameModel : .RoiFrameModel
        An instance of the ROI frame calculation model.
    updater : .InformationUpdater
        An instance of the information updater.
    writeData : bool
        Whether or not data writing is available.
    """

    def __init__(self, cdw):
        """Initialize the class.

        Parameters
        ----------
        cdw : .CameraDataWidget
            An instance of the camera data widget.
        """
        self.cameraDataWidget = cdw
        self.fullFrameModel = FullFrameModel()
        self.roiFrameModel = RoiFrameModel()
        self.bufferModel = BufferModel()
        self.updater = InformationUpdater()
        self.roiResetDone = False
        self.writeData = False
        self.filesCreated = False
        self.centroidFilename = None
        self.psdFilename = None

        self.cameraDataWidget.saveDataCheckBox.toggled.connect(self.handleSaveData)

    def getBufferSize(self):
        """Get the buffer size of the buffer data model.

        Returns
        -------
        int
            The buffer size that the buffer model holds.
        """
        return self.bufferModel.bufferSize

    def getCentroidForUpdate(self, frame):
        """Calculate centroid from frame for offset update.

        Parameters
        ----------
        frame : numpy.array
            A frame from a camera CCD.

        Returns
        -------
        GenericInformation
            The instance containing the results of the calculations.
        """
        return self.fullFrameModel.calculateCentroid(frame)

    def getCentroids(self, isRoiMode):
        """Return the current x, y coordinate of the centroid.

        Parameters
        ----------
        isRoiMode : bool
            True is system is in ROI mode, False if in Full Frame mode.

        Returns
        -------
        (float, float)
            The x and y pixel coordinates of the most current centroid.
            Return (None, None) if not in ROI mode.
        """
        if isRoiMode:
            return self.bufferModel.getCentroids()
        else:
            return (None, None)

    def getDataConfiguration(self):
        """Get the current data configuration.

        Returns
        -------
        dict
            The set of current data configuration parameters.
        """
        config = {}
        config['pixelScale'] = self.bufferModel.pixelScale
        return config

    def getPsd(self, isRoiMode, currentFps):
        """Return the power spectrum distribution (PSD).

        Parameters
        ----------
        isRoiMode : bool
            True is system is in ROI mode, False if in Full Frame mode.
        currentFps : float
            The current Frames per Second rate from the camera.

        Returns
        -------
        (numpy.array, numpy.array, numpy.array)
            The PSDX, PSDY and Frequencies from the PSD calculation.
        """
        if isRoiMode:
            psd = self.bufferModel.getPsd(currentFps)
            return psd
        else:
            return (None, None, None)

    def handleSaveData(self, checked):
        self.writeData = checked

    def passFrame(self, frame, currentStatus):
        """Get a frame, do calculations and update information.

        Parameters
        ----------
        frame : numpy.array
            A frame from a camera CCD.
        currentStatus : .CameraStatus
            Instance containing the current camera status.
        """
        if frame is None:
            return
        try:
            if currentStatus.isRoiMode:
                if not self.roiResetDone:
                    self.cameraDataWidget.reset()
                    self.roiResetDone = True
                genericFrameInfo = self.roiFrameModel.calculateCentroid(frame)
                self.bufferModel.updateInformation(genericFrameInfo, currentStatus.frameOffset)
            else:
                if self.roiResetDone:
                    self.cameraDataWidget.reset()
                    self.roiResetDone = False
                genericFrameInfo = self.fullFrameModel.calculateCentroid(frame)
                fullFrameInfo = FullFrameInformation(int(genericFrameInfo.centerX),
                                                     int(genericFrameInfo.centerY),
                                                     genericFrameInfo.flux, genericFrameInfo.maxAdc)
                self.cameraDataWidget.updateFullFrameData(fullFrameInfo)
        except FrameRejected as err:
            self.updater.displayStatus.emit(str(err), STATUSBAR_FAST_TIMEOUT)

    def setBufferSize(self, value):
        """Set the buffer size on the buffer model.

        Parameters
        ----------
        value : int
            The requested buffer size.
        """
        self.bufferModel.bufferSize = value

    def setDataConfiguration(self, config):
        """Set a new configuration for the data controller.

        Parameters
        ----------
        config : dict
            The new configuration parameters.
        """
        self.bufferModel.pixelScale = config['pixelScale']

    def setFrameChecks(self, fullFrameCheck, roiFrameCheck):
        """Set the frame checks to the corresponding models.

        Parameters
        ----------
        fullFrameCheck : func
            The function capturing the full frame check.
        roiFrameCheck : func
            The function capturing the ROI frame check.
        """
        self.fullFrameModel.frameCheck = fullFrameCheck
        self.roiFrameModel.frameCheck = roiFrameCheck

    def showRoiInformation(self, show, currentFps):
        """Display the current ROI information on camera data widget.

        Parameters
        ----------
        show : bool
            Flag that determines if information is shown.
        currentFps : int
            The current camera FPS.
        """
        if show:
            roiFrameInfo = self.bufferModel.getInformation(currentFps)
            self.cameraDataWidget.updateRoiFrameData(roiFrameInfo)

    def writeDataToFile(self, psd):
        """Write centroid and power spectrum distributions to a file.

        Parameters
        ----------
        psd : tuple
            The PSDX. PSDY and Frequency components.
        """
        if not self.writeData:
            return

        if psd[0] is None:
            return

        centroidX = np.array(self.bufferModel.centerX)
        centroidY = np.array(self.bufferModel.centerY)

        if not self.filesCreated:
            dateTag = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.centroidFilename = 'smm_centroid_{}.h5'.format(dateTag)
            self.psdFilename = 'smm_psd_{}.h5'.format(dateTag)
            self.filesCreated = True

        centDf = pd.DataFrame({
                              'X': centroidX,
                              'Y': centroidY
                              })
        psdDf = pd.DataFrame({
                             'Frequencies': psd[2],
                             'X': psd[0],
                             'Y': psd[1]
                             })
        dateKey = 'DT_{}'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))

        centDf.to_hdf(self.centroidFilename, key=dateKey)
        psdDf.to_hdf(self.psdFilename, key=dateKey)
