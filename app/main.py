# app/main.py
from fastapi import FastAPI
from .user import app as user_app

app = FastAPI()
app.mount("/user", user_app)
