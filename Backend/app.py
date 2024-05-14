from flask import Flask, request, send_from_directory
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)


con = sqlite3.connect("./database.db", check_same_thread=False)
cur = con.cursor()



@app.route('/get_image/<image_name>', methods = ["GET"])
def get_image(image_name):
    return send_from_directory(r"C:\Users\Ton\OneDrive - Innlandet fylkeskommune\Skrivebord\Eksamenforbredning\Backend\static\images", image_name)


@app.route('/get_resturanger', methods = ["GET"])
def get_resturants():
    cur.execute("SELECT * FROM resturanger")
    content = cur.fetchall()
    result = []
    for resturant in content:
        result.append({"navn": resturant[1], "id": resturant[0]})
    return result


@app.route('/get_resturant', methods = ["GET"])
def get_resturant():
    rid = request.get_json()["rid"]
    cur.execute("SELECT * FROM resturanger WHERE id = ?", (rid,))
    content = cur.fetchone()
    result = [content[0], content[1]]
    return result



@app.route('/get_resturang_meny', methods = ["GET"])
def resturang_meny():
    rid = request.get_json()["rid"]
    cur.execute("SELECT * FROM meny_retter WHERE resturang_id = ?", (rid,))
    content = cur.fetchall()
    result = []
    for data in content:
        result.append({"id": data[0], "rid": data[1], "rett": data[2], "bilde": data[3], "besrkivelse": data[4], "pris": data[5]})
    return result



if __name__ == "__main__":
    app.run(debug=True, port=5010)