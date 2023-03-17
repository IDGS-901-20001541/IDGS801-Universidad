from db import get_connection

class getAllTabla:
    def getall():
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call consultar_profesores()')
                resulset = curso.fetchall()
            curso.close()
        except Exception as ex:
                print('ERROR')
        return resulset

class searchId:
    def searchM(id):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_profesor(%s)',(id))
                resutset = cursor.fetchall()
                cursor.close()  
        except Exception as ex:
                print('ERROR')
        return resutset

class insertMaestro:
    def insertM(nombre,apellidos,matricula,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call insertar_profesor(%s, %s, %s,%s)',
                              (nombre, apellidos,matricula,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class modifMaestro:
    def modM(nombre,apellidos,id,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call modificar_profesor(%s, %s, %s,%s)',
                              (nombre, apellidos,id,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class elimiMaestro:
    def eliminarM(id):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call eliminar_profesor(%s)',
                              (id))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass
"""**********************************************"""
class getAllTablaAlmno:
    def getallAlumno():
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call consultar_alumnos()')
                resulset = curso.fetchall()
            curso.close()
        except Exception as ex:
                print('ERROR')
        return resulset

class searchIdAlumno:
    def searchA(id):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_alumno(%s)',(id))
                resutset = cursor.fetchall()
                cursor.close()  
        except Exception as ex:
                print('ERROR')
        return resutset

class insertAlumno:
    def insertA(nombre,apellidos,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call insertar(%s, %s, %s)',
                              (nombre, apellidos,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class modifAlumno:
    def modA(id,nombre,apellidos,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call modificar_alumno(%s, %s, %s,%s)',
                              (id,nombre, apellidos,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class elimiAlumno:
    def eliminarA(id):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call eliminar_alumno(%s)',
                              (id))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass


