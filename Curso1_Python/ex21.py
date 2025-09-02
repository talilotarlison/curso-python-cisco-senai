# Dicionário de informações de uma pessoa
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "Lisboa"
}

# Dicionário com diferentes tipos de valores
cadastro_produtos = {
    "id_produto_1": {"nome": "Teclado", "preco": 50.00},
    "id_produto_2": {"nome": "Mouse", "preco": 25.00}
}

print(pessoa) # Saída: {'nome': 'Carlos', 'idade': 30, 'cidade': 'Lisboa'}
print(cadastro_produtos) # Saída: {'id_produto_1': {'nome': 'Teclado', 'preco': 50.0}, 'id_produto_2': {'nome': 'Mouse', 'preco': 25.0}}

# Acessando um valor usando sua chave
print(pessoa["nome"]) # Saída: Carlos