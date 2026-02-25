import json
import time
import random
from datetime import datetime

# For RPi port initialization
SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 9600

SIMULATION_MODE = True

def _fake_readings():
    moisture=random.randint(30,60)
    humidity=random.randint(35,70)
    temperature=round(random.uniform(20,50),1)
    pump_status="ON" if humidity<40 else "OFF"

    return{
        "timestamp":datetime.now().isoformat(timespec="seconds"),
        "moisture":moisture,
        "humidity":humidity,
        "temperature":temperature,
        "pump_status":pump_status
    }

def test_readings():
    if SIMULATION_MODE:
        return _fake_readings()
    else:
        print("Testing readings for RPI needs to be implemented...")
        return {
            "timestamp": "",
            "moisture": "",
            "humidity": "",
            "temperature": "",
            "pump_status": ""
        }
