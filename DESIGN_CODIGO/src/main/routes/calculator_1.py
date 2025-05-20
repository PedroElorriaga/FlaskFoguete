from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calculators_route_1 = Blueprint('calculator1', __name__)


@calculators_route_1.route('/test', methods=['POST'])
def testing_host():
    return jsonify({
        "success": True
    })


@calculators_route_1.route('/calculate', methods=['POST'])
def calculate():
    try:
        calculator_instance = Calculator1()
        response = calculator_instance.calculate(request)
    except Exception as excinfo:
        return jsonify({
            "success": False,
            "response": str(excinfo)
        })

    return jsonify({
        "sucess": True,
        "response": response
    })
