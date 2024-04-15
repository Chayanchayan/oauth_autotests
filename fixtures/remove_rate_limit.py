import requests
import pytest
from constants import MockTeacherData, Constants


@pytest.fixture(scope="class")
def remove_rate_limit():
    data = {"untrottled": {"data": MockTeacherData.MOCK_TEACHER_USERNAME, "type": "email"}}
    response = requests.post(
        f'https://{Constants.key}@core-main-qa-gateway.stage-uchi.ru/auth/private/remove-from-trottle', json=data)
    if response.status_code == 200:
        print("Teacher was untrottled")
    else:
        print(f"{response.status_code} Teacher wasn't untrottled")
