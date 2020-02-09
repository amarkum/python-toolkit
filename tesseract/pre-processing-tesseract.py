import cv2

# reads the image in RGB channel
image = cv2.imread("english-text.png", 1)

# 1. SCALING

# The images that are rescaled are either shrunk or enlarged.
# If you’re interested in shrinking your image, INTER_AREA is the way to go for you.
# (Btw, the parameters fx and fy denote the scaling factor in the function below.)
# scales the image to 0.5
scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# save the scaled image
cv2.imwrite("english-text-scaled.png", scaled_image)

# in most cases, you may need to scale your image to a larger size to recognize small characters.
# In this case, INTER_CUBIC generally performs better than other alternatives, though it’s also slower than others.
enlarged_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# save the enlarged image
cv2.imwrite("english-text-enlarged.png", enlarged_image)

# If you’d like to trade off some of your image quality for faster performance,
# you may want to try INTER_LINEAR for enlarging images.
linear_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# save the linear image
cv2.imwrite("english-text-linear.png", linear_image)

# 2. BLURRING
# Image blurring is usually achieved by convolving the image with a low-pass filter kernel.

average_image = cv2.blur(image, (5, 5))
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)
median_image = cv2.medianBlur(image, 3)

# 3. THRESHOLD
# pick a threshold value, say 127.
# If the pixel value is greater than the threshold, it becomes black.
# If less, it becomes white.

threshold_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# save the threshold image
cv2.imwrite("english-text-threshold.png", average_image)

# close all cv2 window
cv2.destroyAllWindows()
