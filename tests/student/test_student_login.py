import pytest
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-3"""


@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
class TestMockStudentLogin:
    def test_mock_student_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_student_login()
        login.is_on_student_lk()
