from flask import Flask, jsonify,render_template
from flask import request
from flask import redirect
from flask import url_for
from models import db, Alumnos
from config import DevelomentConfig
import forms
from Alumnos.routers import alumnos
from Directivos.routers import dir
from Maestros.routers import maestros


app= Flask(__name__)
app.config.from_object(DevelomentConfig)
app.config['DEBUG']=True
app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)


@app.route("/",methods=['GET','POST'])
def home():
   btn = request.form.get("registra")
   if btn == 'Maestros':
        return redirect((url_for('maestros.insertarprof')))
   return render_template('main.html')



if __name__=='__main__':
    db.init_app(app)
    with app.app_context():
      db.create_all
    app.run()
