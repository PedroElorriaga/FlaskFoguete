from src.main.tests.mocks.mock_request_calculator_2 import MockRequestCalculator2
from src.main.factory.calculator2_factory import calculator2_factory
import pytest


mock_request = MockRequestCalculator2(body={'numbers': [3, 5, 6]})


def test_format():
    calculator = calculator2_factory()
    response = calculator.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_results():
    calculator = calculator2_factory()
    response = calculator.calculate(mock_request)

    assert response['calculator_type'] == 'Calculator2'
    assert response['result'] == 0.09


def test_error_handle():
    mock_request_error = MockRequestCalculator2(body={'num': [3, 5, 6]})
    calculator = calculator2_factory()

    with pytest.raises(Exception) as excinfo:
        calculator.calculate(mock_request_error)

    assert str(excinfo.value) == 'Valor invalido'
