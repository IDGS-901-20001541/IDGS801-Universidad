from flask import Blueprint
from flask import Blueprint, redirect, render_template, request, url_for
import forms
from models import db, Alumnos

#establecer el blueprint 
alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/getAlum',methods=['GET'])
def getdata():
    return {'key':'Alumnos'}

@alumnos.route("/insert", methods=['GET','POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.correo.data)
       #Realizar el insert en la bd
        db.session.add(alum)
        db.session.commit()
        
        return redirect('ABCompleto')
    return render_template('index.html',form = create_form)


@alumnos.route("/ABCompleto",methods=["GET","POST"])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos ) 


@alumnos.route("/modificar",methods=["GET","POST"])
def modificar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    if request.method=='POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        
        db.session.add(alum)
        db.session.commit()
        return redirect('ABCompleto')
    return render_template('modificar.html',form=create_form)


@alumnos.route("/eliminar",methods=["GET","POST"])
def eliminar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    if request.method=='POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABCompleto')
    return render_template('eliminar.html',form=create_form)



