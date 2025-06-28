from unittest.mock import Mock

meu_dado_mockado = Mock()
print(meu_dado_mockado)  # Retorna um ID diferente toda vez em que é chamado

meu_dado_mockado.return_value = 'Qualquer coisa'
print(meu_dado_mockado.return_value)  # Retorna 'Qualquer coisa'

# Carrega um metodo com o seguinte valor '44'
meu_dado_mockado.qualquer_metodo.return_value = 44
valor = meu_dado_mockado.qualquer_metodo()
print(valor)  # Retorna 44

print(dir(meu_dado_mockado))  # Mostra os atributos e metodos do objeto
