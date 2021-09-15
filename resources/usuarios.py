from flask import request, jsonify, Blueprint
from datetime import datetime

import modelos
from modelos import controller_usuarios

# --------------------------------USUARIOS--------------------------------

# Configuracion del Objeto blueprint con las rutas de usuarios
usuarios_bp = Blueprint('routes-usuarios', __name__)

# ENDPOINT crear nuevo usuario - http://127.0.0.1:5000/usuarios
@usuarios_bp.route('/usuarios', methods=["POST"]) #CHEQUEADO
def crear_usuario():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_usuario = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    username = datos_usuario['username']
    mail = datos_usuario['mail']
    password = datos_usuario['password']
    fecha_usuario = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05

    # ejecutamos la funcion crear_usuario desde controller_usuarios
    nuevo_usuario = controller_usuarios.signup(username, mail, password, fecha_usuario)

    if nuevo_usuario:
        return jsonify({"mensaje": "Usuario creado con exito"})
    return jsonify({"mensaje": "Internal Error"})

# ENDPOINT obtener todos los usuarios de la tabla usuarios de la DB - http://127.0.0.1:5000/usuarios
@usuarios_bp.route('/usuarios', methods=["GET"]) #CHEQUEADO
def obtener_usuarios():
    # Obtenermos usuarios de invocar funcion obtener_usuarios en controller_usuarios
    usuarios = modelos.controller_usuarios.obtener_usuarios()

    if usuarios:
        return jsonify({"usuarios": usuarios})
    elif usuarios == False:
        return jsonify({"mensaje": "Internal Error"})
    else:
        return jsonify({"usuarios": {}})

# ENDPOINT obtener datos de usuario logeado - http://127.0.0.1:5000/usuarios
@usuarios_bp.route('/usuarios', methods=["GET"]) #CONSULTAR - IMPRIME TODOS LOS USUARIOS DEBERIA IMPRIMIR UNO SOLO
def obtener_usuario_by_id():
    # Recibimos el id_usuario como argumento para seleccionar cual queremos editar
    arg_id_usuario = request.args.get('id_usuario')

    # Obtenermos usuario de invocar funcion obtener_usuario_by_id en controller_usuarios
    seleccion_usuario = modelos.controller_usuarios.obtener_usuario_by_id(arg_id_usuario)

    if seleccion_usuario:
        return jsonify({"usuario": seleccion_usuario})
    elif seleccion_usuario == False:
        return jsonify({"mensaje": "Internal Error"})
    else:
        return jsonify({"usuarios": {}})

# ENDPOINT editar datos de perfil de usuario - http://127.0.0.1:5000/usuarios
@usuarios_bp.route('/usuarios', methods=["PUT"]) #CHEQUEADO - ACTUALIZA PERO ME DA EL ERROR DE SELECCIONAR BY ID
def editar_usuario():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_update_usuario = request.get_json()

    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    username = datos_update_usuario['username']
    mail = datos_update_usuario['mail']
    password = datos_update_usuario['password']
    foto_usuario = datos_update_usuario['foto_usuario']
    pais = datos_update_usuario['pais']
    fecha_usuario = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05

    # Recibimos el id_control como argumento para seleccionar cual queremos editar
    arg_id_usuario = request.args.get('id_usuario')

    if controller_usuarios.editar_usuario(arg_id_usuario, username, mail, password, foto_usuario, pais, fecha_usuario):
        nuevo_update = controller_usuarios.obtener_usuario_by_id(arg_id_usuario)
        return jsonify({"Usuario editado con exito": nuevo_update})
    return jsonify({"mensaje": "Internal Error"})
