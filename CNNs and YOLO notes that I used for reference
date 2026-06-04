# Computer Vision Internship Notes: CNNs and YOLO

## 1. Big Picture

The goal of computer vision is to enable a computer to understand visual information from images or videos.

Typical pipeline:

Camera → Frame Acquisition → Preprocessing → CNN Feature Extraction → YOLO Detection → Bounding Boxes → Performance Analysis

In this project, a webcam acts as the visual sensor and YOLO performs object detection on captured frames.

---

# 2. What is an Image?

Computers do not see images the way humans do.

An image is simply a matrix of numbers.

Example:

frame.shape = (480, 640, 3)

where:

* 480 = image height
* 640 = image width
* 3 = color channels

OpenCV stores colors in:

BGR (Blue, Green, Red)

A single pixel:

frame[100][200]

might return:

[34, 120, 255]

meaning:

* Blue = 34
* Green = 120
* Red = 255

Computer vision is fundamentally the processing of these numbers.

---

# 3. What is Preprocessing?

Preprocessing means modifying the image before feeding it to the model.

Purpose:

* Reduce noise
* Improve quality
* Increase speed
* Improve detection

Common techniques:

## Grayscale

Converts:

(Height, Width, 3)

into:

(Height, Width)

Advantages:

* Less memory
* Faster processing
* Simpler image representation

---

## Resizing

Example:

1920×1080

↓

640×480

Advantages:

* Fewer pixels
* Faster inference
* Higher FPS

---

## Gaussian Blur

Purpose:

* Reduce image noise
* Smooth image

Useful when images contain random disturbances.

---

## Edge Detection

Purpose:

* Identify object boundaries
* Highlight shape information

Common method:

Canny Edge Detection

---

# 4. What is Machine Learning?

Traditional Programming:

Rules + Data → Answer

Machine Learning:

Data + Answers → Rules

Instead of writing rules manually, the computer learns patterns from examples.

---

# 5. What is a Neural Network?

A neural network is a mathematical model that learns patterns from data.

Structure:

Input Layer
↓
Hidden Layers
↓
Output Layer

Example:

Image
↓
Neural Network
↓
Bottle

---

# 6. What are Weights?

Weights represent learned knowledge.

Initially:

Random values

During training:

Weights are adjusted repeatedly.

After training:

Weights contain useful information about patterns in data.

The entire knowledge of a trained neural network is stored in its weights.

---

# 7. Why Regular Neural Networks Are Bad for Images

Images contain huge amounts of information.

Example:

640 × 480 × 3

=

921,600 values

A fully connected neural network becomes extremely inefficient.

Solution:

Convolutional Neural Networks (CNNs)

---

# 8. What is a CNN?

CNN = Convolutional Neural Network

A CNN is a neural network designed specifically for image data.

Instead of looking at the entire image at once, it analyzes small regions.

Advantages:

* Fewer parameters
* Better feature extraction
* Faster computation
* Excellent performance on images

---

# 9. What is Convolution?

A convolution uses a small filter called a kernel.

Example:

3×3 kernel

The kernel slides across the image and extracts useful information.

The CNN automatically learns useful filters during training.

---

# 10. What Features Does a CNN Learn?

CNNs learn features hierarchically.

Early Layers:

* Edges
* Lines
* Corners

Middle Layers:

* Curves
* Shapes
* Textures

Deep Layers:

* Object parts
* Complete objects

Process:

Pixels
↓
Edges
↓
Shapes
↓
Parts
↓
Objects

This hierarchy is one of the most important concepts in computer vision.

---

# 11. What are Feature Maps?

After convolution, the network produces feature maps.

Feature maps indicate where specific features occur in an image.

Example:

One feature map may highlight vertical edges.

Another may highlight curves.

Another may highlight corners.

YOLO performs detection using these extracted features.

---

# 12. What is Pooling?

Pooling reduces the size of feature maps.

Common method:

Max Pooling

Purpose:

* Reduce computation
* Retain important information
* Improve efficiency

Example:

Large feature map
↓
Smaller feature map

---

# 13. Training vs Inference

Training:

The model learns.

Uses:

* Images
* Labels
* Loss functions
* Weight updates

Inference:

The model makes predictions using learned knowledge.

In this internship:

We are performing inference, not training.

Example:

results = model(frame)

This is inference.

---

# 14. What is YOLO?

YOLO stands for:

You Only Look Once

It is a real-time object detection algorithm.

YOLO performs:

* Object localization
* Object classification

in a single forward pass.

---

# 15. Classification vs Detection

Classification:

Question:

What is in the image?

Answer:

Bottle

Detection:

Questions:

What is in the image?
Where is it located?

Answer:

Bottle at coordinates (x1, y1, x2, y2)

YOLO performs detection.

---

# 16. Why YOLO is Fast

Older methods:

* Generate regions
* Analyze each region separately

YOLO:

Image
↓
Single Neural Network
↓
All Predictions

One pass.

Hence:

Real-time performance.

---

# 17. YOLO Architecture (Simplified)

Input Image
↓
CNN Backbone
↓
Feature Extraction
↓
Detection Head
↓
Bounding Boxes
Class Labels
Confidence Scores

---

# 18. What Does YOLO Output?

For each detected object:

1. Class
2. Confidence Score
3. Bounding Box

Example:

Class = Bottle

Confidence = 0.93

Bounding Box:

x1 = 100
y1 = 50
x2 = 250
y2 = 400

Meaning:

The model is 93% confident there is a bottle within those coordinates.

---

# 19. What is a Bounding Box?

A rectangle surrounding an object.

Represented using coordinates:

(x1, y1)

Top-left corner

(x2, y2)

Bottom-right corner

---

# 20. What is Confidence?

Confidence indicates how certain YOLO is about a prediction.

Example:

0.95

means:

95% confidence

Higher confidence generally means a more reliable prediction.

---

# 21. What is FPS?

FPS = Frames Per Second

Formula:

FPS = 1 / Processing Time Per Frame

Higher FPS:

* Faster system
* Better real-time performance

Lower FPS:

* Slower response
* Reduced usability

---

# 22. Why Resolution Affects FPS

Higher Resolution:

More pixels
More computation
Lower FPS

Lower Resolution:

Fewer pixels
Less computation
Higher FPS

Tradeoff:

Speed vs Accuracy

---

# 23. Important Terms for the Internship

Frame:
Single image captured from a video stream.

Inference:
Running a trained model on data.

Bounding Box:
Rectangle around detected object.

Class:
Object category.

Confidence:
Model certainty.

Feature:
Pattern extracted from image.

CNN:
Neural network specialized for image processing.

YOLO:
Real-time object detection model.

FPS:
Frames processed per second.

Preprocessing:
Image enhancement before detection.

---

# Final Summary

Image
↓
Preprocessing
↓
CNN extracts features
↓
YOLO analyzes features
↓
Predicts classes
↓
Predicts bounding boxes
↓
Produces confidence scores
↓
Displays detections in real time

This is the complete conceptual pipeline behind a real-time object detection system using YOLO.
