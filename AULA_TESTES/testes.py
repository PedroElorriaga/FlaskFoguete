from codigos import fizz_buzz


def test_unitario_fizz_buzz_retorna_fizz():
    # 4 FASES -> SetUp / Exercise / Verify / TearDown

    # SetUp
    valor_do_input = 3
    retorno_esperado = 'Fizz'

    # Exercise
    resultado = fizz_buzz(valor_do_input)

    # Verify
    assert resultado == retorno_esperado


def test_unitario_fizz_buzz_retorna_buzz():
    # 4 FASES -> SetUp / Exercise / Verify / TearDown

    # SetUp
    valor_do_input = 5
    retorno_esperado = 'Buzz'

    # Exercise
    resultado = fizz_buzz(valor_do_input)

    # Verify
    assert resultado == retorno_esperado


def test_unitario_fizz_buzz_retorna_fizzbuzz():
    # 4 FASES -> SetUp / Exercise / Verify / TearDown

    # SetUp
    valor_do_input = 0
    retorno_esperado = 'FizzBuzz'

    # Exercise
    resultado = fizz_buzz(valor_do_input)

    # Verify
    assert resultado == retorno_esperado


def test_unitario_fizz_buzz_retorna_valor_do_input():
    # 4 FASES -> SetUp / Exercise / Verify / TearDown

    # SetUp
    valor_do_input = 1
    retorno_esperado = valor_do_input

    # Exercise
    resultado = fizz_buzz(valor_do_input)

    # Verify
    assert resultado == retorno_esperado
