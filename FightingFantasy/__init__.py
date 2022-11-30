import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configure database
app.config['SECRET_KEY'] = '\xbc\xb5\xfaQeX-\x10\x86\xee\xb1\x83\xfa\x96^\xb1u\xaaY\x1bC.\xf7\xe8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ffp.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(app)

import models
import views