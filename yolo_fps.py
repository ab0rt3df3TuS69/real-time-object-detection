import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

prev_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.putText(
        annotated,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO + FPS", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()