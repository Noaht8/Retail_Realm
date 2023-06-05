from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'asdbasbdlkajsblda132d'
# create the extension
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes 
