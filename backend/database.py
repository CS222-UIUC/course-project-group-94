import sqlalchemy as db

#currently connecting to my local mySQL database (username: root, password: Group94)
engine = db.create_engine('mysql://root:Group94@localhost:3306/Nutrify')
connection = engine.connect()
metadata = db.MetaData()

#based on what a person uploads each day, all columns must be reset to 0 every 24 hours
nutrional_info = db.Table('Running Total on Daily Nutrition', metadata,
                db.Column('Calories', db.Integer()),
                db.Column('Fat', db.Integer()),
                db.Column('Carbs', db.Integer()),
                db.Column('Protein', db.Integer()),
                db.Column('Username', db.String(63), nullable = False))

#user info for logging in and tracking who's eating what
user_info = db.Table('User Info', metadata,
                db.Column('Username', db.String(63), nullable = False),
                db.Column('Password', db.String(63), nullable = False))
                #in the future this could have more functionality such as storing a profile picture

#stores whether user is on low, med, or high for each nutrition category
#table assumes that columns store a string that contains either "low", "medium", or "high"
user_preferences = db.Table('User Preferences', metadata,
                    db.Column('Calories', db.String(15), nullable = False),
                    db.Column('Fat', db.String(63), nullable = False),
                    db.Column('Carbs', db.String(63), nullable = False),
                    db.Column('Protein', db.String(63), nullable = False),
                    db.Column('Username', db.String(63), nullable = False))

metadata.create_all(engine)
