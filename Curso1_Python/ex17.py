# Verifica se a pessoa precisa fazer curso teórico ou prático

fez_teorico = input("Você já fez o curso teórico? (sim/não): ")
fez_pratico = input("Você já fez o curso prático? (sim/não): ")

if fez_teorico.lower() == "sim" or fez_pratico.lower() == "sim":
    print(" Você já iniciou o processo de habilitação.")
else:
    print(" Você ainda não iniciou o processo de habilitação.")
