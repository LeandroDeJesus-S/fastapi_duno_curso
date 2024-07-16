from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message

api = FastAPI()


@api.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@api.get('/html', response_class=HTMLResponse)
def read_html():
    return '<h1>Olá Mundo!</h1>'
