import sqlalchemy as db
from sqlalchemy.sql import select

#currently connecting to my local mySQL database (username: root, password: Group94)
engine = db.create_engine('mysql://root:Group94@localhost:3306/Nutrify')
connection = engine.connect()
metadata = db.MetaData()

# Working on gathering data from the database and 
# comparing it to the diet preferences that the user inputted to see if it goes over
nutritional_info.query(data).filter(data.nutritional_info.in_([user_preferences]))
s = select([user_preferences])
result = connection.execute(s)
warning = False
if result:
    warning = True

