from ftfy import warnings
import sqlalchemy as db
from sqlalchemy.sql import select
import numpy as np

#currently connecting to my local mySQL database (username: root, password: Group94)

# Working on gathering data from the database and 
# comparing it to the diet preferences that the user inputted to see if it goes over
def comparePreferences(calories, sugarDiet, biologicalSex, fat):
    engine = db.create_engine('mysql://root:Group94@localhost:3306/Nutrify')
    connection = engine.connect()
    metadata = db.MetaData()

    calories, sugarLowerRange, sugarUpperRange, lowerFat, upperFat = dietPreferenceReader(calories, sugarDiet, biologicalSex)
    nutritional_info = db.Table("Running Total on Daily Nutrition", metadata, autoload = True, autoload_with = engine)
    data = db.select([nutritional_info]).where(nutritional_info.columns.Username == username)
    data = connection.execute(data).fetchall()
    warning = True
    warningDict = {"Calories": warning, "Fat": warning, "Sugar": warning}
    if (data[0][0] <= calories):
        warningDict["Calories"] = True
    else:
        warningDict["Calories"] = False
    if (data[0][1] >= lowerFat) and (data[0][1] <= upperFat):
        warningDict["Fat"] = True
    else:
        warningDict["Fat"] = False
    if (data[0][4] >= sugarLowerRange) and (data[0][4] <= sugarUpperRange):
        warningDict["Sugar"] = True
    else:
        warningDict["Sugar"] = False

    return warningDict


