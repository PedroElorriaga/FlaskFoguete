from src.tests.mocks.mock_request import MockRequest
from src.calculators.calculator_1 import Calculator1
import pytest


def test_format():
    mock_request = MockRequest(body={'number': 3.0})
    calculator_instance = Calculator1()

    response = calculator_instance.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_results():
    mock_request = MockRequest(body={'number': 3.0})
    calculator_instance = Calculator1()

    response = calculator_instance.calculate(mock_request)

    assert response['result'] == 15.71
    assert response['calculator_type'] == 'Calculator1'


def test_error_handle():
    mock_request = MockRequest(body={'number': 3})
    calculator_instance = Calculator1()

    with pytest.raises(Exception) as excinfo:
        calculator_instance.calculate(mock_request)

    assert str(excinfo.value) == 'Valor invalido'
