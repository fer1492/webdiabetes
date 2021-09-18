from flask import Blueprint, render_template

views_bp = Blueprint('routes-views', __name__)

# ENDPOINT template homepage
@views_bp.route('/home')
def home():
    return render_template("home.html", username="FULANITO89")
