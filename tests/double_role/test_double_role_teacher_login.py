import pytest
import testit
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3627)
@pytest.mark.regression
@pytest.mark.usefixtures("remove_teacher_rate_limit")
@pytest.mark.parametrize("unbind_user", ["mock-teacher-parent"], indirect=True)
class TestDoubleRoleTeacherLogin:
    def test_double_role_teacher_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_double_role_teacher_login()
