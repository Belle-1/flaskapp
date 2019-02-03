# from flask import Flask
#
#
# app = Flask(__name__,
#             instance_relative_config=True,
#             )
# app.config.from_object('config')
# app.config.from_pyfile('config.py')
#
# # print(app.config['DEBUG'])
# # print(app.config['SECRET_KEY'])


from flask import Flask
import os
from unipath import Path


app = Flask(__name__,
            instance_relative_config=True,
            instance_path=os.getcwd() + "\instance")
app.config.from_object('config')
app.config.from_pyfile('config.py')


from app import views
