from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin #ATNÇÃO: pesquisar o que essa biblioteca faz

@login_manager.user_loader #Informa ao login manager que essa é a função que retorna o usuário.
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default="default.png")
    posts = database.relationship("Post", backref="autor", lazy=True)
                                #"Post": Nome da tabela relacionada
                                #backref: Nome do usuário dentro da tabela do Post ex: post.autor  > traz o usuário
                                #laze = True: passa todas as informações do autor quando você buscar
    cursos = database.Column(database.String, nullable=False, default="Não informado")
    #ATENÇÃO: Acrescentar os seguidores > followers = database.Column(database.String, nullable=False, default="Não informado")


    def contar_posts(self):
        return len(self.posts)
    
    #def followersCount(self):
    #   return len(self.followers)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)#cria a função no DB para quando o usuário criar o post ela rodar
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)
                                                        #a class tem que está em letra minuscula
    
    #ATENÇÃO: Criar uma coluna que referencia a tabela Like
    #likes =  database.relationship("Like", backref="autor", lazy=True)                                                               #Atributo que você quer pegar

    #ATENÇÃO: Criar uma tabela like que conterá o usuário que deu o like e a quantidade de likes