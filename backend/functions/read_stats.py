'''
Function to retrieve numeric values on label from the converted string.
Parameters: convertedImg -> string (converted image)
Returns: tuple -> calories, fat, carbohydrates, and sugar in grams
'''


def getFromImage(convertedImg):
    checkString = convertedImg.lower()
    checkString = checkString.replace(" ", "")
    calIndex = checkString.index("calories") + 8
    calories = ""
    while checkString[calIndex].isnumeric():
        calories += checkString[calIndex]
        calIndex += 1
    fatIndex = checkString.index("totalfat") + 8
    fat = ""
    while checkString[fatIndex].isnumeric():
        fat += checkString[fatIndex]
        fatIndex += 1
    carbIndex = checkString.index("totalcarbohydrate") + \
                len("totalcarbohydrate")
    carb = ""
    while checkString[carbIndex].isnumeric():
        carb += checkString[carbIndex]
        carbIndex += 1
    sugarIndex = checkString.index("totalsugars") + len("totalsugars")
    sugar = ""
    while checkString[sugarIndex].isnumeric():
        sugar += checkString[sugarIndex]
        sugarIndex += 1
    return (int(calories), int(fat), int(carb), int(sugar))
