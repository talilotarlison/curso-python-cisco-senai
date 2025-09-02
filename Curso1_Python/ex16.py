# Verifica se a pessoa pode dirigir com base na idade e se tem carteira

idade = int(input("Digite sua idade: "))
tem_carteira = input("Você tem carteira de motorista? (sim/não): ")

if idade >= 18 and tem_carteira.lower() == "sim":
    print( "Você pode dirigir!")
else:
    print("Você NÃO pode dirigir.")
