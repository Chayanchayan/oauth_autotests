import pytest
import testit
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3628)
@pytest.mark.regression
@pytest.mark.usefixtures("remove_parent_rate_limit")
@pytest.mark.parametrize("unbind_user", ["mock-teacher-parent"], indirect=True)
class TestDoubleRoleParentLogin:
    def test_double_role_parent_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_double_role_parent_login()
