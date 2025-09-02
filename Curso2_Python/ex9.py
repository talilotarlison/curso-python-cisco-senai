def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2  # Calcula o índice do meio
        
        if vetor[meio] == valor:
            return meio  # Valor encontrado, retorna o índice
        
        elif vetor[meio] < valor:
            inicio = meio + 1  # O valor está na metade direita, ajusta o índice do início
        
        else:
            fim = meio - 1  # O valor está na metade esquerda, ajusta o índice do fim
    
    return -1  # Valor não encontrado, retorna -1
