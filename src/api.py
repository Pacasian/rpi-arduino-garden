# WE ARE USING THE FASTAPI SERVICE
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from src.arduino_client import test_readings
from src.serial_reader import read_latest_from_arduino
import asyncio
from typing import Set

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

# --- Live state + websocket clients ---
_latest =None
_latest_lock= asyncio.Lock()
_clients:Set[WebSocket] = set()



@app.get("/health")
def health():
    return {
        "status":"OK"
    }

@app.post("/test")
def test():
    return test_readings()

@app.get("/latest")
async def latest():
    async with _latest_lock:
        return _latest or test_readings()

async def _broadcast(payload: dict):
    dead = []
    msg = json.dumps(payload)
    for ws in list(_clients):
        try:
            await ws.send_text(msg)
        except Exception:
            dead.append(ws)
    for ws in dead:
        _clients.discard(ws)

async def _sensor_loop():
    global _latest
    last_ts = None
    while True:
        reading = test_readings()
        ts= reading.get("timestamp")

        async with _latest_lock:
            _latest= reading

        if ts != last_ts:
            last_ts = ts
            await _broadcast(reading)
        await asyncio.sleep(1)

async def _sensor_loop():
    global _latest
    last_ts = None

    # TODO: change this to your actual port
    # macOS examples: /dev/tty.usbmodem14101 or /dev/tty.usbserial-xxxx
    arduino_port = "/dev/tty.usbmodem11201"

    for reading in read_latest_from_arduino(arduino_port, baud=9600):
        ts = reading.get("timestamp")

        async with _latest_lock:
            _latest = reading

        if ts != last_ts:
            last_ts = ts
            await _broadcast(reading)

        # yield to event loop
        await asyncio.sleep(0)

@app.on_event("startup")
async def startup():
    asyncio.create_task(_sensor_loop())

@app.websocket("/ws/latest")
async def ws_latest(websocket: WebSocket):
    await websocket.accept()
    _clients.add(websocket)

    async with _latest_lock:
        await websocket.send_text(json.dumps(test_readings()))

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        _clients.discard(websocket)
