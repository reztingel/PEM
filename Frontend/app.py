from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Backend./database.db'
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)


app = Flask(__name__)
CORS(app)

class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    
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
    
    def load_user(user_id):
        return User.query.get(user_id)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)


@app.route('/', methods = ["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == "POST":
        email = request.form['username']
        passord = request.form['passord']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.passord, passord):
            user.authenticated = True
            db.session.commit()
            login_user(user)
            return redirect(url_for('get_resturanger'))
        else:
            flash('feil brukernavn eller passord', 'error')

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    current_user.authenticated = False
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))




@app.route('/get_resturanger', methods = ["GET"])
def get_resturanger():
    resturanger = requests.get('http://127.0.0.1:5001/get_resturanger').json()
    return render_template("index.html", resturanger=resturanger)



@app.route('/get_resturang/<int:sid>', methods = ["GET"])
def get_resturang(sid):
    resturang_meny = requests.get('http://127.0.0.1:5001/get_resturang_meny', json={"sid": sid}).json()
    resturang = requests.get('http://127.0.0.1:5001/get_resturang', json={"sid": sid}).json()
    return render_template("resturang.html", resturang=resturang, meny=resturang_meny)







if __name__ =="__main__":
    app.run(debug=True, port=5000)
