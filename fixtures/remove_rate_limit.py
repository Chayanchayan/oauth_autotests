import requests
import pytest

from constants import MockTeacherData, Constants, MockParentData


@pytest.fixture(scope="class")
def remove_teacher_rate_limit():
    data = {"untrottled": {"data": MockTeacherData.MOCK_TEACHER_USERNAME, "type": "email"}}
    response = requests.post(
        f'https://{Constants.key}@core-main-qa-gateway.stage-uchi.ru/auth/private/remove-from-trottle', json=data)
    if response.status_code == 200:
        print("Teacher was untrottled")
    else:
        print(f"{response.status_code} Teacher wasn't untrottled")


@pytest.fixture(scope="class")
def remove_parent_rate_limit():
    data = {"untrottled": {"data": MockParentData.MOCK_PARENT_LOGIN_USERNAME, "type": "email"}}
    response = requests.post(
        f'https://{Constants.key}@core-main-qa-gateway.stage-uchi.ru/auth/private/remove-from-trottle', json=data)
    if response.status_code == 200:
        print("Parent was untrottled")
    else:
        print(f"{response.status_code} Teacher wasn't untrottled")
