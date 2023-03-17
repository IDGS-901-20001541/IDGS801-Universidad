from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id =IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos') 
    correo = EmailField('correo')

class profeForm(Form):
    id =IntegerField('id')
    matricula=StringField('matricula')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos') 
    correo = EmailField('correo')
    estatus = IntegerField('estatus')

