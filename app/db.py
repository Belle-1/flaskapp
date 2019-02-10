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
    address_1 = db.Column(db.Text, nullable=False)
    address_2 = db.Column(db.Text, nullable=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    total = db.Column(db.Integer, nullable=False)  # default= delivery_charges+subtotal
    submitted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    delivery_charges = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)  # needs to be calculated automatically

    def __init__(self, customer_id, submitted_on, delivery_charges, sub_total, quantity, order_items):
        self.customer_id = customer_id
        self.submitted_on = submitted_on
        self.delivery_charges = delivery_charges
        self.sub_total = sub_total
        self.quantity = quantity
        self.order_items = order_items
        self.total = delivery_charges + sub_total


class OrderItem(db.Model):
    __tablename__ = "order_item"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_size_color_id = db.Column(db.Integer, db.ForeignKey('product_size_color.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=True, default=None)
    selling_price = db.Column(db.Integer, nullable=False)  # needs to be calculated automatically like: original price */+=? sale_amount
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, order_id, product_size_color_id, sale_id, quantity):
        self.order_id = order_id
        self.product_size_color_id = product_size_color_id
        self.sale_id = sale_id
        self.quantity = quantity
        self.selling_price = 1/Sale.query.filter_by(id=sale_id).sale_amount * Product.product_size_colors.filter_by(id=product_size_color_id)  # this needs to be checked against None values for sales :)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ar = db.Column(db.Text, nullable=False)
    desc_ar = db.Column(db.Text, nullable=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    on_sale = db.Column(db.Boolean, nullable=False, default=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    photos = db.relationship('ProductPhoto', backref='product', lazy=True)  #
    product_size_colors = db.relationship('ProductSizeColor', backref='product', lazy=True)
    product_sale = db.relationship('ProductSale', backref='product', lazy=True, uselist=False)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(50), nullable=False)
    # cat_ar = db.Column(db.String(50), nullable=False)
    # is_main = db.Column(db.Boolean, nullable=False, default=False)
    # parent_id = db.Column(db.Integer, dbForeignKey('cat.id'), nullable=True)


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(5), nullable=False)
    # size_ar = db.Column(db.String(50), nullable=False)


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(25), nullable=False)
    # color_ar = db.Column(db.String(25), nullable=False)


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_amount = db.Column(db.Integer, nullable=False)
    # sale_amount_ar = db.Column(db.Integer, nullable=False)


class ProductSizeColor(db.Model):
    __tablename__ = "product_size_color"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class ProductSale(db.Model):
    __tablename__ = "product_sale"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)


class ProductPhoto(db.Model):
    __tablename__ = "product_photo"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    photo = db.Column(db.Text, nullable=False)
    is_primary = db.Column(db.Boolean, default=False)
    # is_low_quality = db.Column(db.Boolean, default=False)


class PendingOrder(db.Model):
    __tablename__ = "pending_order"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


class OrderStatus(db.Model):
    __tablename__ = "order_status"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)


class HistoryOrder(db.Model):
    __tablename__ = "history_order"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    order_status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'), nullable=False)
    status_on = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.Text, nullable=True)
