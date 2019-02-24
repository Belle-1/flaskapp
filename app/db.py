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
    total = db.Column(db.Integer, nullable=False, default=0)
    submitted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    delivery_charges = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False, default=0)
    total_quantity = db.Column(db.Integer, nullable=False, default=0)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def _update(self):
        self.total_quantity = sum([i.quantity for i in self.order_items])
        self.sub_total = sum([i.selling_price for i in self.order_items])
        self.total = self.delivery_charges + self.sub_total


class OrderItem(db.Model):
    __tablename__ = "order_item"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  #
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=True, default=None)  #
    selling_price = db.Column(db.Integer, nullable=False, default=0)  #
    quantity = db.Column(db.Integer, nullable=False)

    def _update(self):
        product_price = Product.query.filter_by(id=self.product_id).first().price
        product_on_sale = Product.query.filter_by(id=self.product_id).first().on_sale
        self.sale_id = ProductSale.query.filter_by(product_id=self.product_id).first().sale_id if product_on_sale else None
        sale_amount = Sale.query.filter_by(id=self.sale_id).first().sale_amount if self.sale_id else 0
        self.selling_price = product_price - (product_price * (sale_amount / 100)) if sale_amount else product_price

    def color(self, lang='eng'):
        if lang == 'eng':
            color = Color.query.filter_by(id=Stock.query.filter_by(self.stock_id).first().color_id).first().color
        elif lang == 'ar':
            color = Color.query.filter_by(id=Stock.query.filter_by(self.stock_id).first().color_id).first().color_ar
        return color

    def size(self, lang='eng'):
        if lang == 'eng':
            size = Size.query.filter_by(id=Stock.query.filter_by(self.stock_id).first().size_id).first().size
        elif lang == 'ar':
            size = Size.query.filter_by(id=Stock.query.filter_by(self.stock_id).first().size_id).first().size_ar
        return size


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ar = db.Column(db.Text, nullable=False)
    desc_ar = db.Column(db.Text, nullable=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    on_sale = db.Column(db.Boolean, nullable=False, default=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    stocks = db.relationship('Stock', backref='product', lazy=True)
    product_sale = db.relationship('ProductSale', backref='product', lazy=True, uselist=False)
    exists = db.Column(db.Boolean, nullable=False, default=True)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.String(50), nullable=False)
    cat_ar = db.Column(db.String(50), nullable=False)
    is_main = db.Column(db.Boolean, nullable=False, default=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=True)
    level = db.Column(db.Integer, nullable=False)


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
    sale_amount_ar = db.Column(db.Integer, nullable=False)


class Stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    photos = db.relationship('ProductPhoto', backref='product', lazy=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)


class ProductSale(db.Model):
    __tablename__ = "product_sale"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)


class ProductPhoto(db.Model):
    __tablename__ = "product_photo"
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    photo = db.Column(db.Text, nullable=False)
    is_primary = db.Column(db.Boolean, nullable=False, default=False)
    is_low_quality = db.Column(db.Boolean, nullable=False, default=False)


class OrderStatus(db.Model):
    __tablename__ = "order_status"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    status_ar = db.Column(db.String(20), nullable=True)


class HistoryOrder(db.Model):
    __tablename__ = "history_order"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    order_status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'), nullable=False)
    status_on = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.Text, nullable=True)
