import cv2

video = cv2.VideoCapture('Resources/pedestrians.mp4')

# Reading first frame
_, frame2 = video.read()

while video.isOpened():
    frame1 = frame2
    # New frame is read to compare with old frame
    _, frame2 = video.read()

    # The difference between both images is found, then it is blurred
    # and is converted into gray scale 
    diff = cv2.absdiff(frame1, frame2)
    diff = cv2.GaussianBlur(diff, (5, 5), 0)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Pixels having value beyond 30 is converted to white and the rest to black
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    # MORPH_OPEN helps to remove small noises in the image
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, None)
    # Dilate helps to dilate the image
    thresh = cv2.dilate(thresh, None, iterations=5)

    # Create external boundary for the white parts in the thresh
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Checking if the area of the contour is big enough
        # Small contour area may be because of noises
        # Rectangle is then drawn around each contour
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 1)

    # Show the frame
    cv2.imshow('video', frame1)

    # Wait for 100 milliseconds for pressing 'Esc' key (27 is the ASCII value of 'Esc')
    if cv2.waitKey(100) == 27:
        break

# Destroy the window and close the video file
cv2.destroyAllWindows()
video.release()
