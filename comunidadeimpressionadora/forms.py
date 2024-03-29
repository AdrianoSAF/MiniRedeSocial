from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao = PasswordField("confirmação da Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado")

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("senha", validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField("Lembrar dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")

    #ATENÇÃO VALIDAR EMAIL E SENHA

class FormEditarPerfil(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField("Atualizar foto de perfil", validators=[FileAllowed(["jpg", "png"])])

    curso_excel = BooleanField("Excel Impressionador")
    curso_vba = BooleanField("VBA Impressionador")
    curso_powerbi = BooleanField("PowerBi Impressionador")
    curso_python = BooleanField("Python Impressionador")
    curso_ppt = BooleanField("Apresentações Impressionadoras")
    curso_sql = BooleanField("SQL Impressionador")
    

    botao_submit_editarperfil = SubmitField("Confirmar edição")
    
    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("já existe um usuário com esse e-mail")
            
class FormCriarPost(FlaskForm):
    titulo = StringField("Titulo do poste", validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField("Escreva algo aqui", validators=[DataRequired()])
    botao_submit_post = SubmitField("Criar Post")

