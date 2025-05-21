from typing import Dict, List
from src.drivers.interfaces.numpy_handler_interface import DriverHandlingInterface


class Calculator3:
    def __init__(self, driver_numpy: DriverHandlingInterface) -> None:
        self.__driver_numpy = driver_numpy

    def calculate(self, request: Dict) -> Dict:
        data = request.json
        numbers_list = self.__validate_input(data)

        variance = self.__get_variance(numbers_list)
        multiplication = self.__get_multiplication(numbers_list)
        self.__validate_rule(variance, multiplication)

        return self.__format_result()

    def __validate_input(self, data: Dict) -> List[float]:
        if 'numbers' not in data:
            raise Exception('Valor invalido')

        list_numbers_float = [float(n) for n in data['numbers']]
        return list_numbers_float

    def __get_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_numpy.variance(numbers)

        return round(variance, 2)

    def __get_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for n in numbers:
            multiplication *= n

        return multiplication

    def __validate_rule(self, variance: float, multiplication: float) -> None:
        if variance > multiplication:
            raise Exception('Falha')

    def __format_result(self) -> Dict:
        response = {
            "calculator_type": "Calculator3",
            "result": "Deu tudo certo"
        }

        return response
