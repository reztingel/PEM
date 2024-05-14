from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)



@app.route('/', methods = ["GET"])
def entry():
    return redirect("/front")

@app.route("/front", methods=["GET"])
def front():
    category = request.args.get("category")
    if category is None:
        category = "all"
    url = 'https://fakestoreapi.com/products/category/' + category
    if category == "all":
        url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    data = response.json()
    return render_template("index.html", data=data, selected_category=category)





if __name__ =="__main__":
    app.run(debug=True)
