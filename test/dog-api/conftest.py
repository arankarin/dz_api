import pytest
import requests


# Test API: https://dog.ceo/api/
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        # action="store",
        default="https://dog.ceo/api",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

