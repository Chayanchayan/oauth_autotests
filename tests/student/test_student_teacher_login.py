import pytest

from constants import RoleMismatchData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-5"""


@pytest.mark.regression
@pytest.mark.skip
@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
class TestMockStudentTeacherLogin:
    def test_mock_student_teacher_login(self, browser, unbind_user):
        # TODO: 429 ошибка
        login = MockLogin(browser)
        login.mock_student_teacher_login()
        login.is_error_message_received(error_message_block=ErrorMessagePage.TEACHER_ROLE_MISMATCH_MESSAGE_BLOCK,
                                        error_message=RoleMismatchData.TEACHER_ROLE_MISMATCH_MESSAGE)
