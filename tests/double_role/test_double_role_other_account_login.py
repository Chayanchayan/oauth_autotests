import pytest

from constants import DoubleRoleData, RoleMismatchData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-35"""


@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-teacher-parent"], indirect=True)
class TestDoubleRoleOtherAccountLogin:
    def test_double_role_other_account_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_double_role_other_account_login()
        login.is_on_double_role_uchi_login()
