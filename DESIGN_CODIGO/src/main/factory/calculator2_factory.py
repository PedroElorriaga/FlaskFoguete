from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler


def calculator2_factory():
    np_handler = NumpyHandler()
    calculator_instance = Calculator2(np_handler)
    return calculator_instance
