import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        # action="store",
        default="https://api.openbrewerydb.org/breweries/",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

