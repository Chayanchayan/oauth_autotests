import pytest
import testit
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3619)
@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-student"], indirect=True)
@pytest.mark.usefixtures("remove_parent_rate_limit")
class TestMockStudentLogin:
    def test_mock_student_login(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_parent_with_several_student_login()
        login.is_on_student_lk()
