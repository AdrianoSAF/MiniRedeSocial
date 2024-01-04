from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#Para gerar uma hash > no terminal escreva > python > import secrets > secrets.token_hex(16)

app = Flask(__name__)

app.config["SECRET_KEY"] = '9c8393bb76c7909ddc2b6f0cd2b8e2a9'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from comunidadeimpressionadora import routes


