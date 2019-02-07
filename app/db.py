from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    mobile_number = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    email_address = db.Column(db.String(150), nullable=False)
    address = db.relationship('Address', backref='customer', lazy=True, uselist=False)
    order = db.relationship('Order', backref='customer', lazy=True, uselist=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    address_1 = db.Column(db.text, nullable=False)
    address_2 = db.Column(db.text, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    submitted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    delivery_charges = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_size_color_id = db.Column(db.Integer, db.ForeignKey('productsizecolor.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    on_sale = db.Column(db.Boolean, nullable=False, default=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    cat = db.relationship('Cat', backref='product', lazy=True, uselist=False)
    sizes = db.relationship('Size', backref='product', lazy=True)
    colors = db.relationship('Color', backref='product', lazy=True)
    photos = db.relationship('ProductPhoto', backref='product', lazy=True)
    product_size_color = db.relationship('ProductSizeColor', backref='product', lazy=True)  # needs to be checked out
    sale = db.relationship('Sale', backref='product', lazy=True, uselist=False)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(50), nullable=False)


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(5), nullable=False)
    size_ar = db.Column(db.String(50), nullable=False)


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(25), nullable=False)
    color_ar = db.Column(db.String(25), nullable=False)


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_amount = db.Column(db.Integer, nullable=False)


class ProductSizeColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# --
class ProductSale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)


class ProductPhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    photo = db.Column(db.Text, nullable=False)
    is_primary = db.Column(db.Boolean, default=False)


class PendingOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


class OrderStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)


class HistoryOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    order_status_id = db.Column(db.Integer, db.ForeignKey('orderstatus.id'), nullable=False)
    status_on = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.Text, nullable=True)
