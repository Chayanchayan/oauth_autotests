import os


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
    MOCK_STUDENT_USERNAME = "75"
    MOCK_STUDENT_PASSWORD = "схема33850"
    MOCK_STUDENT_LK_URL = "https://core-main.stage-uchi.ru/profile/students"


class IncorrectTokenData:
    INCORRECT_TOKEN_MESSAGE = ("Невозможно получить информацию по данному токену, попробуйте еще раз или обратитесь в "
                               "поддержку")
