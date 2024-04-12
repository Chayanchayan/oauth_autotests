from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    'fixtures.page',
    'fixtures.unbind_user'
]


# запуск клинеров, если тесты упали - можно указать несколько фикстур
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        item.fixturenames.append("unbind_user")
