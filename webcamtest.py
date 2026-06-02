import cv2

cap = cv2.VideoCapture(0)
# if u want to js capture a single frame
ret,frame = cap.read()
#if ret:
'''cv2.imshow("Single Frame", frame)
cv2.waitKey(0)  # Wait indefinitely for a key press
#else:
    #print("Failed to capture frame")
'''


'''while True:
    ret, frame = cap.read()
    print (frame.shape)

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("webcam",frame)
    #cv2.imshow("Gray", cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) : used for greyscaling

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        '''


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blur, 100, 200)

    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()