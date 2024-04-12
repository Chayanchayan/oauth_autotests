import requests
import pytest
from constants import Constants


# @pytest.fixture(scope="class")
# def unbind_student():
#     """
#     Отвязывает студента с OAuth
#     """
#     yield
#     data = {"provider": "mock-student", "identifier": "sd", "account_id": None}
#     res = requests.post(
#         f'https://{Constants.key}@core-main-qa-gateway.stage-uchi.ru/auth/private/update-rp-id', json=data)
#     assert res.status_code == 200, "Student's still bound"

@pytest.fixture(scope="class")
def unbind_user(request):
    """
    Отвязывает студента с OAuth
    """
    yield
    provider = request.param
    data = {"provider": provider, "identifier": "sd", "account_id": None}
    res = requests.post(
        f'https://{Constants.key}@core-main-qa-gateway.stage-uchi.ru/auth/private/update-rp-id', json=data)
    assert res.status_code == 200, f"User's still bound to provider - {provider}"
