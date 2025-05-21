from src.main.tests.mocks.mock_request_calculator_2 import MockRequestCalculator2
from src.main.factory.calculator3_factory import calculator3_factory
import pytest


mock_request = MockRequestCalculator2(body={'numbers': [3, 5, 6]})


def test_format():
    calculator = calculator3_factory()
    response = calculator.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_result():
    calculator = calculator3_factory()
    response = calculator.calculate(mock_request)

    assert response['calculator_type'] == 'Calculator3'
    assert response['result'] == 'Deu tudo certo'


def test_error_rule():
    mock_error = MockRequestCalculator2(body={'numbers': [1, 50, 600]})
    calculator = calculator3_factory()

    with pytest.raises(Exception) as excinfo:
        calculator.calculate(mock_error)

    assert str(excinfo.value) == 'Falha'


def test_error():
    mock_error = MockRequestCalculator2(body={'numb': [1, 50, 600]})
    calculator = calculator3_factory()

    with pytest.raises(Exception) as excinfo:
        calculator.calculate(mock_error)

    assert str(excinfo.value) == 'Valor invalido'
