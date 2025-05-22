from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler


def calculator4_factory():
    np_handler = NumpyHandler()
    calculator_instance = Calculator4(np_handler)

    return calculator_instance
