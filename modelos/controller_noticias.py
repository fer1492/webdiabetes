import sqlite3
from sqlite3 import Error
from database.conexion_database import obtener_conexion_db

# Funcion para crear noticia nueva
def crear_noticia(titulo_noticia, foto_noticia, visitas, fecha_noticia):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos de noticia
    nueva_noticia = f"""INSERT INTO noticias(titulo_noticia,
                                                foto_noticia,
                                                visitas,
                                                fecha_noticia)
                                                VALUES ('{titulo_noticia}',
                                                        '{foto_noticia}',
                                                        '{visitas}',
                                                        '{fecha_noticia}')"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(nueva_noticia)
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
def obtener_noticias():
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia query para obtener todas las noticias de la tabla noticias de la DB
    noticiario = """SELECT * FROM noticias"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        cursor.execute(noticiario)
        noticias_rows = cursor.fetchall()
        lista_noticias = [dict(row) for row in noticias_rows] # Convertimos cada fila en un diccionario de python dentro de la lista noticias
        return lista_noticias
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al obtener las noticias: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion eliminar noticia
def eliminar_noticia(id_noticia):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para eliminar datos de un nuevo control especifico
    eliminar = f"""DELETE FROM noticias WHERE id_noticia = {id_noticia}"""
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