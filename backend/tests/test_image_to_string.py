# -*- coding: utf-8 -*-
from functions import image_to_string


def testContentOfStrings():
    imageName = "tests/resources/eng_bw.png"
    firstString = image_to_string.convertImageToString(imageName)
    imageName = "tests/resources/Label.jpg"
    secondString = image_to_string.convertImageToString(imageName)
    assert firstString[0:14] == "Mild Splendour", "Incorrect reading of " \
        "example text"
    assert secondString[0:15] == "Nutrition Facts", "Incorrect reading of " \
        "example label"
    assert "Total Fat" in secondString, "Missing from Middle of Label"
    assert "Potassium" in secondString, "Missing from End of Label"
