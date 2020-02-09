from PIL import Image
import pytesseract

# pytesseract is a wrapper, tesseract must be in system path
# codebase : https://github.com/madmaze/pytesseract
# brew install tesseract - if not already done

# image_to_string() method accepts image type and returns equivalent text
# We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
text = pytesseract.image_to_string(Image.open("english-text.png"), lang='eng')
print(text)

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# Supported Format : 'JPEG', 'PNG', 'PBM', 'PGM', 'PPM', 'TIFF', 'BMP', 'GIF'
print(pytesseract.image_to_string('english-text.png'))

# Get bounding box estimates - NSEW coordinates of the each character in the image
print(pytesseract.image_to_boxes(Image.open('english-text.png')))

# Get verbose data including boxes, confidences, line and page numbers
# level, page_num, block_num, par_num, line_num	word_num, left, top, width, height, conf, text
print(pytesseract.image_to_data(Image.open('english-text.png')))

# Get information about orientation and script detection
# Page number, Orientation in degrees, Rotate, Orientation confidence, Script: Latin, Script confidence
print(pytesseract.image_to_osd(Image.open('english-text.png')))

# Get HOCR output - XML format
# hOCR is an open standard of data representation for formatted text obtained from optical character recognition (OCR).
hocr = pytesseract.image_to_pdf_or_hocr('english-text.png', extension='hocr')
print(hocr)

