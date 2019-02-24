from app import app
from flask import render_template


@app.route('/', methods=["GET"])
def landing_page():
    # "landing page goes in here :))"
    return render_template("landing_page.html")


@app.route("/products/<int:category_id>", methods=["GET"])
def products(category_id):
    # f"this is '{category_id}' products page created mainly for browsing items."
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


@app.route("/logIn", methods=["GET", "POST"])
def log_in():
    # this page meant for rmployees to get to the system
    return render_template("log_in.html")


@app.route("/dashboard/<status>", methods=["GET", "POST"])
def dashboard(status):
    # this page shows orders to employees
    if status == "pending":
        return render_template("pending_orders.html")
    elif status == "awaits_shipment":
        return render_template("awaits_shipment.html")
    elif status == "delivering":
        return render_template("delivering.html")
    elif status == "failed":
        return render_template("failed_orders.html")
    return render_template("dashboard.html")



























#