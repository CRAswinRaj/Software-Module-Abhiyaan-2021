import cv2

# Reads the image
img = cv2.imread('Resources/abhiyaan_opencv_qn1.png')
# Reads the sample image, which is used to generate histogram
sample_img = cv2.imread('Resources/sample.png')

# Convert the images to hsv type
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
sample_hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)

# Create histogram of hue and saturation of the sample image 
sample_hist = cv2.calcHist([sample_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# Create mask using backprojection of histogram
mask = cv2.calcBackProject([img_hsv], [0, 1], sample_hist, [0, 180, 0, 256], 1)

# Pixels above a threshold of 150 is converted to white and the rest to black
_, thresh = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY)
# Dilating the image
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
thresh = cv2.dilate(thresh, kernal, iterations=4)

# Create contours around the white regions in the threshold image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Rectangle is drawn around the contours if the area of the contour is more than 200 
# This is to avoid drawing rectangle around noises
for contour in contours:
    if cv2.contourArea(contour) > 200:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

# Showing the image
cv2.imshow('Final Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
