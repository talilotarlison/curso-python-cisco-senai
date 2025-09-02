import numpy as np

# Definindo o número de linhas e colunas
num_linhas = 5
num_colunas = 10

# Criando a matriz 2D de bytes
matriz_bytes = np.zeros((num_linhas, num_colunas), dtype=np.uint8)

# Abrindo um arquivo para leitura binária
with open('file.bin', 'rb') as f:
    dados = f.read(num_linhas * num_colunas)  # Lê o número necessário de bytes

    # Preenchendo a matriz com os dados lidos
    for i in range(num_linhas):
        matriz_bytes[i] = list(dados[i*num_colunas:(i+1)*num_colunas])

print(matriz_bytes)
