import pytest
import testit
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3616)
@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
class TestMockStudentOtherAccountLogin:
    def test_mock_student_other_account_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_student_other_account()
        login.is_on_student_uchi_login()
