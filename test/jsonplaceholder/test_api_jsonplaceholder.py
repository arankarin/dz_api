import pytest
import requests

@pytest.mark.parametrize('id_', [1, 3, 5])
def test_getting_resource(base_url, id_):
    response = requests.get(base_url + str(id_))
    res = response.json()
    assert response.status_code == 200
    assert res["id"] == id_


@pytest.mark.parametrize("body_, user_id", [
                            ('test001', 2),
                            ('test001', 3),
                            ('test001', 4),])
def test_greating_resource(base_url, body_, user_id):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json_ = {"title": 'foo', "body": body_, "userId": user_id}
    response = requests.post(base_url, headers=headers, json=json_)
    res = response.json()
    assert response.status_code == 201
    assert res["body"] == body_
    assert res["userId"] == user_id


@pytest.mark.parametrize("id_, user_id", [
                                        (1, 1),
                                        (2, 2)])
def test_updating_resource(base_url,id_, user_id):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json_ = {"id": id_, "title": 'foo', "body": 'bar', "userId": user_id}
    response = requests.put(base_url + str(id_), headers=headers, json=json_)
    res = response.json()
    assert response.status_code == 200
    assert res["id"] == id_
    assert  res["userId"] == user_id


@pytest.mark.parametrize("id_, title_", [
                                    (1, 'test001'),
                                    (2, 'test002')])
def test_Patching_resource(base_url, id_, title_):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json_ = {"title": title_}
    response = requests.patch(base_url + str(id_), headers=headers, json=json_)
    res = response.json()
    assert response.status_code == 200
    assert res['id'] == id_
    assert res['title'] == title_

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_Listing_nested_resources(base_url, post_id):
    response = requests.get(base_url + str(post_id) + '/comments')
    res = response.json()
    assert response.status_code == 200
    assert res[0]['postId'] == post_id

