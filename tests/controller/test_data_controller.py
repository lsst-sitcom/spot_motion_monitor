#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.controller import DataController
from spot_motion_monitor.utils import FrameRejected, GenericFrameInformation, RoiFrameInformation
from spot_motion_monitor.views import CameraDataWidget

class TestDataController():

    def setup_class(cls):
        cls.frame = np.ones((3, 5))

    def test_parametersAfterConstruction(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        assert dc.cameraDataWidget is not None
        assert dc.updateStatusBar is not None
        assert dc.fullFrameModel is not None
        assert dc.roiFrameModel is not None
        assert dc.bufferModel is not None

    def test_updateFullFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(300.3,
                                                                                               400.2,
                                                                                               32042.42,
                                                                                               145.422,
                                                                                               70,
                                                                                               None))
        frame = np.ones((3, 5))
        fps = 24
        dc.passFrame(frame, fps, False)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 1

    def test_failedFrame(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(side_effect=FrameRejected)
        frame = np.ones((3, 5))
        fps = 24
        dc.passFrame(frame, fps, False)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 0

    def test_updateRoiFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateRoiFrameData')
        dc.roiFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(242.3,
                                                                                              286.2,
                                                                                              2519.534,
                                                                                              104.343,
                                                                                              50,
                                                                                              1.532))
        dc.bufferModel.getInformation = mocker.Mock(return_value=RoiFrameInformation(242.5,
                                                                                     286.3,
                                                                                     2501.42,
                                                                                     104.753,
                                                                                     2.5432,
                                                                                     2.2353,
                                                                                     (1000, 25)))
        fps = 40
        dc.passFrame(self.frame, fps, True)
        assert dc.cameraDataWidget.updateRoiFrameData.call_count == 1
