import random

# randrange: gera um número aleatório entre 1 e 10
a = random.randrange(1, 11)

# random: gera um número de ponto flutuante entre 0 e 1, multiplicado por 100 para obter um valor inteiro
b = int(random.random() * 100)

# choice: escolhe aleatoriamente entre 0 e 1
c = random.choice([0, 1])

print(a, b, c)


import random

a = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
b = random.randint(80, 90)  # Gera um número aleatório entre 80 e 90
c = random.randint(0, 1)   # Gera um número aleatório entre 0 e 1

print(a, b, c)
