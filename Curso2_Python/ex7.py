#ORDENAÇÃO SIMPLES DE UMA LISTA DE 2 VALORES em python
#Usandoo variavel AUX

numeros = [55,12]

if numeros[0] > numeros[1]:
    aux = numeros[0]
    numeros[0] = numeros[1]
    numeros[1] = aux
    print(numeros)