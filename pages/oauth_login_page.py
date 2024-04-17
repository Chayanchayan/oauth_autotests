import random

from playwright.async_api import Page
from constants import MockStudentData, MockTeacherData, MockParentData
from locators.oauth_login_page_locators import GeneralLoginPage, BindAccountPage, ParentRegistraionPage, ParentLKPage, \
    StudentRegistrationPage
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
        self.input(GeneralLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_student_other_account(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными студента все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Нажать 'Войти с другого аккаунта'"""
        self.click(BindAccountPage.OTHER_ACCOUNT_BTN)

    def mock_student_teacher_login(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными учителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

    def mock_parent_registration(self):
        """Открыть страницу логина"""
        self.open(MockParentData.MOCK_PARENT_URL)

        """Нажать 'У меня нет аккаунта Учи.ру'"""
        self.click(ParentRegistraionPage.REG_BTN)

        """Заполнить форму регистрации родителя"""
        self.input(ParentRegistraionPage.NAME_INPUT, MockParentData.MOCK_PARENT_USERNAME)
        self.input(ParentRegistraionPage.EMAIL_INPUT, MockParentData.MOCK_PARENT_EMAIL)

        self.input(ParentRegistraionPage.PHONE_INPUT, MockParentData.MOCK_PARENT_PHONE)
        self.click(ParentRegistraionPage.TERMS_CHECKBOX)

        """Нажать 'Продолжить'"""
        self.click(ParentRegistraionPage.CONTINUE_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_parent_student_registration(self):
        """Нажать 'Зарегистрировать' в ЛК родителя"""
        self.click(ParentLKPage.REGISTER_STUDENT_BTN)

        """Нажать 'Добавить'"""
        self.click(StudentRegistrationPage.ADD_BTN)

        """Заполнить данными студента все инпуты"""
        self.input(StudentRegistrationPage.NAME_INPUT, MockStudentData.MOCK_STUDENT_REG_NAME)
        self.input(StudentRegistrationPage.SURNAME_INPUT, MockStudentData.MOCK_STUDENT_REG_SURNAME)
        self.select_random_dropdown_value(StudentRegistrationPage.CLASS_DROPDOWN,
                                          StudentRegistrationPage.CLASS_DROPDOWN_LIST)

        """Продолжить"""
        self.click(StudentRegistrationPage.CONTINUE_BTN)
        self.click(StudentRegistrationPage.CONTINUE_BTN_2)

    def mock_parent_with_several_student_login(self):
        """Открыть страницу логина"""
        self.open(MockStudentData.MOCK_STUDENT_URL)

        """Заполнить данными родителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockParentData.MOCK_PARENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockParentData.MOCK_PARENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Выбрать студента"""
        self.click(GeneralLoginPage.ACTIVATE_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

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
