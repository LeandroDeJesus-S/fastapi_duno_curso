from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import api


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(api)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_html_deve_retornar_html():
    client = TestClient(api)
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Olá Mundo!</h1>'
