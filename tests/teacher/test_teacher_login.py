import pytest
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-15"""


@pytest.mark.regression
@pytest.mark.usefixtures("remove_teacher_rate_limit")
@pytest.mark.parametrize("unbind_user", ["mock-teacher"], indirect=True)
class TestMockTeacherLogin:
    def test_mock_teacher_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_teacher_login()
        login.is_on_teacher_lk()
