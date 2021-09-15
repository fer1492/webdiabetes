import sqlite3
from sqlite3 import Error
from database.conexion_database import obtener_conexion_db

# Funcion para crear un control nuevo
def crear_control(fecha_control, valor_glicemia, valor_insulina, comida, comentario_control):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo control
    nuevo_control = f"""INSERT INTO controles(fecha_control,
                                                valor_glicemia,
                                                valor_insulina,
                                                comida,
                                                comentario_control)
                                                VALUES ('{fecha_control}', 
                                                        '{valor_glicemia}',
                                                        '{valor_insulina}',
                                                        '{comida}',
                                                        '{comentario_control}')"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(nuevo_control)
        con.commit()
        return cursor.lastrowid
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al ingresar un nuevo control: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion para obtener todos los controles
def obtener_controles():
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia query para obtener todas los controles de la tabla controles de la DB
    controles = """SELECT * FROM controles"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row  # Nos trae un objeto tipo fila sqlite3, necesitaremos convertirlo en una lista para poder leerlos
        cursor = con.cursor()
        cursor.execute(controles)
        controles_rows = cursor.fetchall()
        lista_controles = [dict(row) for row in controles_rows]  # Convertimos cada fila en un diccionario de python dentro de la lista controles
        return lista_controles
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al obtener los controles: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion para obtener un control especifico by id_Control
def obtener_control_by_id(id_control):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo control
    select_control = f"""SELECT * FROM controles WHERE id_control = {id_control}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(select_control)
        select = dict(cursor.fetchone())
        return select
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al seleccionar el control: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion actualizar control
def editar_control(id_control, fecha_control, valor_glicemia, valor_insulina, comida, comentario_control):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para crear datos para un nuevo control
    nuevo_control = f"""UPDATE controles SET fecha_control = '{fecha_control}',
                                                valor_glicemia = {valor_glicemia},
                                                valor_insulina = {valor_insulina},
                                                comida = '{comida}',
                                                comentario_control = '{comentario_control}' WHERE id_control = {id_control}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(nuevo_control)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al editar el control: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()

# Funcion eliminar control
def eliminar_control(id_control):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para eliminar datos de un control especifico
    eliminar = f"""DELETE FROM controles WHERE id_control = {id_control}"""
    # Try para conectar con DB, ejecutar sentencia y guardar cambios
    try:
        cursor = con.cursor()
        cursor.execute(eliminar)
        con.commit()
        return True
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al eliminar el control: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()