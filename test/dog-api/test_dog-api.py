import cerberus
import pytest
import requests
from jsonschema import validate


def test_breeds_list_all(base_url):
    """Проверка структуры ответа за запрос /list/all"""
    res = requests.get(base_url + "/breeds/list/all")

    schema = {
        "message": {"type": "dict"},
        "status": {"type": "string"}
        }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


@pytest.mark.parametrize('url', ['/breeds/image/random', '/breeds/hound/images', '/breeds/hound/list'])
def test_breeds_image_random(base_url, url):
    """Проверка структуры ответа за запрос /image/random, /hound/images, 'hound/list"""
    res = requests.get(base_url + url)
    rr = res.json()
    print(type(rr["message"]))
    print(rr["message"])

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
        }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize('url', ['/breeds/list/all', '/breeds/image/random'])
def test_status_pages(base_url, url):
    """Проверка кодов ответов страниц /list/all, /image/random"""
    res = requests.get(base_url + url)
    rr = res.json()
    assert res.status_code == 200
    assert len(rr["message"]) != 0

@pytest.mark.parametrize('amount', [3, 4, 10])
def test_multiplite_img_breed(base_url, amount):
    """Проверка нескольких случайных фото"""
    res = requests.get(base_url + "/breeds/image/random/" + str(amount))
    rr = res.json()
    assert res.status_code == 200
    assert len(rr["message"]) == amount

@pytest.mark.parametrize('breed', ["stbernard", "labrador"])
def test_rsndom_bred(base_url, breed):
    """Проверка случайного фото определенной пароды"""
    res = requests.get(base_url + "/breed/" + breed + "/images/random")
    rr = res.json()
    print(f"rr message = {rr['message']}")
    assert res.status_code == 200
    assert rr["message"].find(breed) > 0





