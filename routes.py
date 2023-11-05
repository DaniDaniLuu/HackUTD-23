from flask import Blueprint, request, jsonify

calc_bp = Blueprint('calc', __name__)


@bp.route('/calc')
def index():
    return "Welcome to the API!"

@bp.route('/user/xxx')
def 


@bp.route('/post/xxx')