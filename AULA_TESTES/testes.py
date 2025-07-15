import pytest

from unittest.mock import MagicMock, patch
from codigos import fizz_buzz, CardTask, CardMutations, DataBaseSimulation, api_simulation


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


@pytest.fixture
def mock_conexao() -> MagicMock:
    cursor = MagicMock()
    cursor.execute().fetchone.return_value = {
        'id': 1, 'produto': 'Ficticio', 'valor': 99.90}
    conexao = MagicMock()
    conexao.cursor.return_value = cursor

    return conexao


def test_unitario_buscar_dado_na_base_de_dados(mock_conexao):
    # SetUp
    resultado_esperado = {'id': 1, 'produto': 'Ficticio', 'valor': 99.90}
    id_produto = 1

    # Exercise
    db_simulador = DataBaseSimulation(conexao_sqlite=mock_conexao)
    resposta = db_simulador.get_card(id_produto)

    assert resposta == resultado_esperado
    # FOI CHAMADO ESSA REQUISIÇÃO ?
    mock_conexao.cursor().execute.assert_called_with(
        "SELECT * FROM produtos WHERE id=?", (id_produto)
    )
    # FOI CHAMADO ESSA FUNÇÃO EXECUTE ?
    mock_conexao.cursor().execute.assert_called()


@pytest.fixture
def mock_request() -> MagicMock:
    resposta = MagicMock()
    resposta.status_code = 200
    resposta.json.return_value = {
        "cep": "06449-410",
        "logradouro": "Rua Urânia",
        "complemento": "",
        "unidade": "",
        "bairro": "Parque Viana",
        "localidade": "Barueri",
        "uf": "SP",
        "estado": "São Paulo",
        "regiao": "Sudeste",
        "ibge": "3505708",
        "gia": "2069",
        "ddd": "11",
        "siafi": "6213"
    }

    return resposta


@patch('requests.get')
# A ordem dos parâmetros é invertida: o último patch vem como primeiro argumento.
# Não foi utilizada nesse caso a ordem dos parametros invertidos
def test_unitario_cep_api(mock_get, mock_request):
    # SetUp
    mock_get.return_value = mock_request
    resultado_esperado = {
        "cep": "06449-410",
        "logradouro": "Rua Urânia",
        "complemento": "",
        "unidade": "",
        "bairro": "Parque Viana",
        "localidade": "Barueri",
        "uf": "SP",
        "estado": "São Paulo",
        "regiao": "Sudeste",
        "ibge": "3505708",
        "gia": "2069",
        "ddd": "11",
        "siafi": "6213"
    }
    cep_input = '06449410'

    # Exercise
    resposta = api_simulation(cep_input)

    assert resposta == resultado_esperado
