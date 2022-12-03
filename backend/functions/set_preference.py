import sqlalchemy as db
import diet_preference_reader


def set_preference(calories, sugarDiet, biologicalSex, protein, carbs,
                   sodium, iron, username):
    calories, sugLow, sugUpp, fatLow, fatUpp, protein, carbs = \
        diet_preference_reader.dietPreferenceReader(calories, sugarDiet,
                                                    biologicalSex,
                                                    protein, carbs)
    engine = db.create_engine('mysql://root:Group94@localhost:3306/nutrify')
    connection = engine.connect()
    metadata = db.MetaData()
    # user_preferences = db.Table('User Preferences', metadata, autoload=True,
    #                             autoload_with=engine)
    nutritional_info = db.Table('Running Total on Daily Nutrition', metadata,
                                autoload=True, autoload_with=engine)
    calUp = db.update(nutritional_info).values(Calories=calories)
    fatUp = db.update(nutritional_info).values(Fat=fatUpp)
    carbUp = db.update(nutritional_info).values(Carbs=carbs)
    protUp = db.update(nutritional_info).values(Protein=protein)
    sugUp = db.update(nutritional_info).values(Sugar=sugUpp)
    sodUp = db.update(nutritional_info).values(Sodium=sodium)
    ironUp = db.update(nutritional_info).values(Iron=iron)
    connection.execute(calUp)
    connection.execute(fatUp)
    connection.execute(carbUp)
    connection.execute(protUp)
    connection.execute(sugUp)
    connection.execute(sodUp)
    connection.execute(ironUp)
