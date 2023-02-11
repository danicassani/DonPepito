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

        conn.commit()
        conn.close()

    def print_columnas(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        a = cursor.execute("PRAGMA table_info(tabla_usuarios)").fetchall()
        conn.close()
        return a

    def insertar_usuario(self, usuario: User):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        #Is the user already registered?
        already_registered = cursor.execute(f'SELECT EXISTS (SELECT 1 FROM tabla_usuarios WHERE id={usuario.id} LIMIT 1)').fetchone()[0] == 1
        if already_registered:
            success = False
        else:    
            query = f'''INSERT INTO tabla_usuarios (nombre, id, exp, nivel_intervalica)
            VALUES ('{usuario.name}', '{usuario.id}', {usuario.exp}, '{usuario.intervalic_level}')'''
            cursor.execute(query)
            success = True
        conn.commit()
        conn.close()
        
        return success

    def seleccionar_usuario(self, id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        a = cursor.execute(f"SELECT * FROM tabla_usuarios WHERE id = {id}").fetchall()
        return a

    def mostrar_todo(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        a = cursor.execute(f"SELECT * FROM tabla_usuarios").fetchall()
        print(a)






