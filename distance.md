### Lighting and Distance Analysis

The performance of the YOLOv8n model was evaluated under different lighting conditions and object distances.

In a normally lit environment, the model was able to detect a person reliably at greater distances. However, in a dimly lit room, detection performance decreased noticeably. During testing, the model stopped consistently detecting the person class at a distance of approximately 2.8 m.

This behavior can be attributed to reduced image quality under poor lighting conditions. Lower illumination decreases the visibility of object features, making it more difficult for the model to identify and classify objects accurately.

The results indicate that lighting conditions have a significant impact on object detection performance, particularly when the object is located farther from the camera.
