import pytest
import testit

from constants import RoleMismatchData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3615)
@pytest.mark.regression
@pytest.mark.usefixtures("remove_teacher_rate_limit")
class TestMockStudentTeacherLogin:
    def test_mock_student_teacher_login(self, browser):
        login = MockLogin(browser)
        login.mock_student_teacher_login()
        login.is_error_message_received(error_message_block=ErrorMessagePage.ROLE_MISMATCH_MESSAGE_BLOCK,
                                        error_message=RoleMismatchData.TEACHER_ROLE_MISMATCH_MESSAGE)
