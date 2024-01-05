from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#Para gerar uma hash > no terminal escreva > python > import secrets > secrets.token_hex(16)

app = Flask(__name__)

app.config["SECRET_KEY"] = '9c8393bb76c7909ddc2b6f0cd2b8e2a9'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'#Redireciona para a página de login 
                                    #quando o usuário acessar uma página 
                                    #que requer o login (login_required)
login_manager.login_message_category = "alert-info" #modifica a mensagem que aparece
                                                    #muda a class

from comunidadeimpressionadora import routes


