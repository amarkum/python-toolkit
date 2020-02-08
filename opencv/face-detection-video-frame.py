import cv2

# get the video object from Video Capture Unit.
# 0 denotes the front camera.
video = cv2.VideoCapture(0)

# video.read() returns two variable in the array
# check - boolean, if it's able to read the video object
# frame - the frame of the image as numpy array
check, frame = video.read()

# prints the frame
print(frame)

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# search the coordinates of the face in the image
faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

# put up a coordinate rectangle on the detected face
for x, y, w, h in faces:
    camera_face_detected_image = cv2.rectangle(frame, (x, y), (x + w, w + h), (0, 255, 0), 3)

# show the frame image
cv2.imshow("camera_face_detected_image", camera_face_detected_image)

# save the camera detected face image
cv2.imwrite("camera-detected-face.jpg", camera_face_detected_image)

# close the window unless some key is pressed.
cv2.waitKey(0)

video.release()
