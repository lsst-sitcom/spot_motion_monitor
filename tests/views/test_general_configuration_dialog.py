#------------------------------------------------------------------------------
# See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import GeneralConfig
from spot_motion_monitor.views import GeneralConfigurationDialog

class TestGeneralConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = GeneralConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'General'

    def test_setConfiguration(self, qtbot):
        ccDialog = GeneralConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        truthConfig = GeneralConfig()
        truthConfig.site = "Different Mountain"

        ccDialog.setConfiguration(truthConfig)
        assert ccDialog.generalConfigTab.siteNameLineEdit.text() == truthConfig.site

    def test_getConfiguration(self, qtbot, mocker):
        ccDialog = GeneralConfigurationDialog()
        qtbot.addWidget(ccDialog)
        ccDialog.show()
        mockGetConfiguration = mocker.patch.object(ccDialog.generalConfigTab, 'getConfiguration')

        ccDialog.getConfiguration()
        assert mockGetConfiguration.call_count == 1
