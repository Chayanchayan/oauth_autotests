import pytest

from constants import RoleMismatchData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-16"""


@pytest.mark.regression
class TestMockTeacherStudentLogin:
    def test_mock_teacher_student_login(self, browser):
        login = MockLogin(browser)
        login.mock_teacher_student_login()
        login.is_error_message_received(error_message_block=ErrorMessagePage.ROLE_MISMATCH_MESSAGE_BLOCK,
                                        error_message=RoleMismatchData.STUDENT_ROLE_MISMATCH_MESSAGE)
