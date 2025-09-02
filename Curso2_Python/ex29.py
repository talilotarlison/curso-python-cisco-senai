# Abrindo um arquivo para leitura
with open('exemplo.txt', 'r') as s:
    q = s.read(1)
    print(q)



for x in open('file', 'rt'):
    print(x)

# Abrindo um arquivo para leitura binária
with open('file.bin', 'rb') as f:
    # Lendo os dados do arquivo em blocos e preenchendo a matriz de bytes
    byte_data = bytearray(f.read())  # Lê tudo e armazena como um bytearray

print(byte_data)  # Exibe o conteúdo lido em bytes
