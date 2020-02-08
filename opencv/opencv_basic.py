import cv2

# reads the image as RGB channel, by setting flag as 1
face_image_rgb = cv2.imread("face.jpeg", 1)

# reads the image as grayscale channel, by setting flag as 0
face_image_grayscale = cv2.imread("face.jpeg", 0)

# resize image to custom height and weight 600px - 600px
resized_image = cv2.resize(face_image_rgb, (600, 600))

# print the height, weight, channel information
print(resized_image.shape)

# prints the width of the image
print(resized_image.shape[0])

# prints the height of the image
print(resized_image.shape[1])

# resize image to half 300px - 300px
resized_image_half = cv2.resize(resized_image, (int(resized_image.shape[0]/2), int(resized_image.shape[1]/2)))

# prints the image data matrix as numpy
print(face_image_rgb)

# show the numpy converted matrix as image
cv2.imshow("resized-face", resized_image_half)

# wait until user performs a click operation
cv2.waitKey(0)

# close all cv2 window
cv2.destroyAllWindows()
