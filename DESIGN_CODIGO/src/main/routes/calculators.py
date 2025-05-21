from flask import Blueprint, jsonify, request
from src.main.factory.calculator1_factory import calculator1_factory
from src.main.factory.calculator2_factory import calculator2_factory
from src.main.factory.calculator3_factory import calculator3_factory

calculators_route = Blueprint('calculator', __name__)


@calculators_route.route('/1/calculate', methods=['POST'])
def calculate1():
    try:
        calculator = calculator1_factory()
        response = calculator.calculate(request)
    except Exception as excinfo:
        return jsonify({
            "success": False,
            "response": str(excinfo)
        })

    return jsonify({
        "sucess": True,
        "response": response
    })


@calculators_route.route('/2/calculate', methods=['POST'])
def calculate2():
    try:
        calculator = calculator2_factory()
        response = calculator.calculate(request)
    except Exception as excinfo:
        return jsonify({
            "success": False,
            "response": str(excinfo)
        })

    return jsonify({
        "success": True,
        "response": response
    })


@calculators_route.route('/3/calculate', methods=['POST'])
def calculate3():
    try:
        calculator = calculator3_factory()
        response = calculator.calculate(request)
    except Exception as excinfo:
        return jsonify({
            "success": False,
            "response": str(excinfo)
        })

    return jsonify({
        "success": True,
        "response": response
    })
