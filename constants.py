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
    MOCK_PARENT_USERNAME = rn.get_person()
    MOCK_PARENT_EMAIL = generate_random_email()
    MOCK_PARENT_PHONE = generate_random_phone_number()


class MockTeacherData:
    MOCK_TEACHER_USERNAME = "teacher1@uchi.ru"
    MOCK_TEACHER_PASSWORD = "1"


class IncorrectTokenData:
    INCORRECT_TOKEN_MESSAGE = ("Невозможно получить информацию по данному токену, попробуйте еще раз или обратитесь в "
                               "поддержку")


class RoleMismatchData:
    TEACHER_ROLE_MISMATCH_MESSAGE = "Вы авторизованы как учитель на Учи.ру"
