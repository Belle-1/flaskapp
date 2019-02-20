from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import app
from app.db import  db, Address, Cat, Size, Color, Sale, Product, ProductSizeColor, ProductSale, Customer, Order, OrderItem

db2 = SQLAlchemy(app)


# class User(db2.Model):
#     id = db2.Column(db2.Integer, primary_key=True)
#     name = db2.Column(db2.String(100), nullable=False)
#     slug = db2.Column(db2.String(200), nullable=False)
#     age = db2.Column(db2.String(200), nullable=False)

#     def __init__(self, name, age):
#         self.name = name
#         self.slug = slugify(name)
#         self.age = age



# def slugify(text):
# 	return text[::-1]

# creates pseudo values
from random import randint, choices
from string import ascii_lowercase
def func():
	# categories
	for i in range(1, 20):
		# exec(f"""cat{i} = Cat(cat={''.join(choices(ascii_lowercase, k=5))})""")
		# exec(f"""cat{i} = Cat(cat='asdasd')""")
		db.session.add(eval(f"""Cat(cat='asdasd')"""))

	# for i in range(1, 20):
	# 	db.session.add(eval(f"""cat{i}"""))
	db.session.commit()

	# Sizes
	for i in range(1, 20):
		# exec(f"""size{i} = Size(size={''.join(choices(ascii_lowercase, k=5))})""")
		# exec(f"""size{i} = Size(size='asdf')""")
		db.session.add(eval(f"""Size(size='asdf')"""))

	# for i in range(1, 20):
	# 	db.session.add(eval(f"""size{i}"""))
	db.session.commit()

	# Colors
	for i in range(1, 20):
		# exec(f"""color{i} = Color({''.join(choices(ascii_lowercase, k=10))})""")
		# exec(f"""color{i} = Color(color='cccccc')""")
		db.session.add(eval(f"""Color(color='cccccc')"""))
		print(f'hello from color number {i}')

	# for i in range(1, 20):
	# 	db.session.add(eval(f"""color{i}"""))
	db.session.commit()

	# Sale
	for i in range(1, 20):
		exec(f"""sale{i} = Sale(sale_amount={randint(10, 50)})""")

	for i in range(1, 20):
		db.session.add(eval(f"""sale{i}"""))
	db.session.commit()

	# Product
	for i in range(1, 40):
		# exec(f"""prodcut{i} = Product(name_ar={''.join(choices(ascii_lowercase, k=20))}, cat_id={randint(1, 19)}, price={randint(1000, 50000)}, on_sale={randint(0, 1)}, total_quantity={randint(1, 40)})""")
		# exec(f"""product{i} = Product(name_ar='nnnnnn', cat_id={randint(1, 19)}, price={randint(1000, 50000)}, on_sale={randint(0, 1)}, total_quantity={randint(1, 40)})""")
		db.session.add(eval(f"""Product(name_ar='nnnnnn', cat_id={randint(1, 19)}, price={randint(1000, 50000)}, on_sale={randint(0, 1)}, total_quantity={randint(1, 40)})"""))

	# for i in range(1, 40):
	# 	db.session.add(eval(f"""product{i}"""))
	db.session.commit()

	# ProductSizeColor
	for i in range(1, 50):
		exec(f"""psc{i} = ProductSizeColor(product_id={randint(1, 39)}, size_id={randint(1, 19)}, color_id={randint(1, 19)}, quantity={randint(1,40)})""")

	for i in range(1, 50):
		db.session.add(eval(f"""psc{i}"""))
	db.session.commit()

	# ProductSale
	for i in range(1, 20):
		exec(f"""product_sale{i} = ProductSale(product_id={randint(1, 39)}, sale_id={randint(1, 19)})""")

	for i in range(1, 20):
		db.session.add(eval(f"""product_sale{i}"""))
	db.session.commit()

	# customer
	for i in range(1, 20):
		# exec(f"""customer{i} = Customer(first_name='{''.join(choices(ascii_lowercase, k=20))}', last_name='{''.join(choices(ascii_lowercase, k=20))}', mobile_number={randint(0000000000, 1199999999)}, phone_number={randint(0000000000, 1999999999)}, email_address='{''.join(choices(ascii_lowercase, k=50))}')""")
		# exec(f"""customer{i} = Customer(first_name='ccccuuu', last_name='lllllll', mobile_number={randint(0000000000, 1199999999)}, phone_number={randint(0000000000, 1999999999)}, email_address='name@domain.com')""")
		db.session.add(eval(f"""Customer(first_name='ccccuuu', last_name='lllllll', mobile_number={randint(0000000000, 1199999999)}, phone_number={randint(0000000000, 1999999999)}, email_address='name@domain.com')"""))

	# for i in range(1, 20):
	# 	db.session.add(eval(f"""customer{i}"""))
	db.session.commit()

	# Address
	for i in range(1, 20):
		# exec(f"""add{i} = Address(customer_id={randint(1, 19)}, region='{''.join(choices(ascii_lowercase, k=20))}', district='{''.join(choices(ascii_lowercase, k=20))}', address_1='{''.join(choices(ascii_lowercase, k=100))}', address_2='{''.join(choices(ascii_lowercase, k=randint(30, 100)))}')""")
		# exec(f"""add{i} = Address(customer_id={randint(1, 19)}, region='regionname', district='districtname', address_1='address one', address_2='address two')""")
		db.session.add(eval(f"""Address(customer_id={randint(1, 19)}, region='regionname', district='districtname', address_1='address one', address_2='address two')"""))

	for i in range(1, 20):
		# db.session.add(eval(f"""add{i}"""))
		pass
	db.session.commit()

	# Order
	for i in range(1, 20):
		exec(f"""order{i} = Order(customer_id={randint(1, 19)}, delivery_charges={randint(200, 300)})""")

	for i in range(1, 20):
		db.session.add(eval(f"""order{i}"""))
	db.session.commit()

	# OrderItem
	for i in range(1, 20):
		exec(f"""order_item{i} = OrderItem(order_id={randint(1, 19)}, product_id={randint(1, 19)}, product_size_color_id={randint(1, 49)}, quantity={randint(1, 10)})""")

	for i in range(1, 20):
		db.session.add(eval(f"""order_item{i}"""))
	db.session.commit()

	for i in range(1, 20):
		exec(f"""order_item{i}._update()""")
		exec(f"""order{i}._update()""")
	db.session.commit()

	print("done!")