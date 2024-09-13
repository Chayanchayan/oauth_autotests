import os
from russian_names import RussianNames

from helpers import (generate_random_email,
                     generate_random_phone_number)

rn = RussianNames()


class Constants:
    try:
        key = os.getenv('API_KEY')
    except KeyError:
        print("API KEY wasn't found")


class Providers:
    STUDENT_PROVIDER = "mock-student"


class TestData:
    MOCK_INPUT_DATA = "test"
    MOCK_LOGIN_PAGE = ("https://oauth-mock.stage-uchi.ru/mock-student/authorize?client_id=butler&nonce"
                       "=ed1856158e3c7f56cf3909d140b30cd9&redirect_uri=https%3A%2F%2Foauth-gw.stage-uchi.ru%2Fauth"
                       "%2Foidc%2Frps%2Fmock-student%2Fcallback&response_type=code&scope=openid&state"
                       "=ed1856158e3c7f56cf3909d140b30cd9")


class MockStudentData:
    MOCK_STUDENT_URL = ("https://core-main-auth.stage-uchi.ru/oauth/connect?token=eyJhbGciOiJIUzI1NiJ9"
                        ".eyJpZGVudGlmaWVyIjoic2QiLCJwcm92aWRlciI6Im1vY2stc3R1ZGVudCIsImhvc3QiOiJodHRwc"
                        "zovL29hdXRoLW1vY2suc3RhZ2UtdWNoaS5ydS9tb2NrLXN0dWRlbnQiLCJwcm92aWRlcl9uYW1lIjoi"
                        "0KPRh9C10L3QuNGH0LXRgdC60LjQuSIsInByb3ZpZGVyX2Rlc2NyaXB0aW9uIjoi0KLQtdGB0YLQvtC"
                        "y0YvQuSDQv9GA0L7QstCw0LnQtNC10YAuINCj0YfQtdC90LjQui4iLCJhY2NvdW50X2lkIjpudWxsLC"
                        "JyZWRpcmVjdF91cmkiOiJodHRwczovL2NvcmUtbWFpbi5zdGFnZS11Y2hpLnJ1IiwiZXJyb3IiOm51bG"
                        "wsImVycm9yX2Rlc2NyaXB0aW9uIjpudWxsLCJlcnJvcl91cmkiOm51bGwsImFjY2Vzc190b2tlbiI6b"
                        "nVsbCwiYXV0aG9yaXphdGlvbl91cmkiOiJodHRwczovL2NvcmUtbWFpbi1hdXRoLnN0YWdlLXVjaGkuc"
                        "nUvYXV0aC9vaWRjLXJwP2hvc3Q9aHR0cHMlM0ElMkYlMkZvYXV0aC1tb2NrLnN0YWdlLXVjaGkucnUlM"
                        "kZtb2NrLXN0dWRlbnQifQ.QbC4VEx15R6Av5qk3v24giPWvGP6_Icvmaj4zZ0qx3I")
    MOCK_STUDENT_BROKEN_URL = ("https://core-main-auth.stage-uchi.ru/oauth/connect?token=eyJhbGciOiJIUzI1NiJ9"
                               ".eyJpZGVudGlmaWjoic2QiLCJwcm92aWRlciI6Im1vY2stc3R1ZGVudCIsImhvc3QiOiJodHRwc"
                               "zovL29hdXRoLW1vY2suc3RhZ2UtdWNoaS5ydS9tb2NrLXN0dWRlbnQiLCJwcm92aWRlcl9uYW1lIjoi"
                               "0KPRh9C10L3QuNGH0LXRgdC60LjQuSIsInByb3ZpZGVyX2Rlc2NyaXB0aW9uIjoi0KLQtdGB0YLQvtC"
                               "y0YvQuSDQv9GA0L7QstCw0LnQtNC10YAuINCj0YfQtdC90LjQui4iLCJhY2NvdW50X2lkIjpudWxsLC"
                               "JyZWRpcmVjdF91cmkiOiJodHRwczovL2NvcmUtbWFpbi5zdGFnZS11Y2hpLnJ1IiwiZXJyb3IiOm51bG"
                               "wsImVycm9yX2Rlc2NyaXB0aW9uIjpudWxsLCJlcnJvcl91cmkiOm51bGwsImFjY2Vzc190b2tlbiI6b"
                               "nVsbCwiYXV0aG9yaXphdGlvbl91cmkiOiJodHRwczovL2NvcmUtbWFpbi1hdXRoLnN0YWdlLXVjaGkuc"
                               "nUvYXV0aC9vaWRjLXJwP2hvc3Q9aHR0cHMlM0ElMkYlMkZvYXV0aC1tb2NrLnN0YWdlLXVjaGkucnUlM"
                               "kZtb2NrLXN0dWRlbnQifQ.QbC4VEx15R6Av5qk3v24giPWvGP6_Icvmaj4zZ0qx3I")
    MOCK_STUDENT_LOGIN_USERNAME = "75"
    MOCK_STUDENT_LOGIN_PASSWORD = "схема33850"
    MOCK_STUDENT_LK_URL = "https://core-main.stage-uchi.ru/profile/students"
    MOCK_STUDENT_REG_NAME = "Студент"
    MOCK_STUDENT_REG_SURNAME = "Тестовый"


