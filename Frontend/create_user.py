#!/usr/bin/env python
"""Create a new admin user."""
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from app import app
from  users import db, User  # Import your Flask application and User model

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db') 
bcrypt = Bcrypt(app)
db.init_app(app)


def create_admin_user():
    """Create a new admin user."""
    with app.app_context():
        db.create_all()

        # Check if any user exists in the database
        if User.query.count() > 0:
            print("Admin user already exists.")
            return

        # Prompt for admin user details
        email = input("Enter email address: ")
        password = input("Enter password: ")
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create and add the admin user to the database
        admin_user = User(email=email, password = hashed_password)
        admin_user.set_password(password=hashed_password)
        db.session.add(admin_user)
        db.session.commit()

        print("Admin user created successfully.")


if __name__ == '__main__':
    create_admin_user()
