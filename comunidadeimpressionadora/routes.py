from flask import render_template, redirect, url_for, flash, request, abort
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin, FormEditarPerfil, FormCriarPost
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user, logout_user, login_required, current_user
import secrets
import os
from PIL import Image #biblioteca que compacta imagem# pip install pillow


@app.route("/")
def home():#ATENÇÃO: tem que conter os posts do usuário mais os dos que ele segue
    posts = Post.query.order_by(Post.id.desc())
    return render_template("home.html", posts=posts)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and "botao_submit_login" in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f"Login feito com sucesso no e-mail {form_login.email.data}", "alert-success")
            par_next = request.args.get("next") #Pega o valor de um parametro específico da url
                                                #args: verifica os parametros da url
            if par_next:
                return redirect(par_next) 
            return redirect(url_for("home"))
        else:
            flash("Falha no login email ou senha incorreto", "alert-danger")
            #ATENÇÃO: ESSA VERIFICAÇÃO PODE FICAR NO FORMS
    
    if form_criarconta.validate_on_submit() and "botao_submit_criarconta" in request.form:
        senha_bcrypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username= form_criarconta.username.data , email= form_criarconta.email.data, 
                          senha=senha_bcrypt)
        database.session.add(usuario)
        database.session.commit()


        flash(f"Login feito com sucesso no e-mail {form_criarconta.email.data}", "alert-success")
        return redirect(url_for("home"))
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)

@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash("Logout feito com sucesso", "alert-success")
    return redirect(url_for("home")) 

@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = url_for("static", filename=f"fotos_perfil/{current_user.foto_perfil}")
    return render_template("perfil.html", foto_perfil=foto_perfil)

@app.route("/post/criar", methods=["GET","POST"])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash("Post criado com sucesso", "alert-success")
        return redirect(url_for("home"))
    return render_template("criarpost.html", form=form)

def salvar_imagem(imagem):
    #cria o código
    codigo = secrets.token_hex(8)

    #adiciona no nome do arquivo
    nome, extensao = os.path.splitext(imagem.filename) #arquivo + extenção# Separar
    nome_arquivo = nome + codigo + extensao #adicionando o token no nome da imagem
    caminho_completo = os.path.join(app.root_path, "static/fotos_perfil", nome_arquivo) #caminho raiz do app

    #reduz a imagem
    tamanho_imagem = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho_imagem) #reduz a imagem# THUMBNAIL significa miniatura

    #salva a imagem
    imagem_reduzida.save(caminho_completo)
    return nome_arquivo

def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if "curso_" in campo.name:
            if campo.data: #se True/ marcado
                lista_cursos.append(campo.label.text)#texto do campo label
    return ";".join(lista_cursos) #transforma uma lista em um texto separado por ;


@app.route("/perfil/editar", methods=["GET", "POST"])
@login_required
def editar_perfil():#ATENÇÃO: quando um usuário novo que não tem curso atualiza alguma informação do perfil, a parte de cursos buga
    form = FormEditarPerfil()
    if form.validate_on_submit():#Method POST
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash("Perfil atualizado com sucesso", "alert-success")
        return redirect(url_for("perfil"))
    elif request.method == "GET":#Method GET
        form.email.data = current_user.email
        form.username.data = current_user.username
    foto_perfil = url_for("static", filename=f"fotos_perfil/{current_user.foto_perfil}")
    return render_template("editarperfil.html", foto_perfil=foto_perfil, form=form)

@app.route("/post/<post_id>", methods=["GET", "POST"])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    
    if current_user == post.autor:
        form = FormCriarPost() #uma stancia do form post
        if request.method == "GET":
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash("Post atualizado com sucesso", "alert-success")
            return redirect(url_for("home"))
    else:
        form = None #para não exibir nada no html
    return render_template("post.html", post=post, form=form)

@app.route("/post/<post_id>/excluir", methods=["GET", "POST"])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash("Post excluido com sucesso", "alert-danger")
        return redirect(url_for("home"))
    else:
        abort(403)
            #403: Link que não tem autorização
            #500: Erro no banco de dados
            #404: Link que não existe