from typing import Dict, List
from src.drivers.interfaces.numpy_handler_interface import DriverHandlingInterface


class Calculator4:
    def __init__(self, numpy_driver: DriverHandlingInterface):
        self.__numpy_driver = numpy_driver

    def calculate(self, request: Dict) -> Dict:
        data = request.json
        numbers_list = self.__validate_format(data)

        numbers_med = self.__get_med(numbers_list)

        return self.__format_response(numbers_med)

    def __validate_format(self, data: Dict) -> List[float]:
        if 'numbers' not in data:
            raise Exception('Valor invalido')

        list_numbers_float = [float(n) for n in data['numbers']]
        return list_numbers_float

    def __get_med(self, numbers: List[float]) -> float:
        return float(self.__numpy_driver.med(numbers))

    def __format_response(self, number: float) -> Dict:
        response = {
            "calculator_type": "Calculator4",
            "result": number
        }

        return response
