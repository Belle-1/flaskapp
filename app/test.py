from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import app

db2 = SQLAlchemy(app)


class User(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    name = db2.Column(db2.String(100), nullable=False)
    slug = db2.Column(db2.String(200), nullable=False)
    age = db2.Column(db2.String(200), nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.slug = slugify(name)
        self.age = age



def slugify(text):
	return text[::-1]

# creates pseudo values
from random import randint, choices
from string import ascii_lowercase
from ... import Cat, Size, Color, Sale, Product, ProductSizeColor, ProductSale

# categories
for i in range(1, 20):
	exec(f"""cat{i} = Cat({''.join(choices(ascii_lowercase, k=15))})""")

for i in range(1, 20):
	db.session.add(eval(f"""cat{i}"""))
db.session.commit()

# Sizes
for i in range(1, 20):
	exec(f"""size{i} = Size({''.join(choices(ascii_lowercase, k=5))})""")

for i in range(1, 20):
	db.session.add(eval(f"""size{i}"""))
db.session.commit()

# Colors
for i in range(1, 20):
	exec(f"""color{i} = Color({''.join(choices(ascii_lowercase, k=10))})""")

for i in range(1, 20):
	db.session.add(eval(f"""color{i}"""))
db.session.commit()

# Sale
for i in range(1, 20):
	exec(f"""sale{i} = Sale({randint(10, 50)})""")

for i in range(1, 20):
	db.session.add(eval(f"""sale{i}"""))
db.session.commit()

# Product
for i in range(1, 40):
	exec(f"""prodcut{i} = Product(name_ar={''.join(choices(ascii_lowercase, k=20))}, cat_id={randint(1, 19)}, price={randint(1000, 50000)}, on_sale={randint(0, 1)}, total_quantity={randint(1, 40)})""")

for i in range(1, 40):
	db.session.add(eval(f"""product{i}"""))
db.session.commit()

# ProductSizeColor
for i in range(1, 50):
	exec(f"""psc{i} = ProductSizeColor(product_id={randint(1, 40)}, size_id={randint(1, 20)}, color_id={randint(1, 20)}, quantity={randint(1,40)})""")

for i in range(1, 50):
	db.session.add(eval(f"""psc{i}"""))
db.session.commit()

# ProductSale
for i in range(1, 20):
	exec(f"""sale{i} = Sale({randint(10, 50)})""")

for i in range(1, 20):
	db.session.add(eval(f"""sale{i}"""))
db.session.commit()