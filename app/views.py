from app import app
from flask import render_template


@app.route('/', methods=["GET"])
def landing_page():
    # "landing page goes in here :))"
    return render_template("landing_page.html")


@app.route("/products/<category_id>", methods=["GET"])
def products(category_id):
    f"this is '{category_id}' products page created mainly for browsing items."
    return render_template("products.html")


@app.route("/product/<int:product_id>", methods=["GET"])
def product(product_id):
    # f"this page shows the information/details about specific product: {product_id} with a 'add to cart' option for customers."
    return render_template("product.html")


@app.route("/shopping_cart", methods=["GET"])
def shopping_cart():
    # "this page shows the items added to the shopping cart."
    return render_template("shopping_cart.html")


@app.route("/submit_purchase", methods=["GET"])
def submit_purchase():
    # "this page dedicated for customers to provide shipment information along with phone number validation for submitting the purchase"
    return render_template("submit_purchase.html")
