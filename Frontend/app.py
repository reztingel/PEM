from flask import Flask, render_template, request, redirect
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/', methods = ["GET"])
def index():
    return redirect('/get_resturanger')

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
