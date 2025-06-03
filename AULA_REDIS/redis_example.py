import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# DAR UM INSERT
r.set('chave_1', 'Dados da chave 1')

# DAR UM SELECT (Usamos o decode porque o arquivo vem em bytes)
meu_dado = r.get('chave_1').decode('utf-8')

# DAR UM DELETE
r.delete('chave_1')

print(meu_dado)  # OUTPUT Dados da chave 1

# COMANDOS PARA HASH (Tipo um dicionario)
r.hset('hash_1', 'nome', 'Pedro')
r.hset('hash_1', 'idade', '22')
r.hset('hash_1', 'peso', '78')
r.hset('hash_1', 'altura', '1.75')

todo_dado = r.hgetall('hash_1')
# OUTPUT {b'nome': b'Pedro', b'idade': b'22', b'peso': b'78', b'altura': b'1.75'}
print(todo_dado)

um_dado = r.hget('hash_1', 'nome').decode('utf-8')
print(um_dado)  # OUTPUT Pedro

# BUSCAR POR EXISTENCIA
elem = r.exists('chave_1')
print(elem)  # OUTPUT 0 = NAO EXISTE

elem2 = r.hexists('hash_1', 'nome')
print(elem2)  # OUTPUT True

# EXPIRACAO DE DADOS TTL (Time To Live)
r.set('chave_delete', 'Esse dados vai ser deletado em 10 segundos', 10)
r.expire('hash_1', 15)
