from requests import delete, get, post, put

print(
    get(
        "http://localhost:5000/api/users",
    ).json()
)  # ОК

print(
    post(
        "http://localhost:5000/api/users",
        json={
            "surname": "testtt",
            "name": "test",
            "age": 12321,
            "speciality": "-----",
            "address": "fewfwe",
            "email": "ffff@a.com",
            "password": "123",
        },
    ).json()
)  # OK

print(
    get(
        "http://localhost:5000/api/users/1",
    ).json()
)  # OK {'user': {'address': None, 'age': 12222, 'email': 'a@a.com', 'id': 1, 'modified_date': '2025-04-01 15:16:46', 'name': 'AAA', 'position': None, 'speciality': None, 'surname': 'BBB'}}

print(
    post(
        "http://localhost:5000/api/users",
        json={
            "surname": "testtt",
            "name": "test",
            "age": 12321,
            "speciality": "-----",
            "address": "fewfwe",
            "email": "ffff@a.com",
            "password": "123",
        },
    ).json()
)  # {'error': 'Such email is already used'}

print(
    put(
        "http://localhost:5000/api/users/1",
        json={
            "surname": "not test",
        },
    ).json()
)  # OK {'id': 1}

print(
    get(
        "http://localhost:5000/api/users/1",
    ).json()
)  # OK {'id': 1}
# surname изменился, как видно {'user': {'address': None, 'age': 12222, 'email': 'a@a.com', 'id': 1, 'modified_date': '2025-04-01 15:16:46', 'name': 'AAA', 'position': None, 'speciality': None, 'surname': 'not test'}}

print(
    delete(
        "http://localhost:5000/api/users/2",
    ).json()
)
# {'message': 'User with id=2 was fired'}
