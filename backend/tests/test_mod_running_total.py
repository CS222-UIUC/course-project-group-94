import sqlalchemy as db
from functions import mod_running_total
from functions import reset_running_total


def testAddingTo():
    engine = db.create_engine('mysql://root:Group94@localhost:3306/nutrify')
    connection = engine.connect()
    metadata = db.MetaData()
    nutritional_info = db.Table('Running Total on Daily Nutrition', metadata,
                                autoload=True, autoload_with=engine)
    retrieve = db.select([nutritional_info]).where(nutritional_info.columns.
                                                   Username == "andrew")
    retrieve = connection.execute(retrieve).fetchall()
    assert retrieve[0][0] == 0, "Incorrect initial calories"
    assert retrieve[0][1] == 0, "Incorrect initial fat"
    assert retrieve[0][2] == 0, "Incorrect initial carbs"
    assert retrieve[0][3] == 0, "Incorrect initial protein"
    assert retrieve[0][4] == 0, "Incorrect initial sugar"
    mod_running_total.modRunningTotal(100, 100, 203.4, 134.4, 50.2, "andrew",
                                      True)
    retrieve = db.select([nutritional_info]).where(nutritional_info.columns.
                                                   Username == "andrew")
    retrieve = connection.execute(retrieve).fetchall()
    assert retrieve[0][0] == 100, "Failed to add calories"
    assert retrieve[0][1] == 100, "Failed to add fat"
    assert retrieve[0][2] == 203.4, "Failed to add carbs"
    assert retrieve[0][3] == 134.4, "Failed to add protein"
    assert retrieve[0][4] == 50.2, "Failed to add sugar"
    mod_running_total.modRunningTotal(0, 0, 0, 13, 3, "andrew", True)
    retrieve = db.select([nutritional_info]).where(nutritional_info.columns.
                                                   Username == "andrew")
    retrieve = connection.execute(retrieve).fetchall()
    assert retrieve[0][0] == 100, "Failed to keep calories constant"
    assert retrieve[0][1] == 100, "Failed to keep fat constant"
    assert retrieve[0][2] == 203.4, "Failed to keep carbs constant"
    assert retrieve[0][3] == (134.4 + 13), "Failed to add protein to "\
                                           "existing value"
    assert retrieve[0][4] == (50.2 + 3), "Failed to add sugar to "\
                                         "existing value"
    reset_running_total.resetRunningTotal()
    assert retrieve[0][0] == 0, "Failed to reset calories"
    assert retrieve[0][1] == 0, "Failed to reset fat"
    assert retrieve[0][2] == 0, "Failed to reset carbs"
    assert retrieve[0][3] == 0, "Failed to reset protein"
    assert retrieve[0][4] == 0, "Failed to reset sugar"


def testSubtractingTo():
    engine = db.create_engine('mysql://root:Group94@localhost:3306/nutrify')
    connection = engine.connect()
    metadata = db.MetaData()
    nutritional_info = db.Table('Running Total on Daily Nutrition', metadata,
                                autoload=True, autoload_with=engine)
    retrieve = db.select([nutritional_info]).where(nutritional_info.columns.
                                                   Username == "andrew")
    retrieve = connection.execute(retrieve).fetchall()
    mod_running_total.modRunningTotal(1, 1, 1, 1, 1, "andrew", False)
    assert retrieve[0][0] == 0, "Incorrect initial calories"
    assert retrieve[0][1] == 0, "Incorrect initial fat"
    assert retrieve[0][2] == 0, "Incorrect initial carbs"
    assert retrieve[0][3] == 0, "Incorrect initial protein"
    assert retrieve[0][4] == 0, "Incorrect initial sugar"
    mod_running_total.modRunningTotal(100, 100, 203.4, 134.4, 50.2, "andrew",
                                      True)
    mod_running_total.modRunningTotal(50, 50, 3.4, 34, 25, "andrew", False)
    assert retrieve[0][0] == (100 - 50), "Failed to subtract calories"
    assert retrieve[0][1] == (100 - 50), "Failed to subtract fat"
    assert retrieve[0][2] == (203.4 - 3.4), "Failed to subtract carbs"
    assert retrieve[0][3] == (134.4 - 34), "Failed to subtract protein"
    assert retrieve[0][4] == (50.2 - 25), "Failed to subtract sugar"
    reset_running_total.resetRunningTotal()
    assert retrieve[0][0] == 0, "Failed to reset calories"
    assert retrieve[0][1] == 0, "Failed to reset fat"
    assert retrieve[0][2] == 0, "Failed to reset carbs"
    assert retrieve[0][3] == 0, "Failed to reset protein"
    assert retrieve[0][4] == 0, "Failed to reset sugar"
