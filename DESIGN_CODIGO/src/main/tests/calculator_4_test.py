from src.factory.calculator4_factory import calculator4_factory
from src.main.tests.mocks.mock_request_calculator_2 import MockRequestCalculator2
import pytest

mock_request = MockRequestCalculator2(body={'numbers': [8, 7.5, 10, 9, 6.5]})


def test_format():
    calculator = calculator4_factory()
    response = calculator.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_format():
    calculator = calculator4_factory()
    response = calculator.calculate(mock_request)

    assert response['calculator_type'] == 'Calculator4'
    assert response['result'] == 8.2


def test_error():
    mock_error = MockRequestCalculator2(body={'num': [1, 2, 3]})
    calculator = calculator4_factory()

    with pytest.raises(Exception) as excinfo:
        calculator.calculate(mock_error)

    assert str(excinfo.value) == 'Valor invalido'
