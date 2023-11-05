from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return "Welcome to the API!"

@bp.route('/user/xxx')
def 


@bp.route('/post/xxx')