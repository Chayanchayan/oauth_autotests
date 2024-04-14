from playwright.async_api import Page
from constants import MockStudentData
from locators.oauth_login_page_locators import StudentLoginPage, BindAccountPage
from pages.base import Base
from data.assertions import Assertions


class MockLogin(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertions(page)

    def mock_student_login(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными все инпуты"""
        self.input(StudentLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_USERNAME)
        self.input(StudentLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_PASSWORD)

        """Сабмит"""
        self.click(StudentLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def is_on_student_lk(self):
        """Проверка перехода в личный кабинет ученика"""
        self.assertions.check_url(MockStudentData.MOCK_STUDENT_LK_URL, "We're not in student's lk!")
