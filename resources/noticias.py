from flask import request, jsonify, Blueprint
from datetime import datetime

import modelos
from modelos import controller_noticias

# Configuracion del Objeto blueprint con las rutas de noticias
noticias_bp = Blueprint('routes-noticias', __name__)

# --------------------------------NOTICIAS--------------------------------

# ENDPOINT crear nueva noticia - http://127.0.0.1:5000/noticias
@noticias_bp.route('/noticias', methods=["POST"]) #CHEQUEADO
def crear_noticia():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_noticia = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    titulo_noticia = datos_noticia["titulo_noticia"]
    foto_receta = datos_noticia["foto_noticia"]
    # visitas = +1 cada vez que alguien ingresa a la noticia deberia sumar 1 a visitas
    visitas = datos_noticia["visitas"]
    fecha_noticia = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05

    # ejecutamos la funcion crear_receta desde controller receta
    nueva_noticia = controller_noticias.crear_noticia(titulo_noticia, fecha_noticia, visitas, fecha_noticia)

    if nueva_noticia:
        return jsonify({"mensaje": "Noticia Creada"})
    return jsonify({"mensaje": "Internal Error."})

# ENDPOINT obtener todas las noticias de la table noticias en la DB - http://127.0.0.1:5000/noticias
@noticias_bp.route('/noticias', methods=["GET"]) #CHEQUEADO
def obtener_noticias():
    # Obtenermos recetario de invocar funcion obtener_controles en controller_controles
    noticias = modelos.controller_noticias.obtener_noticias()

    if noticias:
        return jsonify({"controles": noticias})
    elif noticias == False:
        return jsonify({"mensaje": "Internal Error"})
    else:
        return jsonify({"controles": {}})

# ENDPOINT eliminar control - http://127.0.0.1:5000/noticias
@noticias_bp.route('/noticias', methods=["DELETE"]) #CHEQUEADO
def eliminar_noticia():
    # variable donde vamos a almacenar el id del control que queremos eliminar
    arg_id_noticia = request.args.get('id_noticia')

    if controller_noticias.eliminar_noticia(arg_id_noticia):
        return jsonify({"mensaje": "Noticia Eliminada"})
    return jsonify({"mensaje": "Internal Error"})