class MockParentData:
    MOCK_PARENT_URL = ("https://core-main-auth.stage-uchi.ru/oauth/connect?token=eyJhbGciOiJIUzI1NiJ9"
                       ".eyJpZGVudGlmaWVyIjoic2QiLCJwcm92aWRlciI6Im1vY2stcGFyZW50IiwiaG9zdCI6Imh0dHBzOi"
                       "8vb2F1dGgtbW9jay5zdGFnZS11Y2hpLnJ1L21vY2stcGFyZW50IiwicHJvdmlkZXJfbmFtZSI6ItCg0"
                       "L7QtNC40YLQtdC70YzRgdC60LjQuSIsInByb3ZpZGVyX2Rlc2NyaXB0aW9uIjoi0KLQtdGB0YLQvtCy0"
                       "YvQuSDQv9GA0L7QstCw0LnQtNC10YAuINCg0L7QtNC40YLQtdC70YwuIiwiYWNjb3VudF9pZCI6bnVs"
                       "bCwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9jb3JlLW1haW4uc3RhZ2UtdWNoaS5ydSIsImVycm9yI"
                       "jpudWxsLCJlcnJvcl9kZXNjcmlwdGlvbiI6bnVsbCwiZXJyb3JfdXJpIjpudWxsLCJhY2Nlc3NfdG9"
                       "rZW4iOm51bGwsImF1dGhvcml6YXRpb25fdXJpIjoiaHR0cHM6Ly9jb3JlLW1haW4tYXV0aC5zdGFn"
                       "ZS11Y2hpLnJ1L2F1dGgvb2lkYy1ycD9ob3N0PWh0dHBzJTNBJTJGJTJGb2F1dGgtbW9jay5zdGFn"
                       "ZS11Y2hpLnJ1JTJGbW9jay1wYXJlbnQifQ.D7-iypA1ugRFYRprTU9gkfx096D0vXs95SFFuoHfs2A")
    MOCK_PARENT_LOGIN_USERNAME = "parent271@uchi.ru"
    MOCK_PARENT_LOGIN_PASSWORD = "1"
    MOCK_PARENT_USERNAME = rn.get_person()
    MOCK_PARENT_EMAIL = generate_random_email()
    MOCK_PARENT_PHONE = generate_random_phone_number()


class MockTeacherData:
    MOCK_TEACHER_URL = ("https://core-main-auth.stage-uchi.ru/oauth/connect?token=eyJhbGciOiJIUzI1NiJ9"
                        ".eyJpZGVudGlmaWVyIjoic2QiLCJwcm92aWRlciI6Im1vY2stdGVhY2hlciIsImhvc3QiOiJod"
                        "HRwczovL29hdXRoLW1vY2suc3RhZ2UtdWNoaS5ydS9tb2NrLXRlYWNoZXIiLCJwcm92aWRlc"
                        "l9uYW1lIjoi0KPRh9C40YLQtdC70YzRgdC60LjQuSIsInByb3ZpZGVyX2Rlc2NyaXB0aW9u"
                        "Ijoi0KLQtdGB0YLQvtCy0YvQuSDQv9GA0L7QstCw0LnQtNC10YAuINCj0YfQuNGC0LXQu"
                        "9GMLiIsImFjY291bnRfaWQiOm51bGwsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vY29yZS"
                        "1tYWluLnN0YWdlLXVjaGkucnUiLCJlcnJvciI6bnVsbCwiZXJyb3JfZGVzY3JpcHRpb24"
                        "iOm51bGwsImVycm9yX3VyaSI6bnVsbCwiYWNjZXNzX3Rva2VuIjpudWxsLCJhdXRob3Jpe"
                        "mF0aW9uX3VyaSI6Imh0dHBzOi8vY29yZS1tYWluLWF1dGguc3RhZ2UtdWNoaS5ydS9hdXRo"
                        "L29pZGMtcnA_aG9zdD1odHRwcyUzQSUyRiUyRm9hdXRoLW1vY2suc3RhZ2UtdWNoaS5ydSU"
                        "yRm1vY2stdGVhY2hlciJ9.Kt0xGJConRRU9z3IzM9wsxiyse84Yc-B61ppSbFeKDw")
    MOCK_TEACHER_USERNAME = "teacher1@uchi.ru"
    MOCK_TEACHER_PASSWORD = "1"
    MOCK_TEACHER_NAME = "Учитель"
    MOCK_TEACHER_SURNNAME = "Тестовый"
    MOCK_TEACHER_PATRONYMIC = "Тестович"
    MOCK_TEACHER_EMAIL = generate_random_email()
    MOCK_TEACHER_PHONE = generate_random_phone_number()
    MOCK_TEACHER_REG_PASSWORD = "123456789"
    MOCK_TEACHER_STUDENT_NAME_INPUT = "Тестовый Ученик"
    MOCK_TEACHER_LK_URL = "https://core-main.stage-uchi.ru/teachers/lk"
    MOCK_TEACHER_CLASS_CODE_TEXT = "Код класса:"
    MOCK_TEACHER_LOGIN_PAGE_GREETING_TEXT = "Свяжите аккаунты на Учи.ру и платформе Учительский"


