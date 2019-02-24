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


def func2():
	products = [
		{'name', 'name_ar', 'desc', 'cat_id', 'price', 'on_sale', 'total_quantity'}
	]
	colors = [
		{'color': 'red', 'color_ar': 'أحمر'},
		{'color': 'pink', 'color_ar': 'زهري'},
		{'color': 'black', 'color_ar': 'أسود'},
		{'color': 'blue', 'color_ar': 'أزرق'},
		{'color': 'green', 'color_ar': 'أخضر'},
		{'color': 'light green', 'color_ar': 'أخضر فاتح'},
		{'color': 'dark green', 'color_ar': 'جيشي'},
		{'color': 'white', 'color_ar': 'أبيض'},
		{'color': 'purple', 'color_ar': 'بنفسجي'},
		{'color': 'oily', 'color_ar': 'زيتي'},
		{'color': 'dark red', 'color_ar': 'خمري'},
		{'color': 'yellow', 'color_ar': 'أصفر'},
		{'color': 'dark blue', 'color_ar': 'كحلي'},
		{'color': 'orange', 'color_ar': 'برتقالي'},
		{'color': 'cyan', 'color_ar': 'سماوي'},
		{'color': 'grey', 'color_ar': 'رمادي'},
		{'color': 'brown', 'color_ar': 'بني'},
		{'color': 'beige', 'color_ar': 'بيج'},
	]
	sizes = [
		{'size': 'XM', 'size_ar': 'XM'},
		{'size': 'XS', 'size_ar': 'XS'},
		{'size': 'S', 'size_ar': 'S'},
		{'size': 'M', 'size_ar': 'M'},
		{'size': 'L', 'size_ar': 'L'},
		{'size': 'XL', 'size_ar': 'XL'},
		{'size': 'XXL', 'size_ar': 'XXL'},
		{'size': 'XXXL', 'size_ar': 'XXXL'},
		{'size': 'XXXXL', 'size_ar': 'XXXL'},
	]
	cats = [
		{'id': 1,'cat': 'women', 'cat_ar': 'نساء', 'is_main': True, 'parent_id': None, 'level': 0},
		{'id': 2,'cat': 'men', 'cat_ar': 'رجال', 'is_main': True, 'parent_id': None, 'level': 0},
		{'id': 3,'cat': 'kids', 'cat_ar': 'أطفال', 'is_main': True, 'parent_id': None, 'level': 0},
		{'id': 4, 'cat': 'girls', 'cat_ar': 'بناتي', 'is_main': False, 'parent_id': 3, 'level': 1},
		{'id': 5, 'cat': 'boys', 'cat_ar': 'ولادي', 'is_main': False, 'parent_id': 3, 'level': 1},
		{'id': 6, 'cat': 'jackets & coats', 'cat_ar': 'الجاكيتات و المغاطف', 'is_main': False, 'parent_id': 4, 'level': 2},
		{'id': 7, 'cat': 'sweaters & hoodies', 'cat_ar': 'كنزات و ههوديز', 'is_main': False, 'parent_id': 2, 'level': 1},
		{'id': 8, 'cat': 'underwear', 'cat_ar': 'ملابس داخلية', 'is_main': False, 'parent_id': 2, 'level': 1},
		{'id': 9,'cat': 'jackets & Coats', 'cat_ar': 'الجاكيتات و المعاطف', 'is_main': False, 'parent_id': 1, 'level': 1},
		{'id': 10,'cat': 'jackets & Coats', 'cat_ar': 'الجاكيتات و المعاطف', 'is_main': False, 'parent_id': 2, 'level': 1},
	]
	sales = [
		{'sale_amount': 5, 'sale_amount_ar': '٥'}
		{'sale_amount': 10, 'sale_amount_ar': '١٠'}
		{'sale_amount': 15, 'sale_amount_ar': '١٥'}
		{'sale_amount': 20, 'sale_amount_ar': '٢٠'}
		{'sale_amount': 25, 'sale_amount_ar': '٢٥'}
		{'sale_amount': 30, 'sale_amount_ar': '٣٠'}
		{'sale_amount': 35, 'sale_amount_ar': '٣٥'}
		{'sale_amount': 40, 'sale_amount_ar': '٤٠'}
		{'sale_amount': 45, 'sale_amount_ar': '٤٥'}
		{'sale_amount': 50, 'sale_amount_ar': '٥٠'}
		{'sale_amount': 55, 'sale_amount_ar': '٥٥'}
		{'sale_amount': 60, 'sale_amount_ar': '٦٠'}
		{'sale_amount': 65, 'sale_amount_ar': '٦٥'}
		{'sale_amount': 70, 'sale_amount_ar': '٧٠'}
		{'sale_amount': 75, 'sale_amount_ar': '٧٥'}
		{'sale_amount': 80, 'sale_amount_ar': '٨٠'}
		{'sale_amount': 85, 'sale_amount_ar': '٨٥'}
		{'sale_amount': 90, 'sale_amount_ar': '٩٠'}
		{'sale_amount': 95, 'sale_amount_ar': '٩٥'}
		{'sale_amount': 100, 'sale_amount_ar': '١٠٠'}
	]
	status = [
		{'status': 'accepted', 'status_ar': ''},
		{'status': 'failed', 'status_ar': ''},
		{'status': 'declined', 'status_ar': ''},
		{'status': 'delivered', 'status_ar': ''},
		{'status': 'pending', 'status_ar': 'قيد انتظار الوموافقة'},
		{'status': 'awaiting shipment', 'status_ar': 'قيد انتظار الشحن'},
		{'status': 'shipped', 'status_ar': ''},
		{'status': 'delivering', 'status_ar': 'قيد التوصيل'},
		{'status': 'returned', 'status_ar': ''},
		{'status': 'removed', 'status_ar': ''},
		{'status': 'on hold', 'status_ar': ''}, # means that a product is now shipped to somebody but not delivered yet. so there is a possiblity of returning it
	]
	product_photos = [
		{'product_id': , 'photo_name': '', 'is_primary': , 'is_low_quality': },
	]

	stock = [
		{'product_id': , 'size_id': , 'color_id': , 'quantity': },
	]
	product_sales = [
		{'product_id': , 'sale_id': },
	]

