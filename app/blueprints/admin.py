from flask import Blueprint, render_template
from flask_security import roles_required, auth_required, current_user

bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../templates/admin')


@bp.route('/')
@auth_required()
@roles_required("admin")
def index():
    return render_template("acceuil.html.twig")