class DoubleRoleData:
    MOCK_DOUBLE_ROLE_TEACHER_PARENT_URL = ("https://core-main-auth.stage-uchi.ru/oauth/connect?token"
                                           "=eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoic2QiLCJwc"
                                           "m92aWRlciI6Im1vY2stdGVhY2hlci1wYXJlbnQiLCJob3N0Ij"
                                           "oiaHR0cHM6Ly9vYXV0aC1tb2NrLnN0YWdlLXVjaGkucnUvb"
                                           "W9jay10ZWFjaGVyLXBhcmVudCIsInByb3ZpZGVyX25hbWUiOi"
                                           "LQo9GH0LjRgtC10LvRjNGB0LrQuNC5L9GA0L7QtNC40YLQtdC70"
                                           "YzRgdC60LjQuSIsInByb3ZpZGVyX2Rlc2NyaXB0aW9uIjoi0KLQt"
                                           "dGB0YLQvtCy0YvQuSDQv9GA0L7QstCw0LnQtNC10YAuINCj0Y"
                                           "fQuNGC0LXQu9GMLdGA0L7QtNC40YLQtdC70YwuIiwiYWNjb3V"
                                           "udF9pZCI6bnVsbCwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9jb"
                                           "3JlLW1haW4uc3RhZ2UtdWNoaS5ydSIsImVycm9yIjpudWxsLCJ"
                                           "lcnJvcl9kZXNjcmlwdGlvbiI6bnVsbCwiZXJyb3JfdXJpIjpud"
                                           "WxsLCJhY2Nlc3NfdG9rZW4iOm51bGwsImF1dGhvcml6YXRpb25f"
                                           "dXJpIjoiaHR0cHM6Ly9jb3JlLW1haW4tYXV0aC5zdGFnZS11Y2"
                                           "hpLnJ1L2F1dGgvb2lkYy1ycD9ob3N0PWh0dHBzJTNBJTJGJTJGb"
                                           "2F1dGgtbW9jay5zdGFnZS11Y2hpLnJ1JTJGbW9jay10ZWFjaGVyL"
                                           "XBhcmVudCJ9.CJi1uRWopV4gFaQcPwnbVoXjKX0aHyGFb12p9H-H-4Y")

    MOCK_DOUBLE_ROLE_TEACHER_BLOCK_TEXT = "Аккаунт учителя"
    MOCK_DOUBLE_ROLE_PARENT_BLOCK_TEXT = "Аккаунт родителя"


class IncorrectData:
    INCORRECT_TOKEN_MESSAGE = ("Невозможно получить информацию по данному токену, попробуйте еще раз или обратитесь в "
                               "поддержку")
    EMAIL_IN_USE_ERROR = "Этот e-mail уже занят"


class RoleMismatchData:
    TEACHER_ROLE_MISMATCH_MESSAGE = "Вы авторизованы как учитель на Учи.ру"
    STUDENT_ROLE_MISMATCH_MESSAGE = "Вы авторизованы как ученик на Учи.ру"
    PARENT_ROLE_MISMATCH_MESSAGE = "Вы авторизованы как родитель на Учи.ру"
