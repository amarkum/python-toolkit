# Python Tesseract

```text
Python-tesseract is an optical character recognition (OCR) tool for python. 
That is, it will recognize and "read" the text embedded in images.
Python-tesseract is a wrapper for Google's Tesseract-OCR Engine. 
It is also useful as a stand-alone invocation script to tesseract, as it can read all image types.
supported Pillow and Leptonica imaging libraries, includes jpeg, png, gif, bmp, tiff, and others.
If used as a script, Python-tesseract will print the recognized text instead of writing it to a file.
```

### Install Tesseract in the system
`brew install tesseract`

### Install python wrapper 
`pip install pytesseract`

### PSM Mode
```text
Page Segmentation Modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.
```

### OEM Mode

```text
OCR Engine Modes:
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.
```