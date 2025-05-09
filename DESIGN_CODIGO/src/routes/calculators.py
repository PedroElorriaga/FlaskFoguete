from flask import Blueprint, jsonify

calculators_route = Blueprint('calculator', __name__)


@calculators_route.route('/test', methods=['POST'])
def testing_host():
    return jsonify({
        "success": True
    })
