# [TUPLE] Criar e exibir uma tupla simples

#Tarefa: Leia dois nomes do usuário e coloque-os em uma tupla. Depois exiba a tupla e o tipo dela.
# Orientações: 
 
# usar input(), print(), type()
 
# usar tupla no formato (valor1, valor2)
 
# tipo trabalhado: str, tuple

nome1 = input("Digite o primeiro nome: ")  # Lê o primeiro nome do usuário
nome2 = input("Digite o segundo nome: ")  # Lê o segundo nome do usuário
tupla_nomes = (nome1, nome2)  # Cria uma tupla com os dois nomes
print("Tupla de nomes:", tupla_nomes)  # Exibe a tupla de nomes
print("Tipo da tupla:", type(tupla_nomes))  # Exibe o tipo da tupla de nomes
