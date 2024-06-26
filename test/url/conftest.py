import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        # action="store",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default="200"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return int(request.config.getoption('--status_code'))