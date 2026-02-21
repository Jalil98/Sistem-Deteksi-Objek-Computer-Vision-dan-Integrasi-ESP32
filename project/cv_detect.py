import cv2
from ultralytics import YOLO
import subprocess

model = YOLO("model/best.pt")

cap = cv2.VideoCapture(0)

esp32 = subprocess.Popen(
    ["python", "esp32_simulator.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

print("System started")

while True:

    ret, frame = cap.read()

    results = model(frame)

    annotated = results[0].plot()

    if len(results[0].boxes) > 0:

        print("Object detected")

        esp32.stdin.write("DETECTED\n")
        esp32.stdin.flush()

        response = esp32.stdout.readline().strip()

        print("ESP32 Response:", response)

    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()