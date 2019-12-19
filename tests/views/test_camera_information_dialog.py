#------------------------------------------------------------------------------
# Copyright LSST Systems Engineering
# See LICENSE for more information.
#------------------------------------------------------------------------------
from collections import OrderedDict
import os

from spot_motion_monitor.views import CameraInformationDialog

class TestCameraInformationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        dialog = CameraInformationDialog()
        qtbot.addWidget(dialog)
        dialog.show()

        assert dialog.cameraInfoTextBrowser.toPlainText() == ''

    def test_formattedText(self, qtbot):
        dialog = CameraInformationDialog()
        qtbot.addWidget(dialog)

        cameraInfo = OrderedDict()
        cameraInfo['Model'] = "Tester"
        cameraInfo['Vendor'] = "Good Times"
        cameraInfo['Width'] = 600
        cameraInfo['Height'] = 400

        dialog.setCameraInformation(cameraInfo)
        dialog.show()

        truthText = ['Model: Tester', 'Vendor: Good Times',
                     'Width: 600', 'Height: 400']
        truthString = os.linesep.join(truthText)

        assert dialog.cameraInfoTextBrowser.toPlainText() == truthString
