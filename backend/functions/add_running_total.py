# -*- coding: utf-8 -*-
import sqlalchemy as db
import numpy as np

'''
Function to increment elements int he database based on inputted values and
the username of the user whose elements will be added.

Parameters:
    calories -> flaot (number of calories of food item)
    fat -> float (amount of fat in grams in food item)
    carbs -> float (amount of carbs in grams in food item)
    protein -> float (amount of protein in grams in food item)
    sugar -> float (amount of sugar in the food item)
    username -> string (username of user)
'''


def addRunningTotal(calories, fat, carbs, protein, sugar, username):
    engine = db.create_engine('mysql://root:Group94@localhost:3306/nutrify')
    connection = engine.connect()
    metadata = db.MetaData()
    nutritional_info = db.Table('Running Total on Daily Nutrition', metadata,
                                autoload=True, autoload_with=engine)
    retrieve = db.select([nutritional_info]).where(nutritional_info.columns.
                                                   Username == username)
    arr = np.zeros(5)
    arr[0] = retrieve[0][0] + calories  # add increments
    arr[1] = retrieve[1][0] + fat
    arr[2] = retrieve[2][0] + carbs
    arr[3] = retrieve[3][0] + protein
    arr[4] = retrieve[4][0] + sugar
    calUp = db.update([nutritional_info]).values(Calories=arr[0]).where(
        nutritional_info.columns.Username == username)
    fatUp = db.update([nutritional_info]).values(Fat=arr[1]).where(
        nutritional_info.columns.Username == username)
    carbUp = db.update([nutritional_info]).values(Carbs=arr[2]).where(
        nutritional_info.columns.Username == username)
    protUp = db.update([nutritional_info]).values(Protein=arr[3]).where(
        nutritional_info.columns.Username == username)
    sugUp = db.update([nutritional_info]).values(Sugar=arr[4]).where(
        nutritional_info.columns.Username == username)
    connection.execute(calUp)
    connection.execute(fatUp)
    connection.execute(carbUp)
    connection.execute(protUp)
    connection.execute(sugUp)
