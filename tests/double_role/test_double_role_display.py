import pytest

from constants import DoubleRoleData
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-30"""


@pytest.mark.regression
class TestDoubleRoleDisplayLogin:
    def test_double_role_display(self, browser):
        login = MockLogin(browser)
        login.check_mock_double_role_page()
        login.is_first_role_displayed(first_role=DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_BLOCK_TEXT)
        login.is_second_role_displayed(second_role=DoubleRoleData.MOCK_DOUBLE_ROLE_PARENT_BLOCK_TEXT)
