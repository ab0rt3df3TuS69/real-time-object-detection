'''from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("test.jpg")

for box in results[0].boxes:

    class_id = int(box.cls[0])

    confidence = float(box.conf[0])

    class_name = model.names[class_id]

    print(f"Object: {class_name}")
    print(f"Confidence: {confidence:.2f}")
    print("-" * 20)'''
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("test.jpg")

for box in results[0].boxes:

    class_id = int(box.cls[0])

    confidence = float(box.conf[0])

    class_name = model.names[class_id]

    x1, y1, x2, y2 = box.xyxy[0]

    print(f"Object: {class_name}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Box: ({x1:.0f},{y1:.0f}) -> ({x2:.0f},{y2:.0f})")
    print("-" * 30)