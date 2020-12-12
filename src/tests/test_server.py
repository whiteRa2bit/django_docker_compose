import os
import json

import requests

SERVER_HOST = os.environ.get('HSE_HTTP_TESTS_SERVER_HOST', 'server')
SERVER_PORT = int(os.environ.get('HSE_HTTP_FLASK_PORT', 80))
ITEM_ID = 1
URL = 'http://' + SERVER_HOST
GET_ITEMS_URL = URL + '/items'
GET_ITEM_URL = URL + '/items/{}'.format(ITEM_ID)
ADD_ITEM_URL = URL + '/items/add'.format(ITEM_ID)
UPDATE_ITEM_URL = URL + '/items/update/{}'.format(ITEM_ID)
DELETE_ITEM_URL = URL + '/items/delete/{}'.format(ITEM_ID)
if SERVER_PORT != 80:
    URL += ':{}'.format(SERVER_PORT)

BASE_ITEM = {
    "name": "ds_hse",
    "topic": "distributed systems",
    "rate": 10,
    "link": "https://github.com/osukhoroslov/hse-ds-2020"
}


def test_get_items():
    response = requests.get(GET_ITEMS_URL)
    body = json.loads(response.content)
    assert response.status_code == 200
    assert body["data"] == []


def test_add_item():
    response = requests.post(ADD_ITEM_URL, data=json.dumps(BASE_ITEM))
    body = json.loads(response.content)
    assert response.status_code == 200
    assert body["data"] == {**{"id": ITEM_ID}, **BASE_ITEM}


def test_get_item():
    response = requests.get(GET_ITEM_URL)
    body = json.loads(response.content)
    assert response.status_code == 200
    assert body["data"] == {**{"id": ITEM_ID}, **BASE_ITEM}


def test_update_item(new_name="hse_ds"):
    update_params = {"name": new_name}
    response = requests.patch(UPDATE_ITEM_URL, data=json.dumps(update_params))
    body = json.loads(response.content)
    assert response.status_code == 200
    real = {**{"id": ITEM_ID}, **BASE_ITEM}
    real["name"] = new_name
    assert body["data"] == real


def test_delete_item():
    response = requests.delete(DELETE_ITEM_URL)
    assert response.status_code == 200
    response = requests.get(GET_ITEMS_URL)
    body = json.loads(response.content)
    assert response.status_code == 200
    assert body["data"] == []
