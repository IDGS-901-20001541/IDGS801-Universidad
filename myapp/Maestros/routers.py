from flask import Blueprint, redirect, render_template, request, url_for
from temApp import insertMaestro, searchId,modifMaestro, elimiMaestro,getAllTabla
import forms

#establecer el blueprint 
maestros = Blueprint('maestros',__name__)

@maestros.route("/insertprof", methods=['GET','POST'])
def insertarprof():
    create_form = forms.profeForm(request.form)
    if request.method == 'POST':      
        nombre = create_form.nombre.data
        apellidos=create_form.apellidos.data
        correo= create_form.correo.data
        matricula= create_form.matricula.data
        
        insertMaestro.insertM(nombre,apellidos,correo,matricula)

        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('Profesores.html',form = create_form)

@maestros.route("/modProf", methods=['GET','POST'])
def modificarProf():
    create_form = forms.profeForm(request.form)
    if request.method  =='GET':
        id = request.args.get('id')
        resultset= searchId.searchM(id)
        for row in resultset:
                create_form.id.data = id
                create_form.nombre.data = row[2]
                create_form.apellidos.data = row[3]
                create_form.correo.data = row[4]
        
    if request.method == 'POST':    
        id= create_form.id.data  
        nombre = create_form.nombre.data
        apellidos=create_form.apellidos.data
        correo= create_form.correo.data
            
        modifMaestro.modM(nombre,apellidos,id,correo)
        
        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('modificarPro.html',form = create_form)

@maestros.route("/eliminarPro", methods=['GET','POST'])
def eliminarPro():
    create_form = forms.profeForm(request.form)
    if request.method  =='GET':
        id = request.args.get('id')
        resultset= searchId.searchM(id)
        for row in resultset:
                create_form.id.data = id
                create_form.nombre.data = row[2]
                create_form.apellidos.data = row[3]
                create_form.correo.data = row[4]
    if request.method == 'POST':    
        id= create_form.id.data  
        
        elimiMaestro.eliminarM(id)
        
        return redirect(url_for('maestros.ABCompletoProf'))
    return render_template('eliminarPro.html',form = create_form)

@maestros.route("/ABCompletoProf",methods=["GET","POST"])
def ABCompletoProf():
    create_formP = forms.profeForm(request.form)
    resultset1 = getAllTabla.getall()
    print(resultset1)
    for row in resultset1:
         print(row)

    return render_template('ABCProf.html', form = create_formP, profesor = resultset1 ) 
