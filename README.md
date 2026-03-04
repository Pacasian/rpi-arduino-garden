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
uvicorn src.api:app --reload --port 8000     
```

## To find the usb port the arduino is having 
```bash
ls /dev/tty.usb*   
```
## To open the websocket in the Postman
Follow the options in the Postman: ## New -> WebSocket -> Paste the following link
```bash
ws://localhost:8000/ws/latest
```
