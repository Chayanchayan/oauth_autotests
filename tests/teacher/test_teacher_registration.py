import pytest
import testit
from pages.oauth_login_page import MockLogin


@testit.workItemIds(3620)
@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-teacher"], indirect=True)
@pytest.mark.skip
class TestMockTeacherRegistration:
    def test_mock_teacher_registration(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_teacher_registration()
        login.is_in_class_page()
