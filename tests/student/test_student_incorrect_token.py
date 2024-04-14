import pytest
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-17"""


@pytest.mark.regression
class TestMockStudentReceiveIncorrectToken:
    def test_mock_student_receive_incorrect_token(self, browser):
        login = MockLogin(browser)
        login.mock_student_receive_incorrect_token()
        login.is_broken_token_message_received()
