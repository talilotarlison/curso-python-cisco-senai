numbers = [i * i for i in range(5)]  # Cria a lista [0, 1, 4, 9, 16]
foo = list(filter(lambda x: x < 10, numbers))  # Filtra números menores que 10
print(foo)



numbers = [i * i for i in range(5)]  # Cria a lista [0, 1, 4, 9, 16]
foo = numbers[1::2]  # Pega os elementos nos índices ímpares: [1, 9]
print(foo)
