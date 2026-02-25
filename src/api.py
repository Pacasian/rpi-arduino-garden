# WE ARE USING THE FASTAPI SERVICE

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.arduino_client import test_readings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

@app.get("/health")
def health():
    return {
        "status":"OK"
    }

@app.post("/test")
def test():
    return test_readings()
