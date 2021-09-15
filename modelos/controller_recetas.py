import sqlite3
from sqlite3 import Error
from database.conexion_database import obtener_conexion_db

from datetime import datetime

# Funcion para crear receta nueva
def crear_receta(titulo, foto_receta, tiempo, fecha_receta):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos de receta
    nueva_receta = f"""INSERT INTO recetas(titulo, 
                                            foto_receta, 
                                            tiempo,
                                            fecha_receta) 
                                            VALUES ('{titulo}', 
                                                    '{foto_receta}', 
                                                    {tiempo}, 
                                                    '{fecha_receta}')"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(nueva_receta)
        con.commit()
        return cursor.lastrowid
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al insertar nueva receta: {str(e)}")
        return False

    finally:
        if con:
            cursor.close()
            con.close()

# Funcion para obtener todas las recetas agregadas en la tabla recetas de la DB
def obtener_recetas():
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia query para obtener todas las recetas de la tabla recetas de la DB
    recetario = """SELECT * FROM recetas"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        cursor.execute(recetario)
        recetas_rows = cursor.fetchall()
        recetas = [dict(row) for row in recetas_rows] # Convertimos cada fila en un diccionario de python dentro de la lista recetas
        return recetas
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al obtener las recetas: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion para obtener una receta especifico by id_receta
def obtener_receta_by_id(id_receta):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para una nuevo receta
    select_receta = f"""SELECT * FROM recetas WHERE id_receta = {id_receta}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(select_receta)
        select = dict(cursor.fetchone())
        return select
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al seleccionar la receta: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion eliminar receta
def eliminar_receta(id_receta):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para eliminar datos de un nuevo control especifico
    eliminar = f"""DELETE FROM recetas WHERE id_receta = {id_receta}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(eliminar)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al eliminar la receta: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()