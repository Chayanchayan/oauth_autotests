import pytest
from pages.oauth_login_page import MockLogin


@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
class TestMockStudentLogin:
    def test_mock_student_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_student_login()
