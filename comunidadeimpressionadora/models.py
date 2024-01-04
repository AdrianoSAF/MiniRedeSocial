from comunidadeimpressionadora import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default="default.jpg")
    posts = database.relationship("Post", backref="autor", lazy=True)
                                #"Post": Nome da tabela relacionada
                                #backref: Nome do usuário dentro da tabela do Post ex: post.autor  > traz o usuário
                                #laze = True: passa todas as informações do autor quando você buscar
    cursos = database.Column(database.String, nullable=False, default="Não informado")

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)#cria a função no DB para quando o usuário criar o post ela rodar
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)
                                                                    #a class tem que está em letra minuscula
                                                                    #Atributo que você quer pegar
