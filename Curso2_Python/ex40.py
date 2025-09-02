# ex1

from random import randint
    
for i in range(2):
   print(randint(1, 2), end='')
    
#ex2
try:
    x = 10 / 2  # Executado sem erro
    y = 10 / 0  # Levanta uma exceção
except ZeroDivisionError:
    print("Divisão por zero!")

# ex3
try:
    raise BaseException("Exceção de exemplo")
except BaseException as e:
    print(f"Caught exception: {e}")
#ex4

try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#  ex4

# UNICODE é um padrão:

# como o ASCII, mas muito mais expansivo.

# O Unicode é um sistema de codificação de caracteres que visa abranger todos os caracteres usados em todos os sistemas de escrita do mundo. Ele é muito mais expansivo que o ASCII, que é limitado a 128 caracteres. O Unicode, por sua vez, pode representar milhões de caracteres, cobrindo uma vasta gama de símbolos, alfabetos e até mesmo emojis.

# A principal diferença entre o Unicode e o ASCII é que o ASCII é limitado a caracteres básicos (como letras, números e pontuação) e usa 7 bits por caractere, enquanto o Unicode pode usar de 1 a 4 bytes para representar caracteres e pode acomodar praticamente todos os sistemas de escrita modernos e antigos.UNICODE é um padrão:

# como o ASCII, mas muito mais expansivo.

# O Unicode é um sistema de codificação de caracteres que visa abranger todos os caracteres usados em todos os sistemas de escrita do mundo. Ele é muito mais expansivo que o ASCII, que é limitado a 128 caracteres. O Unicode, por sua vez, pode representar milhões de caracteres, cobrindo uma vasta gama de símbolos, alfabetos e até mesmo emojis.

# A principal diferença entre o Unicode e o ASCII é que o ASCII é limitado a caracteres básicos (como letras, números e pontuação) e usa 7 bits por caractere, enquanto o Unicode pode usar de 1 a 4 bytes para representar caracteres e pode acomodar praticamente todos os sistemas de escrita modernos e antigos.

# ex5
x = '\''
print(len(x))

# ex6
print(ord('c') - ord('a'))

# ex7

print(chr(ord('z') ‑ 2))

# ex8

print(3 * 'abc' + 'xyz')

# ex9
print('Mike' > "Mikey")

