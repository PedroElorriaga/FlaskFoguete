from typing import Dict


class Calculator1:
    def calculate(self, request: Dict) -> Dict:
        data = request.json
        input_data = self.__validate_input(data)

        number_part = input_data / 3
        first_operation = self.__fisrt_operation(number_part)
        second_operation = self.__second_operation(number_part)
        result = first_operation + second_operation + number_part

        return self.__format_result(result)

    def __validate_input(self, data) -> float:
        if 'number' not in data or type(data['number']) != float:
            raise Exception('Valor invalido')

        return data['number']

    def __fisrt_operation(self, number: float) -> float:
        result = (((number / 4) + 7) ** 2) * 0.257

        return result

    def __second_operation(self, number: float) -> float:
        result = ((number ** 2.121) / 5) + 1

        return result

    def __format_result(self, result: float) -> Dict:
        response = {
            "calculator_type": "Calculator1",
            "result": round(result, 2)
        }

        return response
