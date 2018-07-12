#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.utils import NO_DATA_VALUE
from spot_motion_monitor.views import CameraDataWidget

class TestCameraDataWidget():

    def test_defaulTextValues(self, qtbot):
        cdw = CameraDataWidget()
        cdw.show()
        qtbot.addWidget(cdw)

        assert cdw.accumPeriodValueLabel.text() == NO_DATA_VALUE
        assert cdw.fpsValueLabel.text() == NO_DATA_VALUE
        assert cdw.numFramesAcqValueLabel.text() == NO_DATA_VALUE
        assert cdw.fluxValueLabel.text() == NO_DATA_VALUE
        assert cdw.maxAdcValueLabel.text() == NO_DATA_VALUE
        assert cdw.centroidXLabel.text() == NO_DATA_VALUE
        assert cdw.centroidYLabel.text() == NO_DATA_VALUE
        assert cdw.rmsXLabel.text() == NO_DATA_VALUE
        assert cdw.rmsYLabel.text() == NO_DATA_VALUE
