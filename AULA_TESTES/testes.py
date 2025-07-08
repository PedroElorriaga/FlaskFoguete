from codigos import fizz_buzz, CardTask, CardMutations


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


def test_unitario_card_task_setup():
    # SetUp
    tarefa_id = 1
    tarefa = 'Temperar frango'
    status = 'Fazendo'

    # Exercise
    card = CardTask(tarefa_id, tarefa, status)

    # Verify
    assert card.id == tarefa_id
    assert card.tarefa == tarefa
    assert card.status == status


def test_unitario_criar_tarefa():
    # SetUp
    tarefa = 'Temperar frango'
    status = 'Fazendo'

    # Exercise
    card_mutation = CardMutations()
    resposta = card_mutation.create_task(tarefa, status)

    assert resposta.tarefa == tarefa
    assert resposta.status == status


def test_unitario_listar_tarefas():
    # SetUp
    tarefa = 'Temperar frango'
    status = 'Fazendo'

    # Exercise
    card_mutation = CardMutations()
    card_mutation.create_task(tarefa, status)
    resposta = card_mutation.list_tasks()

    assert len(resposta) > 0
    assert isinstance(resposta, list)


def test_unitario_atualizar_uma_tarefa():
    # SetUp
    tarefa = 'Temperar frango'
    status = 'Fazendo'
    data = {'id': 1, 'status': 'Feito'}

    # Exercise
    card_mutation = CardMutations()
    card_mutation.create_task(tarefa, status)
    resposta = card_mutation.update_task(data)

    assert isinstance(resposta, CardTask)
    assert resposta.id == data['id']


def test_unitario_atualizar_uma_tarefa_nao_existente():
    # SetUp
    data = {'id': 10, 'status': 'Feito'}

    # Exercise
    card_mutation = CardMutations()
    resposta = card_mutation.update_task(data)

    assert resposta == None
