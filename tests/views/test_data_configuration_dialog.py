#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QDialogButtonBox

from spot_motion_monitor.config import DataConfig
from spot_motion_monitor.views import DataConfigurationDialog

class TestDataConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'Data'

    def test_setConfiguration(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        truthConfig = DataConfig()
        truthConfig.buffer.pixelScale = 0.54

        ccDialog.setConfiguration(truthConfig)
        assert float(ccDialog.dataConfigTab.pixelScaleLineEdit.text()) == truthConfig.buffer.pixelScale

    def test_getConfiguration(self, qtbot, mocker):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()
        mockGetConfiguration = mocker.patch.object(ccDialog.dataConfigTab, 'getConfiguration')

        ccDialog.getConfiguration()
        assert mockGetConfiguration.call_count == 1

    def test_validInputFromTabs(self, qtbot):
        ccDialog = DataConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        ccDialog.dataConfigTab.pixelScaleLineEdit.setText(str(-1))
        assert ccDialog.buttonBox.button(QDialogButtonBox.Ok).isEnabled() is False
