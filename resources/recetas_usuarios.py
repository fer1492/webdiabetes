from flask import request, jsonify, Blueprint
from datetime import datetime

from modelos import controller_recetas_usuarios, controller_usuarios, controller_recetas

# Configuracion del Objeto blueprint con las rutas de recetas_usuarios
recetas_usuarios_bp = Blueprint('routes-recetas_usuarios', __name__)

# ENDPOINT crear receta favorita - http://127.0.0.1:5000/recetas_usuarios
@recetas_usuarios_bp.route('/recetas_usuarios', methods=["POST"])
def crear_receta_favorita():
    # Acceso a los parametros que van a ingresar los usuarios con request en formato json (diccionario)
    datos_receta = request.get_json()
    # Asignamos valores a las variables para la funcion por intermedio del valor json diccionario
    fecha_receta_usuario = datetime.now().strftime("%x %X")  # formato time: 5/22/2021 10:24:05
    favorito = datos_receta['favorito'] # DEFAULT 0 = no favorito | 1 = favorito

    # Argumentos que voy a soliciar a las tablas para completar id_receta e id_usuario
    # arg_id_receta = request.args.get('id_receta')
    # arg_id_usuario = request.args.get('id_usuario')

    if controller_recetas_usuarios.crear_receta_favorita(fecha_receta_usuario, favorito, 2, 1):
        # fav_receta = controller_recetas.obtener_receta_by_id(arg_id_receta)
        # fav_usuario = controller_usuarios.obtener_usuario_by_id(arg_id_usuario)
        # return jsonify{"mensaje": f"Receta: {fav_receta} agregada en favoritos por el usuario: {fav_usuario}"})
        return jsonify({"GOLAZO"})
    return jsonify({"mensaje": "Internal Error"})