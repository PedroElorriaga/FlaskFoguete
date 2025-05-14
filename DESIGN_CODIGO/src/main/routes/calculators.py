from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calculators_route = Blueprint('calculator', __name__)


@calculators_route.route('/test', methods=['POST'])
def testing_host():
    return jsonify({
        "success": True
    })


@calculators_route.route('/calculate', methods=['POST'])
def calculate():
    calculator_instance = Calculator1()
    response = calculator_instance.calculate(request)
    return jsonify({
        "sucess": True,
        "response": response
    })
