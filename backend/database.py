import sqlalchemy as db

engine = db.create_engine('sqlite:///test.sqlite')
connection = engine.connect()
metadata = db.MetaData()

nutrional_info = db.Table('Nutritional Info', metadata,
                db.Column('Calories', db.Integer()),
                db.Column('Fat', db.Integer()),
                db.Column('Sodium', db.Float()),
                db.Column('Carbs', db.Integer()),
                db.Column('Sugar', db.Integer()),
                db.Column('Protein', db.Integer()),
                db.Column('Calcium', db.Float()),
                db.Column('Iron', db.Float()),
                db.Column('Potassium', db.Float()))

metadata.create_all(engine) 