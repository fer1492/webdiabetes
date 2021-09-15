from flask import request, jsonify, Blueprint
from datetime import datetime

from modelos import controller_lugares

# Configuracion del Objeto blueprint con las rutas de lugares
lugares_bp = Blueprint('route-lugares', __name__)

# --------------------------------LUGARES--------------------------------

# ENDPOINT crear nuevo lugar - http://127.0.0.1:5000/lugares
@lugares_bp.route('/lugares', methods=["POST"]) #CHEQUEADO
def agregar_lugar():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_lugar = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    titulo_lugar = datos_lugar['titulo_lugar']
    fecha_lugar = datetime.now().strftime('%x %X')  # formato time: 5/22/2021 10:24:05
    latitud = datos_lugar['latitud']
    longitud = datos_lugar['longitud']

    # ejecutamos la funcion crear_control desde controller_controles
    nuevo_lugar = controller_lugares.agregar_lugar(titulo_lugar, fecha_lugar, latitud, longitud)

    if nuevo_lugar:
        return jsonify({"mensaje": "Nuevo lugar creado con exito"})
    return jsonify({"mensaje": "Internal Error"})

# ENDPOINT obtener todos los lugares de la table lugares en la DB - http://127.0.0.1:5000/lugares
@lugares_bp.route('/lugares', methods=["GET"]) #NO CHEQUEADO IMPRIME DICCIONARIO VACIO
def obtener_lugares():
    # Obtenermos lugares de invocar funcion obtener_lugares en controller_lugares
    todos_lugares = controller_lugares.obtener_lugares()

    if todos_lugares:
        return jsonify({"lugares": todos_lugares})
    elif todos_lugares == False:
        return jsonify({"mensjae": "Internal Error"})
    else:
        return jsonify({"lugares": {}})

# ENDPOINT editar lugar - http://127.0.0.1:5000/lugares
@lugares_bp.route('/lugares', methods=["PUT"]) #ERROR AL SELECCIONA POR ID
def editar_lugar():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_lugar = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    titulo_lugar = datos_lugar["titulo_lugar"]
    valoracion_lugar = datos_lugar["valoracion_lugar"]
    imagen_lugar = datos_lugar["imagen_lugar"]
    link_web = datos_lugar["link_web"]
    fecha_lugar = datetime.now().strftime('%x %X')  # formato time: 5/22/2021 10:24:05
    latitud = datos_lugar["latitud"]
    longitud = datos_lugar["longitud"]

    # Recibimos el id_control como argumento para seleccionar cual queremos editar
    arg_id_lugar = request.args.get('id_lugar')

    if controller_lugares.editar_lugar(arg_id_lugar, titulo_lugar, valoracion_lugar, imagen_lugar, link_web, fecha_lugar, latitud, longitud):
        nuevo_lugar = controller_lugares.obtener_lugar_by_id(arg_id_lugar)
        return jsonify({"Lugar editado con exito": nuevo_lugar})
    return jsonify({"mensaje": "Internal Error"})

# ENDPOINT eliminar lugar - http://127.0.0.1:5000/lugares
@lugares_bp.route('/lugares', methods=["DELETE"]) #CHEQUEADO
def eliminar_lugar():
    # variable donde vamos a almacenar el id del lugar que queremos eliminar
    arg_id_lugar = request.args.get('id_lugar')

    if controller_lugares.eliminar_lugar(arg_id_lugar):
        return jsonify({"mensaje": "Lugar Eliminado"})
    return jsonify({"mensaje": "Internal Error"})
