import cv2

# reads the image as RGB channel, by setting flag as 1
face_image_rgb = cv2.imread("face.jpeg", 1)

# reads the image as grayscale channel, by setting flag as 0
face_image_grayscale = cv2.imread("face.jpeg", 0)

# prints the image data matrix as numpy
print(face_image_rgb)

# show the numpy converted matrix as image
cv2.imshow("colorful", face_image_grayscale)

# wait until user performs a click operation
cv2.waitKey(0)

# close all cv2 window
cv2.destroyAllWindows()





