from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


def calculator3_factory():
    np_handler = NumpyHandler()
    calculator_instance = Calculator3(np_handler)
    return calculator_instance
