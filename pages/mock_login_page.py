from playwright.async_api import Page
from constants import MockStudentData
from locators.mock_login_page import StudentLoginPage, BindAccountPage
from pages.base import Base
from data.assertions import Assertions


class MockLogin(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def mock_student_login(self):
        # открыть страницу логина
        self.open(MockStudentData.MOCK_STUDENT_URL)

        # заполнить данными все инпуты
        self.input(StudentLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_USERNAME)
        self.input(StudentLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_PASSWORD)

        # сабмит
        self.click(StudentLoginPage.LOGIN_BTN)

        # связать аккаунты
        self.click(BindAccountPage.BIND_BTN)

