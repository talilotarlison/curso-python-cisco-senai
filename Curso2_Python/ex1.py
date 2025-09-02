from random import randrange
# pedra  -> 2
# tesoura -> 1
# papel -> 0


print("##### JOGO JOKENPO EM PYTHON ####")
print("Escolha um numero de uma opção abaixo :")
print("[2] - Pedra")
print("[1] - Tesoura")
print("[0] - Papel")

options = ["papel", "tesoura", "pedra"];

maquina = randrange(0, 3)
jogador = int(input("Escolhar uma opção:\n"))


if options[jogador] == "pedra"  and options[maquina]== "papel":
    print(f"Voce perdeu!!, vc escolheu {options[jogador]} e a maquina escolheu {options[maquina]}!!")
elif options[jogador] == "papel"  and options[maquina]== "pedra":
    print(f"Voce Ganhou!!, vc escolheu {options[jogador]} e a maquina escolheu {options[maquina]}!!")
elif   jogador > maquina:
     print(f"Voce Ganhou!!, vc escolheu {options[jogador]} e a maquina escolheu {options[maquina]}!!")
elif   jogador < maquina:
     print(f"Voce perdeu!!, vc escolheu {options[jogador]} e a maquina escolheu {options[maquina]}!!")
else:
    print(f"Empatou!, vc escolheu {options[jogador]} e a maquina escolheu {options[maquina]}!!")