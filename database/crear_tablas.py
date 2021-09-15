import sqlite3
from sqlite3 import Error

# Funcion para establecer coneccion con sqlite3 sino envia un error | retornar conexion en una variable
def obtener_conexion_db():
    try:
        conexion = sqlite3.connect('diabCompanion.db')
        print("Conexion Exitosa!")
        return conexion
    except Error:
        print(Error)

# Funcion para crear tablas | Debo pasarle parametro de conexion con sqlite3 - funcion de obtener conexion en variable
def crear_tablas(conexion):
    # variable tablas = lista de todas las tablas a crear para diabCompanion.db
    tablas = [
        """CREATE TABLE usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                                   username TEXT (25) NOT NULL UNIQUE,
                                   mail TEXT NOT NULL UNIQUE,
                                   password TEXT (16) NOT NULL,
                                   foto_usuario TEXT,
                                   pais TEXT,
                                   fecha_usuario TEXT NOT NULL)""",

        """CREATE TABLE controles(id_control INTEGER PRIMARY KEY AUTOINCREMENT,
                                    fecha_control TEXT NOT NULL,
                                    valor_glicemia INTEGER DEFAULT 0,
                                    valor_insulina INTEGER DEFAULT 0,
                                    comida TEXT,
                                    comentario_control TEXT (50),
                                    id_usuario,
                                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario))""",

        """CREATE TABLE recetas(id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo TEXT (25) NOT NULL,
                                foto_receta TEXT NOT NULL,
                                tiempo INTEGER NOT NULL,
                                fecha_receta TEXT NOT NULL,
                                id_usuario INTEGER,
                                FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario))""",

        """CREATE TABLE noticias(id_noticia INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo_noticia TEXT (25) NOT NULL,
                                visitas INTEGER DEFAULT 0,
                                foto_noticia TEXT NOT NULL,
                                fecha_noticia TEXT NOT NULL)""",

        """CREATE TABLE lugares(id_lugar INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo_lugar TEXT (25) NOT NULL,
                                valoracion_lugar REAL DEFAULT 0.0,
                                imagen_lugar TEXT,
                                link_web TEXT,
                                fecha_lugar DATE NOT NULL,
                                latitud REAL NOT NULL,
                                longitud REAL NOT NULL)""",

        """CREATE TABLE recetas_usuarios(comentario TEXT (50),
                                        fecha_receta_usuario TEXT NOT NULL,
                                        valoracion REAL DEFAULT 0.0,
                                        favorito INTEGER DEFAULT 0 NOT NULL,
                                        id_receta INTEGER NOT NULL,
                                        id_usuario INTEGER NOT NULL,
                                        FOREIGN KEY(id_receta) REFERENCES recetas(id_receta),
                                        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
                                        PRIMARY KEY (id_receta, id_usuario))""",

        """CREATE TABLE noticias_usuarios(favorito INTEGER DEFAULT 0 NOT NULL,
                                            id_noticia INTEGER NOT NULL,
                                            id_usuario INTEGER NOT NULL,
                                            FOREIGN KEY(id_noticia) REFERENCES noticias(id_noticia),
                                            FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
                                            PRIMARY KEY (id_noticia, id_usuario))""",

        """CREATE TABLE lugares_usuarios(comentario TEXT (50),
                                        fecha_lugares_usuarios TEXT NOT NULL,
                                        valoracion REAL DEFAULT 0.0,
                                        favorito INTEGER DEFAULT 0 NOT NULL,
                                        id_lugar INTEGER NOT NULL,
                                        id_usuario INTEGER NOT NULL,
                                        FOREIGN KEY(id_lugar) REFERENCES lugares(id_lugar),
                                        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
                                        PRIMARY KEY (id_lugar, id_usuario))"""
    ]

    for tabla in tablas:
        conexion.execute(tabla)
    conexion.commit()
    print("Tablas creadas con exito!")

# Corro el codigo - name = main me permite ejecutar el codigo solo desde este script, no desde otro
if __name__ == "__main__":
    # Intentamos con un try crear las tablas
    try:
        print("Creando Base de datos...")
        conexion = sqlite3.connect('diabCompanion.db')
        print("Creando Tablas...")
        # Ciclo for para iterar y crear cada una de las tablas de la DB
        crear_tablas(conexion)
        conexion.close()
    except Exception as e:
        print(f"Error creando base de datos: {e}", e)