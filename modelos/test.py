
# Funcion para obtener todas las recetas favoritas de un usuario especifico
def crear_receta_favorita(fecha_receta_usuario, favorito, id_receta, id_usuario):
    # Realizamos conexion con DB
    con = obtener_conexion_db()
    # Creamos una sentencia para insertar datos de receta favorita
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
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(receta_favorita)
        con.commit()
        favorito = dict(cursor.fetchone())
        return favorito
    # Except en caso de no poder ejecutar sentencia, imprime mensaje editado y error correspondiente
    except Error as e:
        print(f"Error al marcar receta como favorita: {str(e)}")
        return False
    finally:
        if con:
            cursor.close()
            con.close()