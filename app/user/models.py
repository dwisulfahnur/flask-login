from app.core.db import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Integer())
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return  True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return 'User {}'.format(self.username)
