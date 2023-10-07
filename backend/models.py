from fastapi import FastAPI
from pydantic import BaseModel


class Step(BaseModel):
    id: int
    text: str