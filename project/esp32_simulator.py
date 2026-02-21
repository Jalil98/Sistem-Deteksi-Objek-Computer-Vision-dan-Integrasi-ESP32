import time

print("ESP32 Simulator started")

while True:
    command = input()

    if command == "DETECTED":
        print("ESP32: Sensor OK")

    time.sleep(0.1)