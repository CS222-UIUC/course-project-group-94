from functions import image_to_string
from functions import check_for_bad_ingredients


def testCheckOnStrings():
    none = "absodhns asohnf asej tranfat ssf"
    transfat = "the trans fats"
    highfructose = "high fructose corn syrup"
    artificialsweet = "this product contains sucralose"
    assert not check_for_bad_ingredients.checkForBad(none)[0], \
        "False positive"
    assert check_for_bad_ingredients.checkForBad(none)[1] == "none", \
        "Incorrect label"
    assert check_for_bad_ingredients.checkForBad(transfat)[0], "False "\
                                                               "negative"
    assert check_for_bad_ingredients.checkForBad(transfat)[1] == "transfat", \
        "Incorrect label"
    assert check_for_bad_ingredients.checkForBad(highfructose)[0], "False "\
                                                                   "negative"
    assert check_for_bad_ingredients.checkForBad(highfructose)[1] == "hfcs", \
        "Incorrect label"
    assert check_for_bad_ingredients.checkForBad(artificialsweet)[0], \
        "False negative"
    assert check_for_bad_ingredients.checkForBad(artificialsweet)[1] == \
           "artsweet", "Incorrect label"


def testCheckOnAnImage():
    imageName = "tests/resources/Label.jpg"
    imgString = image_to_string.convertImageToString(imageName)
    warnResult = check_for_bad_ingredients.checkForBad(imgString)
    assert warnResult[0], "Image was not parsed correctly"
    assert warnResult[1] == "transfat", "Incorrect identificaztion in warning"
