import string
import random

from fastapi import FastAPI, APIRouter, status

router = APIRouter(tags=["View"])

@router.get("/ping/")
def hello():
    return {"message": "pong"}

@router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
)
def generate_password(password_len: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_len))
    return {f"You password: {password}"}
