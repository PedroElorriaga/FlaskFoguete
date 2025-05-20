from typing import Dict, List
from src.drivers.interfaces.numpy_handler_interface import DriverHandlingInterface


class Calculator2:
    def __init__(self, driver_numpy: DriverHandlingInterface) -> None:
        self.__driver_numpy = driver_numpy

    def calculate(self, request: Dict) -> Dict:
        data = request.json
        numbers_list = self.__validate_input(data)

        first_operation = self.__multiplicate_number(numbers_list)
        second_operation = self.__value_inverse(first_operation)

        return self.__format_result(second_operation)

    def __validate_input(self, data: Dict) -> List[float]:
        if 'numbers' not in data:
            raise Exception('Valor invalido')

        list_formated_float = []
        for n in data['numbers']:
            list_formated_float.append(float(n))

        return list_formated_float

    def __multiplicate_number(self, numbers: List[float]) -> List[float]:
        list_multiplicated_numbers = []
        for n in numbers:
            list_multiplicated_numbers.append((n*11) ** 0.95)

        return list_multiplicated_numbers

    def __value_inverse(self, numbers: List[float]) -> float:
        inverse_value = 1/self.__driver_numpy.standard_deviation(numbers)

        return inverse_value

    def __format_result(self, result: float) -> Dict:
        response = {
            "calculator_type": "Calculator2",
            "result": round(result, 2)
        }

        return response
