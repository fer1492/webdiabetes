import sqlite3

# Funcion para establecer conexion con sqlite3 o envia un error en caso contrario | retornar conexion en una variable = conexion
def obtener_conexion_db():
    try:
        conexion = sqlite3.connect('database/diabCompanion.db')
        print("Conexion Exitosa!")
        return conexion
    except Exception as e:
        print(f"Error al conectar con base de datos: {e}", e)