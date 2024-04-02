import time
import pytest
from pages.mock_login_page import MockLogin


@pytest.mark.smoke
class TestMockStudentLogin:
    def test_mock_student_login(self, browser):
        login = MockLogin(browser)
        login.mock_student_login()
        # time.sleep(234234234)
