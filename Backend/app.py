from flask import Flask, render_template, redirect, url_for
import sqlite3


app = Flask(__name__)


con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


@app.route("/")
def index():
    return render_template("")



if __name__ == "__main__":
    app.run(debug=True)