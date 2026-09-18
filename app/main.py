from fastapi import FastAPI
from pydantic import BaseModel

from app.service import create_task, get_tasks

app = FastAPI(title="Agent Lab API")


class TaskCreate(BaseModel):
    title: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return get_tasks()


@app.post("/tasks")
def add_task(payload: TaskCreate):
    return create_task(payload.title)