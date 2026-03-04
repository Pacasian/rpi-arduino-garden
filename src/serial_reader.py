import json
import time
from datetime import datetime

import serial
from serial.serialutil import SerialException

def read_latest_from_arduino(port: str, baud: int = 9600, timeout: float = 2.0):
    """
    Blocking generator: yields dict readings parsed from Arduino JSON lines.
    Adds timestamp on the server side.
    """
    while True:
        try:
            with serial.Serial(port, baudrate=baud, timeout=timeout) as ser:
                # Give Arduino time to reset after opening serial
                time.sleep(2)

                while True:
                    raw = ser.readline().decode("utf-8", errors="ignore").strip()
                    if not raw:
                        continue

                    try:
                        data = json.loads(raw)
                        # add timestamp consistently from server
                        data["timestamp"] = datetime.now().isoformat(timespec="seconds")
                        yield data
                    except json.JSONDecodeError:
                        # Ignore junk lines
                        continue

        except SerialException:
            # Arduino unplugged / wrong port: retry
            time.sleep(1)
            continue