from app import db


class Planet(db.Model):
    #inheriting from sqlalchemy to be able to create these columns in our database
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)