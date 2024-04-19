import pytest
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-14"""


@pytest.mark.regression
@pytest.mark.usefixtures("remove_teacher_rate_limit")
@pytest.mark.parametrize("unbind_user", ["mock-teacher"], indirect=True)
class TestMockOtherAccountLogin:
    def test_mock_teacher_other_account_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_teacher_other_account()
        login.is_on_teacher_uchi_login()
