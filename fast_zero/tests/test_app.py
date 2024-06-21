from http import HTTPStatus

# def test_root_deve_retornar_ok_e_ola_mundo(client):
#     response = client.get('/')  # Act

#     assert response.status_code == HTTPStatus.OK  # Assert
#     assert response.json() == {'message': 'Olá Mundo!'}  # Assert


# def test_ola_mundo_deve_retornar_html_ola_mundo(client):
#     response = client.get('/exercise-ola')

#     assert response.status_code == HTTPStatus.OK
#     assert (
#         response.text
#         == """
#     <html>
#     <body>
#         <h1>Olá mundo!</h1>
#     </body>
#     </html>"""
#     )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'luh',
            'email': 'luh@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'luh',
        'email': 'luh@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'luh',
                'email': 'luh@example.com',
                'id': 1,
            }
        ]
    }


# exercise
def test_read_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'luh',
        'email': 'luh@example.com',
        'id': 1,
    }

    negative_response = client.get('/users/2')
    assert negative_response.status_code == HTTPStatus.NOT_FOUND
    assert negative_response.json() == {'detail': 'User not found'}


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'rafa',
            'email': 'rafa@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'rafa',
        'email': 'rafa@example.com',
        'id': 1,
    }

    # exercise
    negative_response = client.put(
        '/users/2',
        json={
            'username': 'rafa',
            'email': 'rafa@example.com',
            'password': 'secret',
        },
    )

    assert negative_response.status_code == HTTPStatus.NOT_FOUND
    assert negative_response.json() == {'detail': 'User not found'}


def test_delete_users(client):
    response = client.delete(
        '/users/1',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

    # exercise
    negative_response = client.delete(
        '/users/2',
    )

    assert negative_response.status_code == HTTPStatus.NOT_FOUND
    assert negative_response.json() == {'detail': 'User not found'}
