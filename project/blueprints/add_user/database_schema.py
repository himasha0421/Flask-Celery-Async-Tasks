from .extensions import db

#define the db schema
class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50))