from flask import request, jsonify, Blueprint
from datetime import datetime

import modelos
from modelos import controller_recetas

# Configuracion del Objeto blueprint con las rutas de recetas
recetas_bp = Blueprint('routes-recetas', __name__)

# --------------------------------RECETAS--------------------------------

# ENDPOINT crear nueva receta - http://127.0.0.1:5000/recetas
@recetas_bp.route('/recetas', methods=["POST"]) #CHEQUEADO
def crear_receta():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_receta = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    titulo = datos_receta["titulo"]
    foto_receta = datos_receta["foto_receta"]
    tiempo = datos_receta["tiempo"]
    fecha_receta = datetime.now().strftime("%x %X") #formato time: 5/22/2021 10:24:05

    # ejecutamos la funcion crear_receta desde controller receta
    nueva_receta = controller_recetas.crear_receta(titulo, foto_receta, tiempo, fecha_receta)

    if nueva_receta:
        return jsonify({"mensaje": "Receta creada"})
    return jsonify({"mensaje": "Internal Error."})

# ENDPOINT obtener todas las recetas de la table recetas en la DB - http://127.0.0.1:5000/recetas
@recetas_bp.route('/recetas', methods=["GET"]) #CHEQUEADO
def obtener_recetas():
    # Obtenermos recetario de invocar funcion obtener_recetas en controller_recetas
    recetario = modelos.controller_recetas.obtener_recetas()

    if recetario:
        return jsonify({"recetas": recetario})
    elif recetario == False:
        return jsonify({"mensaje": "Internal Error"})
    else:
        return jsonify({"recetas": {}})

# ENDPOINT obtener receta especifica by id - http://127.0.0.1:5000/recetas
def obtener_receta_by_id():
    pass

# ENDPOINT eliminar receta - http://127.0.0.1:5000/recetas
@recetas_bp.route('/recetas', methods=["DELETE"]) #CHEQUEADA
def eliminar_receta():
    # variable donde vamos a almacenar el id de la receta que queremos eliminar
    arg_id_receta = request.args.get('id_receta')

    if controller_recetas.eliminar_receta(arg_id_receta):
        return jsonify({"mensaje": "Receta Eliminada"})
    return jsonify({"mensaje": "Internal Error"})

