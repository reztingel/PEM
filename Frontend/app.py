from flask import Flask, render_template, request, redirect
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


response = requests.get('http://127.0.0.1:5010/get_resturanger')

# Log the response content for debugging
print("Response content:", response.text)

# Attempt to decode the response as JSON
try:
    resturanger = response.json()
    print("JSON decoded successfully:", resturanger)
except requests.exceptions.JSONDecodeError as e:
    print("JSON decode error:", e)


@app.route('/', methods = ["GET"])
def index():
    resturanger = requests.get('http://127.0.0.1:5010/get_resturanger').json()
    return render_template("index.html", resturanger=resturanger)

@app.route('/get_resturang/<sid>', methods = ["GET"])
def get_resturang(sid):
    resturang_meny = requests.get('http://127.0.0.1:5010/get_resturang_meny', json={"sid": sid}).json()
    resturang = requests.get('http://127.0.0.1:5010/get_resturang', json={"sid": sid}).json()
    return render_template("resturang.html", resturang=resturang, meny=resturang_meny)






if __name__ =="__main__":
    app.run(debug=True, port=5000)
