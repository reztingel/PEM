from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)


con = sqlite3.connect("./database.db", check_same_thread=False)
cur = con.cursor()



@app.route('/get_image/<image_name>', methods = ["GET"])
def get_image(image_name):
    return send_from_directory("C:\\Users\\Ton\OneDrive - Innlandet fylkeskommune\\Skrivebord\\Eksamenforbredning\\Backend\\static\\images", image_name)


@app.route('/get_resturanger', methods = ["GET"])
def get_resturanger():
    cur.execute("SELECT * FROM resturanger")
    content = cur.fetchall()
    result = []
    for resturant in content:
        result.append({"navn": resturant[1], "id": resturant[0]})
    return result


@app.route('/get_resturang', methods = ["GET"])
def get_resturang():
    sid = request.get_json()["sid"]
    cur.execute("SELECT * FROM resturanger WHERE id = ?", (sid,))
    content = cur.fetchone()
    result = [content[0], content[1]]
    return result



@app.route('/get_resturang_meny', methods = ["GET"])
def resturang_meny():
    sid = request.get_json()["sid"]
    cur.execute("SELECT * FROM meny_retter WHERE resturang_id = ?", (sid,))
    content = cur.fetchall()
    result = []
    for data in content:
        result.append({"id": data[0], "sid": data[1], "rett": data[2], "bilde": data[3], "beskrivelse": data[4], "pris": data[5]})
    return result



if __name__ == "__main__":
    app.run(debug=True, port=5001)