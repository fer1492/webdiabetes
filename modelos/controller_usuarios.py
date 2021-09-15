import sqlite3
from sqlite3 import Error
from database.conexion_database import obtener_conexion_db

# Funcion para crear usuario - Sign Up
def signup(username, mail, password, fehca_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos de noticia
    crear_usuario = f"""INSERT INTO usuarios(username, mail, password, fecha_usuario)
                        VALUES ('{username}', '{mail}', '{password}', '{fehca_usuario}')"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(crear_usuario)
        con.commit()
        return cursor.lastrowid
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al crear usuario: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion obtener todos los usuarios
def obtener_usuarios():
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia query para obtener todas los controles de la tabla controles de la DB
    usuarios = f"""SELECT * FROM usuarios"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        cursor.execute(usuarios)
        usuarios_row = cursor.fetchall()
        lista_usuarios = [dict(row) for row in usuarios_row] # Convertimos cada fila en un diccionario de python dentro de la lista controles
        return lista_usuarios
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al obtener los usuarios: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion obtener usuario_by_id - Sign In
def obtener_usuario_by_id(id_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo control
    seleccionar_usuario = f"""SELECT FROM usuarios WHERE id_usuario = {id_usuario}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(seleccionar_usuario)
        select = dict(cursor.fetchone())
        return select
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al seleccionar usuario: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion editar tados de usuario - actualizacion perfil de usuario
def editar_usuario(id_usuario, username, mail, password, foto_usuario, pais, fecha_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo control
    update_perfil = f"""UPDATE usuarios SET username = '{username}',
                                            mail = '{mail}',
                                            password = '{password}',
                                            foto_usuario = '{foto_usuario}',
                                            pais = '{pais}',
                                            fecha_usuario = '{fecha_usuario}' WHERE id_usuario = {id_usuario}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(update_perfil)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al editar datos de perfil de usuario: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()