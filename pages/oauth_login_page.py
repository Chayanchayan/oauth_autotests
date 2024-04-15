from playwright.async_api import Page
from constants import MockStudentData, MockTeacherData
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

        """Заполнить данными студента все инпуты"""
        self.input(StudentLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_USERNAME)
        self.input(StudentLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_PASSWORD)

        """Сабмит"""
        self.click(StudentLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_student_other_account(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными студента все инпуты"""
        self.input(StudentLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_USERNAME)
        self.input(StudentLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_PASSWORD)

        """Сабмит"""
        self.click(StudentLoginPage.LOGIN_BTN)

        """Нажать 'Войти с другого аккаунта'"""
        self.click(BindAccountPage.OTHER_ACCOUNT_BTN)

    def mock_student_teacher_login(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными учителя все инпуты"""
        self.input(StudentLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(StudentLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(StudentLoginPage.LOGIN_BTN)

    def mock_student_receive_incorrect_token(self):
        """Открыть страницу логина с неправильным токеном"""
        self.open(MockStudentData.MOCK_STUDENT_BROKEN_URL)

    def is_on_student_lk(self):
        """Проверка перехода в личный кабинет ученика"""
        self.assertions.check_url(MockStudentData.MOCK_STUDENT_LK_URL, "We're not in student's lk page!")

    def is_on_student_uchi_login(self):
        """Проверка перехода на страницу авторизации учи.ру"""
        self.assertions.check_url(MockStudentData.MOCK_STUDENT_URL, "We're not on student uchi.ru login page!")

    def is_error_message_received(self, error_message_block, error_message):
        """Проверка получения сообщения о какой-либо ошибке"""
        self.assertions.is_element_containing_text(error_message_block, error_message,
                                                   "The error message was not received!")
