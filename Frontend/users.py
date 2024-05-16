from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()   

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    passord = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_acitve(self):
        return True
    def get_id(self):
        return self.email
    def is_authenticated(self):
        return self.authenticated
    def is_annonymous(self):
        return False