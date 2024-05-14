from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)



@app.route('/', methods = ["GET"])
def entry():
    return redirect("/front")

@app.route("/front", methods=["GET"])
def front():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    data = response.json()
    return render_template("index.html", data=data)



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
