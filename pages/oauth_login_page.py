from playwright.async_api import Page
from constants import MockStudentData, MockTeacherData, MockParentData, DoubleRoleData
from locators.oauth_login_page_locators import (GeneralLoginPage, BindAccountPage, ParentRegistrationPage,
                                                ParentLKPage,
    StudentRegistrationPage, TeacherRegistrationPage, DoubleRolePage)
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
        self.click(ParentRegistrationPage.REG_BTN)

        """Заполнить форму регистрации родителя"""
        self.input(ParentRegistrationPage.NAME_INPUT, MockParentData.MOCK_PARENT_USERNAME)
        self.input(ParentRegistrationPage.EMAIL_INPUT, MockParentData.MOCK_PARENT_EMAIL)

        self.input(ParentRegistrationPage.PHONE_INPUT, MockParentData.MOCK_PARENT_PHONE)
        self.click(ParentRegistrationPage.TERMS_CHECKBOX)

        """Нажать 'Продолжить'"""
        self.click(ParentRegistrationPage.CONTINUE_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_teacher_registration(self):
        """Открыть страницу логина"""
        self.open(MockTeacherData.MOCK_TEACHER_URL)

        """Нажать 'У меня нет аккаунта Учи.ру'"""
        self.click(ParentRegistrationPage.REG_BTN)

        """Заполнить форму регистрации учителя"""
        self.input(TeacherRegistrationPage.NAME_INPUT, MockTeacherData.MOCK_TEACHER_NAME)
        self.input(TeacherRegistrationPage.SURNAME_INPUT, MockTeacherData.MOCK_TEACHER_SURNNAME)
        self.input(TeacherRegistrationPage.PATRONYMIC_INPUT, MockTeacherData.MOCK_TEACHER_PATRONYMIC)
        self.input(TeacherRegistrationPage.EMAIL_INPUT, MockTeacherData.MOCK_TEACHER_EMAIL)
        self.input(TeacherRegistrationPage.PHONE_INPUT, MockTeacherData.MOCK_TEACHER_PHONE)
        self.input(TeacherRegistrationPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_REG_PASSWORD)
        self.click(TeacherRegistrationPage.TERMS_CHECKBOX)

        """Нажать 'Продолжить'"""
        self.click(TeacherRegistrationPage.CONTINUE_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

        "Заполнить данные региона, школы и перейти на следующий шаг"
        self.click(TeacherRegistrationPage.REGION_DROPDOWN)
        self.click(TeacherRegistrationPage.MOSCOW_OPTION)
        self.click(TeacherRegistrationPage.SCHOOL_DROPDOWN)
        # по какой-то причине обычный клик на школу не срабатывает и приходится кликать еще раз
        self.click(TeacherRegistrationPage.FIRST_SCHOOL)
        self.click(TeacherRegistrationPage.REGION_CONTINUE_BTN)

        "Заполнить данные класса и перейти на следующий шаг"
        self.click(TeacherRegistrationPage.MATH_CHECKBOX)
        self.click(TeacherRegistrationPage.RUSSIAN_LANG_CHECKBOX)
        self.click(TeacherRegistrationPage.SUBJECTS_CONTINUE_BTN)

        "Добавить учеников в класс и перейти на следующий шаг"
        self.input(TeacherRegistrationPage.STUDENT_NAME_INPUT, MockTeacherData.MOCK_TEACHER_STUDENT_NAME_INPUT)
        self.click(TeacherRegistrationPage.STUDENT_SEX_INPUT)
        self.click(TeacherRegistrationPage.STUDENT_DATA_CONTINUE_BTN)

        "Просмотреть данные учеников и завершить регистрацию"
        self.click(TeacherRegistrationPage.DONE_BTN)

        "Заполнить данные еще одного класса и перейти на следующий шаг"
        self.click(TeacherRegistrationPage.SECOND_MATH_CHECKBOX)
        self.click(TeacherRegistrationPage.SECOND_LANG_CHECKBOX)
        self.click(TeacherRegistrationPage.SECOND_SUBJECTS_CONTINUE_BTN)
        #
        # "Просмотреть информацию о передаче доступа родителям и перейти на следующий шаг"
        # self.click(TeacherRegistrationPage.PARENT_ACCESS_BTN)
        #
        # "Перейти в личный кабинет"
        # self.click(TeacherRegistrationPage.TEACHER_LK_BTN)

    def mock_teacher_login(self):
        """Открыть страницу логина"""
        self.open(MockTeacherData.MOCK_TEACHER_URL)

        """Заполнить данными учителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_teacher_other_account(self):
        """Открыть страницу логина"""
        self.open(MockTeacherData.MOCK_TEACHER_URL)

        """Заполнить данными учителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Нажать 'Войти с другого аккаунта'"""
        self.click(BindAccountPage.OTHER_ACCOUNT_BTN)

    def mock_teacher_student_login(self):
        """Открыть страницу логина"""
        self.open(MockTeacherData.MOCK_TEACHER_URL)

        """Заполнить данными ученика все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockStudentData.MOCK_STUDENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

    def mock_double_role_parent_wrong_login(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

        """Выбрать роль учителя"""
        self.click(DoubleRolePage.FIRST_ROLE_BLOCK)

        """Заполнить данными родителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockParentData.MOCK_PARENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockParentData.MOCK_PARENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

    def mock_double_role_teacher_wrong_login(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

        """Выбрать роль родителя"""
        self.click(DoubleRolePage.SECOND_ROLE_BLOCK)

        """Заполнить данными родителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

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

    def check_mock_double_role_page(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

    def mock_double_role_teacher_login(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

        """Выбрать роль учителя"""
        self.click(DoubleRolePage.FIRST_ROLE_BLOCK)

        """Заполнить данными учителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockTeacherData.MOCK_TEACHER_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockTeacherData.MOCK_TEACHER_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_double_role_other_account_login(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

        """Выбрать роль учителя"""
        self.click(DoubleRolePage.FIRST_ROLE_BLOCK)

        """Заполнить данными родителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockParentData.MOCK_PARENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockParentData.MOCK_PARENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Нажать 'Войти с другого аккаунта'"""
        self.click(BindAccountPage.DOUBLE_ROLE_OTHER_ACCOUNT_BUTTON)

    def mock_double_role_parent_login(self):
        """Открыть страницу логина"""
        self.open(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL)

        """Выбрать роль родителя"""
        self.click(DoubleRolePage.SECOND_ROLE_BLOCK)

        """Заполнить данными родителя все инпуты"""
        self.input(GeneralLoginPage.LOGIN_INPUT, MockParentData.MOCK_PARENT_LOGIN_USERNAME)
        self.input(GeneralLoginPage.PASSWORD_INPUT, MockParentData.MOCK_PARENT_LOGIN_PASSWORD)

        """Сабмит"""
        self.click(GeneralLoginPage.LOGIN_BTN)

        """Связать аккаунты"""
        self.click(BindAccountPage.BIND_BTN)

    def mock_student_receive_incorrect_token(self):
        """Открыть страницу логина с неправильным токеном"""
        self.open(MockStudentData.MOCK_STUDENT_BROKEN_URL)

    def is_on_student_lk(self):
        """Проверка перехода в личный кабинет ученика"""
        self.assertions.check_url(MockStudentData.MOCK_STUDENT_LK_URL, "We're not in student's lk page!")

    def is_on_teacher_lk(self):
        """Проверка перехода в личный кабинет учителя"""
        self.assertions.check_url(MockTeacherData.MOCK_TEACHER_LK_URL, "We're not in teacher's lk page!")

    def is_on_student_uchi_login(self):
        """Проверка перехода на страницу авторизации учи.ру"""
        self.assertions.check_url(MockStudentData.MOCK_STUDENT_URL, "We're not on student uchi.ru login page!")

    def is_on_teacher_uchi_login(self):
        """Проверка перехода на страницу авторизации учи.ру"""
        self.assertions.check_url(MockTeacherData.MOCK_TEACHER_URL, "We're not on teacher uchi.ru login page!")

    def is_on_double_role_uchi_login(self):
        """Проверка перехода на страницу авторизации учи.ру"""
        self.assertions.check_url(DoubleRoleData.MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL,
                                  "We're not on double role uchi.ru login page!")

    def is_error_message_received(self, error_message_block, error_message):
        """Проверка получения сообщения о какой-либо ошибке"""
        self.assertions.is_element_containing_text(error_message_block, error_message,
                                                   "The error message was not received!")

    def is_in_class_page(self):
        """Проверка нахождения учителя на странице последнего добавленного класса"""
        self.assertions.has_text(TeacherRegistrationPage.CLASS_CODE_BLOCK, MockTeacherData.MOCK_TEACHER_CLASS_CODE_TEXT,
                                 "We're not in class page!")

    def is_double_role_displayed(self, first_role, second_role):
        """Проверка нахождения на странице с двойной ролью"""
        self.assertions.has_text(DoubleRolePage.FIRST_ROLE_BLOCK, first_role,
                                 "First role is not displayed!")
        self.assertions.has_text(DoubleRolePage.SECOND_ROLE_BLOCK, second_role,
                                 "Second role is not displayed!")
