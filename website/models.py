from . import db 
from flask_login import UserMaxin
from sql_alchemy.sql import func

class User(db.Model, UserMaxin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Coumn(db.Date(timezone=True), default=func.now())
