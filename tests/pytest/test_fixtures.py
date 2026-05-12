import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print('\n [AUTOUSE] send data to analytics service')
    ...

@pytest.fixture(scope="session")
def settings():
    print('\n [SESSION] init AT settings')
    ...

@pytest.fixture(scope="class")
def user():
    print('\n [CLASS] one time user data creation for test class ')
    ...

@pytest.fixture(scope="function")
def browser():
    print('\n [FUNCTION] browser start on every test')
    ...


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self):
        ...