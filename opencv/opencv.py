import matplotlib.pyplot as plt
import numpy as np

import cv2

# reads the image as RGB channel,  by setting flag as 1
face_image_rgb = cv2.imread("face.jpeg", 1)

# reads the image as grayscale channel,  by setting flag as 0
face_image_grayscale = cv2.imread("face.jpeg", 1)

# prints the image data matrix as numpy
print(face_image_rgb)

cv2.imshow("colorful", face_image_rgb)

np.random.seed(19680801)
data = np.random.randn(2, 100)






fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()



