# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract

'''
Function to convert an image of a specified name to a string ("example.jpg").
The string will be stored in a list so that it can be later modified by users
as they wish and accessed by the function to read data from the string.

Parameters: imgName -> string (Name of image file)
            dataList -> list (List of string data from image)
Returns: imgString -> string (converted string from image)
'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract'

def convertImageToString(imgName, dataList):
    imgString = pytesseract.image_to_string(Image.open(imgName))
    dataList.append(imgString)
    return imgString
