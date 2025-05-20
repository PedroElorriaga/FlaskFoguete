from flask import Blueprint, jsonify, request
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

calculators_route_2 = Blueprint('calculator2', __name__)


@calculators_route_2.route('/calculate', methods=['POST'])
def calculate():
    try:
        np_handler = NumpyHandler()
        calculator_instance = Calculator2(np_handler)
        response = calculator_instance.calculate(request)
    except Exception as excinfo:
        return jsonify({
            "success": False,
            "response": str(excinfo)
        })

    return jsonify({
        "success": True,
        "response": response
    })
