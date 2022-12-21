import sqlite3
from Usuario import User

class dbusers():
    def __init__(self, path):
        self.path = path

    def crear_tabla_usuarios(self, path): #ejecutar solo si se va a crear la tabla
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f'''
        CREATE TABLE tabla_usuarios (
            nombre text,
            id text PRIMARY KEY,
            exp integer,
            nivel_intervalica text
        )
        ''')
        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

    def insertar_usuario(self, usuario: User):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO tabla_usuarios (nombre, id, exp, nivel_intervalica)
        VALUES ({usuario.name}, {usuario.id}, {usuario.exp}, {usuario.intervalic_level})''')
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()

    def seleccionar_usuario(self, id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        a = cursor.execute(f"SELECT * FROM tabla_usuarios WHERE id = {id}")
        print(a.fetchall())





