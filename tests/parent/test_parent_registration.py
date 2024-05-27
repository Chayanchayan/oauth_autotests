import pytest
from pages.oauth_login_page import MockLogin

"""https://app.qase.io/case/OAU-8"""


@pytest.mark.regression
@pytest.mark.parametrize("unbind_user", ["mock-parent"], indirect=True)
@pytest.mark.skip
class TestMockParentRegistration:
    def test_mock_parent_registration(self, browser, unbind_user):
        login = MockLogin(browser)
        login.mock_parent_registration()
        login.mock_parent_student_registration()
        login.is_on_student_lk()
