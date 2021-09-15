import sqlite3
from sqlite3 import Error

from database.conexion_database import obtener_conexion_db

# Funcion para crear lugar nuevo
def agregar_lugar(titulo_lugar, fecha_lugar, latitud, longitud):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos de receta
    nuevo_lugar = f"""INSERT INTO lugares(titulo_lugar, 
                                            fecha_lugar, 
                                            latitud, 
                                            longitud)
                                            VALUES ('{titulo_lugar}',
                                                    '{fecha_lugar}',
                                                    {latitud},
                                                    {longitud})"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(nuevo_lugar)
        con.commit()
        return cursor.lastrowid
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al agregar un nuevo lugar {str(e)}")
        return False
    finally:
        cursor.close()
        con.close()

# Funcion para obtener todos los lugares agregadas en la tabla lugares de la DB
def obtener_lugares():
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia query para obtener todas las recetas de la tabla recetas de la DB
    lugares = f"""SELECT * FROM lugares"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        con.execute(lugares)
        lugares_row = cursor.fetchall()
        lista_lugares = [dict(row) for row in lugares_row] # Convertimos cada fila en un diccionario de python dentro de la lista lugares
        return lista_lugares
        # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al oftener lista de lugares {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion para obtener un lugar especifico by id_lugar
def obtener_lugar_by_id(id_lugar):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo lugar
    seleccio_lugar = f"""SELEC FROM lugares WHERE {id_lugar}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(seleccio_lugar)
        lugar = cursor.fetchone()
        return lugar
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al seleccionar lugar {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion actualizar lugar
def editar_lugar(id_lugar, titulo_lugar, fecha_lugar, valoracion_lugar, imagen_lugar, link_web, latitud, longitud):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo lugar
    update_lugar = f"""UPDATE lugares SET titulo_lugar = '{titulo_lugar}',
                                            fecha_lugar = '{fecha_lugar},
                                            valoracion_lugar = '{valoracion_lugar}',
                                            imagen_lugar = '{imagen_lugar}',
                                            link_web = '{link_web}',
                                            latitud = {latitud},
                                            longitud = {longitud} WHERE id_lugar = {id_lugar}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(update_lugar)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al editar lugar {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion eliminar lugar
def eliminar_lugar(id_lugar):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para eliminar datos de un lugar especifico
    eliminar = f"""DELETE FROM lugares WHERE id_lugar = {id_lugar}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(eliminar)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al eliminar lugar {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()
