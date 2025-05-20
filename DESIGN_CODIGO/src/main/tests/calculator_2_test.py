from src.calculators.calculator_2 import Calculator2
from src.main.tests.mocks.mock_request_calculator_2 import MockRequestCalculator2
import pytest


mock_request = MockRequestCalculator2(body={'numbers': [3, 5, 6]})


def test_format():
    calculator_instance = Calculator2()
    response = calculator_instance.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_results():
    calculator_instance = Calculator2()
    response = calculator_instance.calculate(mock_request)

    assert response['calculator_type'] == 'Calculator2'
    assert response['result'] == 0.09


def test_error_handle():
    mock_request_error = MockRequestCalculator2(body={'num': [3, 5, 6]})
    calculator_instance = Calculator2()

    with pytest.raises(Exception) as excinfo:
        calculator_instance.calculate(mock_request_error)

    assert str(excinfo.value) == 'Valor invalido'
