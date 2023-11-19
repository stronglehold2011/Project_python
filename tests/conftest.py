import pytest

@pytest.fixture()
def set_up():
    print("Start test")

    yield
    print("Finish test")


@pytest.fixture(scope="module") # scope="module" указывает, что данный метод относится к самому файлу, в котором его
# используют. Мы пишем set_group в любом из тестов файла и он применится ко всему файлу целиком.
def set_group():
    print("Enter system")

    yield
    print("Exit system")