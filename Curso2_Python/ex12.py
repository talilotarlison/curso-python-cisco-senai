# Explicação:

# assert: É usado para verificar se uma condição é verdadeira. Se for falsa, o Python irá gerar uma exceção AssertionError, interrompendo a execução do programa.

# var != 0: A condição que está sendo verificada. Neste caso, ele está verificando se a variável var não é igual a 0.

# Funcionamento:

# Se var != 0 for verdadeiro, o programa continuará sua execução normalmente.

# Se var != 0 for falso (ou seja, se var for igual a 0), o Python levantará uma exceção AssertionError, e o programa será interrompido, a menos que a exceção seja tratada.

var = 0
assert var != 0  # Vai gerar um erro porque var é igual a 0

var = 5
assert var != 0  # Vai passar, porque var não é 0
print("Tudo certo!")

