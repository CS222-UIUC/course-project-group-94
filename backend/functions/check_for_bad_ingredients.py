'''
Function to check if there are any ingredients which the user should avoid at
all costs. This contains specifically trans fats, high-fructose corn syrup,
and artificial sweeteners.

Parameters:
    convertedImg -> string (The string resulting from image conversion)
Returns:
    tuple (a bool indicating whether a warning should be thrown followed by a
            string indicating which check threw the warning)
'''


def checkForBad(convertedImg):
    checkString = convertedImg.lower()
    checkString = checkString.replace(" ", "")
    transChecker = ["transfat", "hydrogenated"]
    for trans in transChecker:
        if trans in checkString:
            return (True, "transfat")
    hfcsChecker = ["highfructosecornsyrup", "high-fructosecornsyrup"]
    for hfcs in hfcsChecker:
        if hfcs in checkString:
            return (True, "hfcs")
    artificialChecker = ["aspartame", "sucralose", "saccharin"]
    for artSwe in artificialChecker:
        if artSwe in checkString:
            return (True, "artsweet")
    return (False, "none")
