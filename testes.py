from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

with app.app_context():
    # database.drop_all()
    #     #Apaga tudo do banco de dado
    # database.create_all()
    #     #Criando banco, tem que utilizar a ação dentro de um contexto.
    
        #CRIANDO USUARIOS
    # usuario = Usuario(username= "adriano", email= "adriano20@gmail.com", senha="123123")
    # usuario2 = Usuario(username= "adriano1", email= "adriano21@gmail.com", senha="123123")

    # database.session.add(usuario)
    # database.session.add(usuario2)

    # database.session.commit()

        #CRIANDO POSTS
    # meu_post = Post(id_usuario=1, titulo="Primeiro post", corpo="Publicando o primeiro post no site e gravando no banco de dados")
    # database.session.add(meu_post)
    # database.session.commit()

    # meus_usuarios = Usuario.query.all()
    #                 #Query: para pegar algo do banco
    #                 #all: pega todas as informações da busca
    # print(f"Meus Usuários: {meus_usuarios}")
    # primeiro_usuario = meus_usuarios[1]
    # print(f"Primeiro usuário: {primeiro_usuario}")
    # print(Usuario.query.first())

    # #informações do usuário
    # print(f"id do usuario: {primeiro_usuario.id}")
    # print(f"id do usuario: {primeiro_usuario.senha}")
    # print(f"e-mail do usuário: {primeiro_usuario.email}")
    # print(f"Postes do primeiro usuário: {primeiro_usuario.posts}")

    # #Filtrar por algo
    # usuario2 = Usuario.query.filter_by(id=2).first()
    #                                         #Pega o primeiro usuário de resposta dessa query
    #                                         #caso não colocar ele retorna a query
    #                                         #se quiser todos coloca .all()
    # print(usuario2,"\n")

    # post = Post.query.all()
    # print("O autor do post é o: ", post[0].autor, "\n", f"O e-mail dele é: {post[0].autor.email}")

    pass

