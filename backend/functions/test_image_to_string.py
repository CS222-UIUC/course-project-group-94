# -*- coding: utf-8 -*-
import image_to_string


def testNumOfStrings():
    listOfStrings = []
    assert len(listOfStrings) == 0, "Incorrect initial size of list"
    imageName = "Label.jpg"
    image_to_string.convertImageToString(imageName, listOfStrings)
    assert len(listOfStrings) == 1, "Incorrect size of list after adding " \
        "one string"
    imageName = "OtherLabel.png"
    image_to_string.convertImageToString(imageName, listOfStrings)
    assert len(listOfStrings) == 2, "Incorrect size of list after adding " \
        "two strings"


def testContentOfStrings():
    newList = []
    imageName = "eng_bw.png"
    image_to_string.convertImageToString(imageName, newList)
    imageName = "Label.jpg"
    image_to_string.convertImageToString(imageName, newList)
    assert newList[0][0:14] == "Mild Splendour", "Incorrect reading of " \
        "example text"
    assert newList[1][0:15] == "Nutrition Facts", "Incorrect reading of " \
        "example label"
    assert "Total Fat" in newList[1], "Missing from Middle of Label"
    assert "Potassium" in newList[1], "Missing from End of Label"
    assert len(newList) == 2, "Incorrect size of list"
