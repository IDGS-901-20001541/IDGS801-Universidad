
from db import get_connection

try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call consultar_profesores()')
                resulset = curso.fetchall()
                for row in resulset:
                    print(row)
                connection.close()
except Exception as e:
    print(e)
    pass