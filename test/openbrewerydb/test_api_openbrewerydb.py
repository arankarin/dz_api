import cerberus
import pytest
import requests
from func import dictionary_check_from_response

def test_single_brewery(base_url):
    """Единственная пивоварня, тест по id"""
    response = requests.get(base_url + 'madtree-brewing-cincinnati')
    res = response.json()
    assert response.status_code == 200
    assert dictionary_check_from_response(res)


@pytest.mark.parametrize('per_page', [1, 5, 10])
def test_list_brewery(base_url, per_page):
    """Список пивоварен, проверка на ключи ответа и проверка количества пивоверен"""
    response = requests.get(base_url + '?per_page=' + str(per_page))
    res = response.json()
    assert response.status_code == 200
    assert len(response.json()) == per_page
    assert dictionary_check_from_response(res)
    assert len(res) == per_page

@pytest.mark.parametrize("per_page", [1, 2, 3])
@pytest.mark.parametrize("city", ["San Diego", "Bend"])
def test_by_city(base_url, per_page, city):
    i = 0
    response = requests.get(base_url + '?by_city=' + city + '&per_page=' + str(per_page))
    res = response.json()
    print(f" URL = {base_url + '?by_city=' + city + '&per_page=' + str(per_page)}")
    print(res)
    assert response.status_code == 200
    assert len(response.json()) == per_page
    while i != per_page:
        assert res[i]["city"] == city
        i += 1


@pytest.mark.parametrize("per_page", [1, 4, 3])
@pytest.mark.parametrize("state", ["New York", "California"])
def test_by_state(base_url, per_page, state):
    print(f"base_url  = {base_url}")
    response = requests.get(base_url + '?by_state=' + state + '&per_page=' + str(per_page))
    res = response.json()
    assert response.status_code == 200
    assert len(response.json()) == per_page
    for i in range(len(res)):
        assert res[i]["state"].lower() == state.lower()


@pytest.mark.parametrize("per_page", [2, 2, 3])
@pytest.mark.parametrize("by_postal", ["44107"])
def test_by_postal(base_url, per_page, by_postal):
    response = requests.get(base_url + '?by_postal=' + by_postal + '&per_page=' + str(per_page))
    res = response.json()
    assert response.status_code == 200
    assert len(response.json()) == per_page
    for i in range(len(res)):
        assert by_postal in res[i]["postal_code"]