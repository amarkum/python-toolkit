import cv2

# get the video object from Video Capture Unit.
# 0 denotes the front camera.
video = cv2.VideoCapture(0)

# count the number of frame
number_of_frames = 1

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # increment the number of frames
    number_of_frames = number_of_frames + 1

    # video.read() returns two variable in the array
    # check - boolean, if it's able to read the video object
    # frame - the frame of the image as numpy array
    check, frame = video.read()

    # print the frame
    # print(frame)

    # search the coordinates of the face in the image
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

    # put up a coordinate rectangle on the detected face
    for x, y, w, h in faces:
        camera_face_detected_image = cv2.rectangle(frame, (x, y), (x + w, w + h), (0, 255, 0), 3)

    # show the frame
    cv2.imshow("camera_face_detected_image", camera_face_detected_image)

    # change the image in every millisecond
    key = cv2.waitKey(1)

    # if q is pressed quit
    if key == ord('q'):
        break

# finally display the number of image being captured
print(number_of_frames)

video.release()

cv2.destroyAllWindows()
