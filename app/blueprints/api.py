from flask import Blueprint, jsonify


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    # delete(Object.query.get(id))
    return jsonify({"status": True})


@bp.route('/', methods=['PUT'])
def add(id):
    # insert(Object(params))
    return jsonify({"status": True})


@bp.route('/<int:id>', methods=['GET'])
def get(id):
    # Object.query.get(id)
    return jsonify({"status": True})
