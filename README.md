# RPi + Arduino Garden Logger (v1)

Version 1: Raspberry Pi script reads sensor data from Arduino (Serial) and writes to Excel/CSV.

## Features (v1)
- Read data over Serial (USB)
- Log timestamp + sensor values
- Save to file

## Setup
```bash
pip install -r requirements.txt
```

## To Run the uvicorn server
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```

