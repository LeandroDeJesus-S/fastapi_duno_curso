from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_html_deve_retornar_html(client):
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Olá Mundo!</h1>'


def test_crete_user(client):
    req_data = {
        'username': 'test_username',
        'password': 'test_password',
        'email': 'test@email.com',
    }
    resp_data = {
        'id': 1,
        'username': 'test_username',
        'email': 'test@email.com',
    }
    response = client.post('/users', json=req_data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == resp_data


def test_read_users(client):
    resp_data = {
        'users': [
            {'id': 1, 'username': 'test_username', 'email': 'test@email.com'}
        ]
    }
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == resp_data


def test_read_user(client):
    resp_data = {
        'id': 1,
        'username': 'test_username',
        'email': 'test@email.com',
    }

    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == resp_data

    response = client.get('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}

    response = client.get('/users/10')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test_username_updated',
            'password': 'test_password',
            'email': 'test@email.com',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'test_username_updated',
        'email': 'test@email.com',
    }


def test_update_user_invalid_id(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'test_username_updated',
            'password': 'test_password',
            'email': 'test@email.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}

    response = client.put(
        '/users/10',
        json={
            'username': 'test_username_updated',
            'password': 'test_password',
            'email': 'test@email.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_user_delete(client):
    response = client.delete('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}

    response = client.delete('/users/10')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}

    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
