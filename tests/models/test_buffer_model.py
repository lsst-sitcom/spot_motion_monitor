#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.models.buffer_model import BufferModel
from spot_motion_monitor.utils.frame_information import GenericFrameInformation

class TestBufferModel():

    def setup_class(cls):
        cls.model = BufferModel()
        cls.offset = (264, 200)

    def test_parametersAfterConstruction(self):
        assert self.model.bufferSize == 1000
        assert self.model.pixelScale == 1.0
        assert self.model.rollBuffer is False
        assert self.model.maxAdc is not None
        assert self.model.flux is not None
        assert self.model.centerX is not None
        assert self.model.centerY is not None
        assert self.model.objectSize is not None
        assert self.model.stdMax is not None

    def test_listsAfterPassingGenericFrameInfo(self):
        info = GenericFrameInformation(20.42, 30.42, 3245.32543, 119.24245, 60, 1.432435)
        self.model.updateInformation(info, self.offset)
        assert self.model.maxAdc == [info.maxAdc]
        assert self.model.flux == [info.flux]
        assert self.model.centerX == [info.centerX + self.offset[0]]
        assert self.model.centerY == [info.centerY + self.offset[1]]
        assert self.model.objectSize == [info.objectSize]
        assert self.model.stdMax == [info.stdNoObjects]
        assert self.model.rollBuffer is False

    def test_listSizesAfterBufferSizeReached(self):
        bufferSize = 3
        self.model.bufferSize = bufferSize
        info = GenericFrameInformation(20.42, 30.42, 3245.32543, 119.24245, 60, 1.432435)
        for i in range(bufferSize):
            self.model.updateInformation(info, self.offset)
        assert self.model.rollBuffer is True
        assert len(self.model.flux) == bufferSize
        # Update one more time, buffer size should be fixed
        self.model.updateInformation(info, self.offset)
        assert self.model.rollBuffer is True
        assert len(self.model.flux) == bufferSize

    def test_reset(self):
        bufferSize = 3
        self.model.bufferSize = bufferSize
        info = GenericFrameInformation(20.42, 30.42, 3245.32543, 119.24245, 60, 1.432435)
        for i in range(bufferSize):
            self.model.updateInformation(info, self.offset)
        self.model.reset()
        assert len(self.model.maxAdc) == 0
        assert len(self.model.flux) == 0
        assert len(self.model.centerX) == 0
        assert len(self.model.centerY) == 0
        assert len(self.model.objectSize) == 0
        assert len(self.model.stdMax) == 0
        assert self.model.rollBuffer is False

    def test_getRoiFrameInformation(self):
        bufferSize = 3
        currentFps = 40
        duration = bufferSize / currentFps
        self.model.bufferSize = bufferSize
        self.model.pixelScale = 0.35

        info = self.model.getInformation(currentFps)
        assert info is None

        np.random.seed(2000)
        x = np.random.random(3)
        self.model.rollBuffer = True
        self.model.maxAdc = 119.53 + x
        self.model.flux = 2434.35 + x
        self.model.centerX = 200 + x
        self.model.centerY = 321.3 + x
        self.model.objectSize = np.random.randint(60, 65)
        self.model.stdMax = 1.42 + x

        info = self.model.getInformation(currentFps)
        assert info.flux == 2434.8911626243757
        assert info.maxAdc == 120.07116262437593
        assert info.centerX == 200.54116262437594
        assert info.centerY == 321.84116262437595
        assert info.rmsX == 0.013075758426286251
        assert info.rmsY == 0.013075758426290931
        # assert info.objectSize == 64.0
        # assert info.stdNoObjects == 1.9611626243759368
        assert info.validFrames == (bufferSize, duration)

        # self.model.stdMax[1] = np.nan
        # info = self.model.getInformation(duration)
        # assert info.stdNoObjects == 1.9494795589614855

    def test_getCentroids(self):
        self.model.reset()
        bufferSize = 3
        self.model.bufferSize = bufferSize
        centroids = self.model.getCentroids()
        assert centroids == (None, None)
        info = GenericFrameInformation(20.42, 30.42, 3245.32543, 119.24245, 60, 1.432435)
        self.model.updateInformation(info, self.offset)
        centroidX = info.centerX + self.offset[0]
        centroidY = info.centerY + self.offset[1]
        centroids = self.model.getCentroids()
        assert centroids == (centroidX, centroidY)

    def test_getFft(self):
        self.model.reset()
        bufferSize = 3
        currentFps = 40
        self.model.bufferSize = bufferSize
        self.model.pixelScale = 0.35

        fft = self.model.getFft(currentFps)
        assert fft == (None, None, None)

        np.random.seed(2000)
        x = np.random.random(3)
        self.model.rollBuffer = True
        self.model.maxAdc = 119.53 + x
        self.model.flux = 2434.35 + x
        self.model.centerX = 200 + x
        self.model.centerY = 321.3 + x
        self.model.objectSize = np.random.randint(60, 65)
        self.model.stdMax = 1.42 + x

        fft = self.model.getFft(currentFps)
        assert fft[0] is not None
        assert fft[1] is not None
        assert fft[2] is not None
