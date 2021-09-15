from flask import Flask

from resources.usuarios import usuarios_bp
from resources.recetas import recetas_bp
from resources.noticias import noticias_bp
from resources.controles import controles_bp
from resources.lugares import lugares_bp

# Creamos la app Flask
app = Flask(__name__)

# --------------------------------HOMEPAGE--------------------------------

# ENDPOINT homepage
@app.route('/')
def home():
    return "<h1>ACA VA LA HOMEPAGE</h1>"


# --------------------------------USUARIOS--------------------------------

# Importamos las rutas de la seccion usuarios como blueprint creados en resources/
app.register_blueprint(usuarios_bp)

# --------------------------------RECETAS--------------------------------

# Importamos las rutas de la seccion recetas como blueprint creados en resources/
app.register_blueprint(recetas_bp)


# --------------------------------NOTICIAS--------------------------------

# Importamos las rutas de la seccion noticias como blueprint creados en resources/
app.register_blueprint(noticias_bp)


# --------------------------------CONTROLES (solo con usuario logeado)--------------------------------

# Importamos las rutas de la seccion controles como blueprint creados en resources/
app.register_blueprint(controles_bp)

# --------------------------------LUGARES--------------------------------

# Importamos las rutas de la seccion lugares como blueprint creados en resources/
app.register_blueprint(lugares_bp)


# Inicializacion de la app como main, metodo debug=True para actualizacion automatica
if __name__ == "__main__":
    app.run(debug=True)