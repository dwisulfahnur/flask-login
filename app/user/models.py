from app.core.db import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def __repr__(self):
        return '{}'.format(self.username)
