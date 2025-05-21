import numpy
from typing import List
from .interfaces.numpy_handler_interface import DriverHandlingInterface


class NumpyHandler(DriverHandlingInterface):
    def __init__(self):
        self.__np = numpy

    # DESVIO PADRÃO (standard_deviation)
    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers, dtype=self.__np.float64)

    def med(self, numbers: List[float]) -> float:
        return self.__np.mean(numbers)
