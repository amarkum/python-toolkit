import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
image = cv2.imread("face.jpeg", 1)

# convert the image into grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# search the coordinates of the face in the image
# decreases the value by 5%, until the face is found
# lesser the value, greater the accuracy
faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.05, minNeighbors=5)

# print the data type of the faces i.e numpy.ndarray
print(type(faces))

# print the coordinates array
print(faces)

# draw a rectangle box around the face in the image
# where (0,255,0) is the RGB of the border
# 3 is the padding size
for x, y, w, h in faces:
    outline_image = cv2.rectangle(image, (x, y), (x + w, w + h), (0, 255, 0), 4)

# show the numpy converted matrix as image
cv2.imshow("outlined-face-image", outline_image)

# save the outlined image
cv2.imwrite("detected-face.jpg", outline_image)

# wait until user performs a click operation
cv2.waitKey(0)

# close all cv2 window
cv2.destroyAllWindows()
