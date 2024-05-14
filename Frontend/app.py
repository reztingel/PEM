from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")



@app.route('/get_product/<product_id>', methods = ["GET","POST"])
def get_product(product_id):
    if product_id is None:
        return "No product ID provided"
    url = 'https://fakestoreapi.com/products/' + product_id
    response = requests.get(url)
    data = response.json()
    return render_template("productt.html", data=data)





if __name__ =="__main__":
    app.run(debug=True)
