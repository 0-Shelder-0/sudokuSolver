from datetime import datetime
from os import environ

from fastapi import FastAPI, Request, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
from converter import convert_to_text, convert_to_matrix, STRING_EMPTY_VALUE
from custom_queue import send_message_to_queue
from database import engine, get_db
from schemas.solution import SolutionCreate, SolutionUpdate, SolutionIdResponse, SolutionResponse
from schemas.solution_status import SolutionStatusInDb, SolutionStatusCreate
from schemas.status import Status

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

SERVER_NAME = environ.get('NAME')
API_TOKEN = environ.get("API_TOKEN")


@app.get("/")
async def index():
    # todo return page
    return {"message": "Hello World"}


@app.get("/status/{solution_id}", response_model=SolutionStatusInDb)
def get_current_status(solution_id: int, db: Session = Depends(get_db)):
    last_status = crud.get_last_status(db, solution_id=solution_id)
    if last_status is None:
        raise HTTPException(status_code=404, detail="Solution not found")

    return last_status


@app.post("/status/", response_model=SolutionStatusInDb)
def create_status(solution_status: SolutionStatusCreate, request: Request, db: Session = Depends(get_db)):
    api_token = request.headers.get('Api-token')
    if api_token != API_TOKEN:
        raise HTTPException(status_code=403)

    db_status = crud.create_solution_status(db, solution_status=solution_status)
    return db_status


@app.get("/solutions/{solution_id}", response_model=SolutionResponse)
def get_solution(solution_id: int, db: Session = Depends(get_db)):
    db_solution = crud.get_solution_by_id(db, solution_id=solution_id)
    if db_solution is None:
        raise HTTPException(status_code=404, detail="Solution not found")

    solution_matrix = convert_to_matrix(db_solution.solution)
    response = SolutionResponse(solution_id=solution_id, solution=solution_matrix)
    return response


@app.post("/solutions/", response_model=SolutionIdResponse)
def create_solution(solution_create: SolutionCreate, db: Session = Depends(get_db)):
    solution_text = convert_to_text(solution_create.solution)

    db_solution = crud.get_solution_by_text(db, solution=solution_text)
    if db_solution is not None:
        db_status = crud.get_last_status(db, solution_id=db_solution.id)
        if db_status is not None and Status.CREATED.value <= db_status.status <= Status.SOLVED.value:
            response = SolutionIdResponse(solution_id=db_solution.id)
            return response

    if db_solution is None:
        db_solution = crud.create_solution(db, solution_text=solution_text)

    create_model = SolutionStatusCreate(solution_id=db_solution.id,
                                        status=Status.CREATED.value,
                                        created_at=datetime.now())
    crud.create_solution_status(db, solution_status=create_model)

    send_message_to_queue(solution_id=db_solution.id, solution=solution_create.solution)
    response = SolutionIdResponse(solution_id=db_solution.id)
    return response


@app.put("/solutions/{solution_id}", response_model=SolutionIdResponse)
def update_solution(solution_id: int, solution_update: SolutionUpdate, request: Request, db: Session = Depends(get_db)):
    api_token = request.headers.get('Api-token')
    if api_token != API_TOKEN:
        raise HTTPException(status_code=403)

    solution_text = convert_to_text(solution_update.solution)
    crud.update_solution(db, solution_id=solution_id, solution_text=solution_text)

    if solution_text.__contains__(STRING_EMPTY_VALUE):
        status = Status.ERROR.value
    else:
        status = Status.SOLVED.value

    create_model = SolutionStatusCreate(solution_id=solution_id,
                                        status=status,
                                        created_at=datetime.now())
    crud.create_solution_status(db, solution_status=create_model)

    response = SolutionIdResponse(solution_id=solution_id)
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-State-Name"] = SERVER_NAME
    return response
