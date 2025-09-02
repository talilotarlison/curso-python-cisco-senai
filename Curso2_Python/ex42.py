#ex1

# Função que soma dois números:

soma = lambda x, y: x + y
print(soma(2, 3))  # saída: 5


# Função que verifica se um número é par:

par = lambda n: n % 2 == 0
print(par(4))  # saída: True
print(par(5))  # saída: False


# Usando com map:

my_list = [1, 2, 3]
# Insira a linha de código aqui.
print(foo)


numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # saída: [1, 4, 9, 16]


# Usando com filter:

numeros = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # saída: [2, 4]


#ex2

my_list = [1, 2, 3]
# Insira a linha de código aqui.
# print(foo)

# Copiar a lista inteira:

foo = my_list[:]
print(foo)  # saída: [1, 2, 3]


# Criar uma lista com valores multiplicados por 2:

foo = [x*2 for x in my_list]
print(foo)  # saída: [2, 4, 6]


# Somar todos os elementos da lista:

foo = sum(my_list)
print(foo)  # saída: 6


# Obter apenas os elementos pares:

foo = [x for x in my_list if x % 2 == 0]
print(foo)  # saída: [2]

#ex3

foo = list(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)

#  Saída: [2, 3, 4, 5, 6]

#ex4
def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x, end='')

#ex5
def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='');

#ex 6
def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

# ex 7

import os
import errno

try:
    os.makedirs("meu_diretorio")
except OSError as e:
    if e.errno == errno.EEXIST:
        print("O diretório já existe!")
    else:
        raise
# ex8

b = bytearray(3)
print(b)

#ex 9
import os

os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd())

# ex10

import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())

# ex11
import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())

# ex12
import os

os.mkdir('thumbnails')     # cria o diretório "thumbnails" no diretório atual
os.chdir('thumbnails')     # muda o diretório de trabalho para "thumbnails"

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)         # cria diretórios "small", "medium" e "large" dentro de "thumbnails"

print(os.listdir())        # lista todos os arquivos e pastas no diretório atual

# ex13

from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)

# ex14 
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

# ex15

import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")


