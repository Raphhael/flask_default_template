from flask import Blueprint, render_template

bp = Blueprint('public', __name__, url_prefix='/', template_folder='../templates/public')


@bp.route('/')
def accueil():
    return render_template("accueil.html.twig")
