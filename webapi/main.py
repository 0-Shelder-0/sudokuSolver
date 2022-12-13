from os import environ

from fastapi import FastAPI, Request

from custom_queue import send_message_to_queue

app = FastAPI()

SERVER_NAME = environ.get('NAME')


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/solve/", response_model=str)
def solve_sudoku(sudoku: str):
    send_message_to_queue(sudoku)
    #todo дождаться получение решения и вернуть результат
    return 'result'


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-State-Name"] = SERVER_NAME
    return response
