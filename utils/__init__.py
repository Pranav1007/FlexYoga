import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

template_dir = os.path.abspath("utils/templates")
static_dir = os.path.abspath("utils/static")
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(32)

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from utils.flaskblog import routes
