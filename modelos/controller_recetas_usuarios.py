import sqlite3
from sqlite3 import Error

from database.conexion_database import obtener_conexion_db

# Funcion para obtener todas las recetas favoritas de un usuario especifico
def crear_receta_favorita(fecha_receta_usuario, favorito, id_receta, id_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos de receta
    receta_favorita = f"""INSERT INTO recetas_usuarios(fecha_receta_usuarios,
                                                         favorito,
                                                         id_receta,
                                                         id_usuario)
                                                         VALUES('{fecha_receta_usuario}',
                                                                 {favorito},
                                                                 {id_receta},
                                                                 {id_usuario})"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(receta_favorita)
        con.commit()
        return cursor.lastrowid
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al marcar receta como favorita: {str(e)}")
        return False

    finally:
        if con:
            cursor.close()
            con.close()

def obtener_recetas_favoritas(id_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para insertar datos de receta favorita
    receta_favorita = f"""SELECT * recetar r, usuarios u WHERE r.{id_usuario} = u.{id_usuario}"""

    try:
        con.row_factory = sqlite3.Row   # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        cursor.execute(receta_favorita)
        lista_recetas = cursor.fetchall()
        recetas = [dict(row) for row in lista_recetas]  # Convertimos cada fila en un diccionario de python dentro de la lista recetas
        return recetas
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al obtener recetas favoritas de usuario {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

crear_receta_favorita("10/09/2021 19:56:08", 1, 2, 1)