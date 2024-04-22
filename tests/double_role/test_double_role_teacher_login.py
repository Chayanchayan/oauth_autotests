import pytest

from constants import DoubleRoleData
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-31"""


@pytest.mark.regression
@pytest.mark.usefixtures("remove_teacher_rate_limit")
@pytest.mark.parametrize("unbind_user", ["mock-teacher-parent"], indirect=True)
class TestDoubleRoleTeacherLogin:
    def test_double_role_teacher_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_double_role_teacher_login()
        login.is_on_teacher_lk()
