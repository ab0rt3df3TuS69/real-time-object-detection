### FPS Analysis

To evaluate the real-time performance of the system, FPS was measured while running YOLOv8n on live webcam input.

The system maintained an average FPS of around 15 during testing. Different camera resolutions were tested, but the FPS remained largely unchanged. To understand this behavior, the webcam frame rate and model inference time were examined separately.

The webcam was found to be operating at approximately 15 FPS, while YOLOv8n required only about 22-26 ms for inference. This indicated that the model was capable of processing frames faster than they were being captured.

Therefore, the overall system performance was limited mainly by the webcam frame rate and not by the object detection model. The results also confirmed that the system was able to perform object detection reliably in real time.
