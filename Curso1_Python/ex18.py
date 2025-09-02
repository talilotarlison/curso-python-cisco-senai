produtos = [("Arroz", 20), ("Feijão", 10), ("Carne", 30)]
ordenado = sorted(produtos, key=lambda item: item[1])
print(ordenado)
# Saída: [('Feijão', 10), ('Arroz', 20), ('Carne', 30)]
