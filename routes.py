from flask import Blueprint, request, jsonify

import data_analysis

calc_bp = Blueprint('calc', __name__)
analyze_bp = Blueprint('analyze', __name__)


@bp.route('/calc')
def index():
    return "Welcome to the API!"

# returns an array of the values we need to create a graph for approved factors.
@analyze_bp.route('/approvedgraph', methods=['GET'])
def approvedgraph():
    approval=True
    approvedarray = data_analysis.main(approval)
    data = {'array_data': approvedarray}
    return jsonify(data)

# returns an array of the values we need to create a graph for notapproved factors.
@analyze_bp.route('/notapprovedgraph', methods=['GET'])
def notapprovedgraph():
    approval=False
    notapprovedarray = data_analysis.main(approval)
    data = {'array_data': notapprovedarray}
    return jsonify(data)


