from collections import defaultdict

# Dados de entrada
dados = [
    "hello world",
    "hello",
    "hello map reduce",
    "world of map reduce"
]

# Função Map: separa cada palavra e associa o valor 1 para contagem
def map_func(dados):
    result = []
    for frase in dados:
        for palavra in frase.split():
            result.append((palavra, 1))
    return result

# Função Reduce: soma o valor de cada palavra para contar as ocorrências
def reduce_func(mapped_data):
    resultado = defaultdict(int)
    for palavra, contagem in mapped_data:
        resultado[palavra] += contagem
    return resultado

# Passo 1: Aplicar o Map
mapped_data = map_func(dados)

# Passo 2: Aplicar o Reduce
reduced_data = reduce_func(mapped_data)

print("Contagem de palavras:", dict(reduced_data))
