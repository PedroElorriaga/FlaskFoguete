from src.main.tests.mocks.mock_request import MockRequest
from src.main.factory.calculator1_factory import calculator1_factory
import pytest


mock_request = MockRequest(body={'number': 3.0})


def test_format():
    calculator = calculator1_factory()

    response = calculator.calculate(mock_request)

    assert 'calculator_type' in response
    assert 'result' in response


def test_results():
    calculator = calculator1_factory()

    response = calculator.calculate(mock_request)

    assert response['result'] == 15.71
    assert response['calculator_type'] == 'Calculator1'


def test_error_handle():
    mock_request_error = MockRequest(body={'num': 3})
    calculator = calculator1_factory()

    with pytest.raises(Exception) as excinfo:
        calculator.calculate(mock_request_error)

    assert str(excinfo.value) == 'Valor invalido'
