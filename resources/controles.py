from flask import request, jsonify, Blueprint
from datetime import datetime

import modelos
from modelos import controller_controles

# Configuracion del Objeto blueprint con las rutas de controles
controles_bp = Blueprint('routes-controles', __name__)

# --------------------------------CONTROLES (solo con usuario logeado)--------------------------------

# ENDPOINT crear nuevo control - http://127.0.0.1:5000/controles
@controles_bp.route('/controles', methods=["POST"]) #CHEQUEADO
def crear_control():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_control = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    fecha_control = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05
    valor_glicemia = datos_control["valor_glicemia"]
    valor_insulina = datos_control["valor_insulina"]
    comida = datos_control["comida"]
    comentario_control = datos_control["comentario_control"]

    # ejecutamos la funcion crear_control desde controller_controles
    nuevo_control = controller_controles.crear_control(fecha_control, valor_glicemia, valor_insulina, comida, comentario_control)

    if nuevo_control:
        return jsonify({"mensaje": "Nuevo Control creado con exito"})
    return jsonify({"mensaje": "Internal Error"})

# ENDPOINT obtener todas las recetas de la table recetas en la DB - http://127.0.0.1:5000/controles
@controles_bp.route('/controles', methods=["GET"]) #CHEQUEADO - falta asignar a que usuario corresponde el control
def obtener_controles():
    # Obtenermos recetario de invocar funcion obtener_controles en controller_controles
    controles = modelos.controller_controles.obtener_controles()

    if controles:
        return jsonify({"controles": controles})
    elif controles == False:
        return jsonify({"mensaje": "Internal Error"})
    else:
        return jsonify({"controles": {}})

# ENDPOINT eliminar control - http://127.0.0.1:5000/controles
@controles_bp.route('/controles', methods=["DELETE"]) #CHEQUEADO
def eliminar_control():
    # variable donde vamos a almacenar el id del control que queremos eliminar
    arg_id_control = request.args.get('id_control')

    if controller_controles.eliminar_control(arg_id_control):
        return jsonify({"mensaje": "Control Eliminado"})
    return jsonify({"mensaje": "Internal Error"})

# ENDPOINT editar control - http://127.0.0.1:5000/controles
@controles_bp.route('/controles', methods=["PUT"]) #CHEQUEADO
def editar_control():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_control = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    fecha_control = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05
    valor_glicemia = datos_control["valor_glicemia"]
    valor_insulina = datos_control["valor_insulina"]
    comida = datos_control["comida"]
    comentario_control = datos_control["comentario_control"]

    # Recibimos el id_control como argumento para seleccionar cual queremos editar
    arg_id_control = request.args.get('id_control')

    if controller_controles.editar_control(arg_id_control, fecha_control, valor_glicemia, valor_insulina, comida, comentario_control):
        nuevo_control = controller_controles.obtener_control_by_id(arg_id_control)
        return jsonify({"Control editado con exito": nuevo_control})
    return jsonify({"mensaje": "Internal Error."})

# ENDPOINT obtener rango de tiempo para imprimir controles en la DB - http://127.0.0.1:5000/controles
def imprimir_control():
    pass