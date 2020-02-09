import cv2
import pytesseract

# we can even read openCV numarray object of the image in tesseract
opencv_bgr_image = cv2.imread('english-text.png')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
rgb_image = cv2.cvtColor(opencv_bgr_image, cv2.COLOR_BGR2RGB)

# call the image_to_string() method of pytesseract to convert the rgb image to detect text
text = pytesseract.image_to_string(rgb_image)
print(text)

# If custom configuration like oem/psm is needed, use the config keyword.
# Refer : https://github.com/amarkum/python-toolkit/blob/master/tesseract/README.md
# Example of adding any additional options.
custom_oem_psm_config = r'--oem 3 --psm 6'

# use the custom oem and psm configuration
print(pytesseract.image_to_string(rgb_image, config=custom_oem_psm_config))
