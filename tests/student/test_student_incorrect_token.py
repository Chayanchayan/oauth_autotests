import pytest
import testit
from constants import IncorrectData
from locators.oauth_login_page_locators import ErrorMessagePage
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3624)
@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
class TestMockStudentReceiveIncorrectToken:
    def test_mock_student_receive_incorrect_token(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_student_receive_incorrect_token()
        login.is_error_message_received(error_message_block=ErrorMessagePage.TOKEN_ERROR_MESSAGE_BLOCK,
                                        error_message=IncorrectData.INCORRECT_TOKEN_MESSAGE)
