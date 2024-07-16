from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from .schemas import Message, UserDB, UserPublicSchema, UserSchema, UsersSchema

api = FastAPI()
database = []


@api.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@api.get('/html', response_class=HTMLResponse)
def read_html():
    return '<h1>Olá Mundo!</h1>'


@api.post(
    '/users', response_model=UserPublicSchema, status_code=HTTPStatus.CREATED
)
def create_users(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@api.get('/users/{user_id}', response_model=UserPublicSchema)
def read_user(user_id: int):
    if user_id > len(database) or user_id <= 0:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='user not found')

    return database[user_id - 1]


@api.get('/users', response_model=UsersSchema)
def read_users():
    return {'users': database}


@api.put('/users/{user_id}', response_model=UserPublicSchema)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id <= 0:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='user not found')

    user_db = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_db
    return user_db


@api.delete('/users/{user_id}', response_model=Message)
def user_delete(user_id: int):
    if user_id > len(database) or user_id <= 0:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='user not found')

    del database[user_id - 1]
    return Message(message='User deleted')
