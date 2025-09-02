import sys

# Imprime mensagem de erro no stderr
sys.stderr.write("Este é um erro!\n")

# Imprime uma mensagem normal no stdout
print("Esta é uma saída normal.")


import sys
sys.stderr = open('erros.log', 'w')
sys.stderr.write("Este é um erro que vai para um arquivo.\n")

import sys

# Redireciona stderr para um arquivo
sys.stderr = open('erros.log', 'w')
sys.stderr.write("Mensagem de erro para o arquivo.")

