# Outra  maneira de fazer busca linear:

def buscar(numero):

    numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
    
    numero_entrada =  numero;
    
    for numero in numeros:
        if numero_entrada == numero:
           print("numero ta nas lista");
        else:
            print("numero não ta nas lista");
buscar(31)