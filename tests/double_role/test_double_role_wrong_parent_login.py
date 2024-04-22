import pytest

from constants import DoubleRoleData, RoleMismatchData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-33"""


@pytest.mark.regression
class TestDoubleRoleParentWrongLogin:
    def test_double_role_parent_wrong_login(self, browser):
        login = MockLogin(browser)
        login.mock_double_role_parent_wrong_login()
        login.is_error_message_received(error_message_block=ErrorMessagePage.ROLE_MISMATCH_MESSAGE_BLOCK,
                                        error_message=RoleMismatchData.PARENT_ROLE_MISMATCH_MESSAGE)
