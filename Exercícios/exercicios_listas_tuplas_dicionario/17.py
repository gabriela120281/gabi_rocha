# [TUPLE - desafio] Organizar valores sem mexer na tupla original

# Tarefa: Leia quatro números em uma tupla e exiba: 
# a tupla original
# uma lista ordenada apenas para visualização
# o tipo da variável ordenada
# Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

num1 = int(input("Digite o primeiro número inteiro: "))  # Lê o primeiro número inteiro
num2 = int(input("Digite o segundo número inteiro: "))  # Lê o segundo número inteiro
num3 = int(input("Digite o terceiro número inteiro: "))  # Lê o terceiro número inteiro
num4 = int(input("Digite o quarto número inteiro: "))  # Lê o quarto número inteiro
tupla_numeros = (num1, num2, num3, num4)  # Cria uma tupla com os quatro números inteiros
print("Tupla original:", tupla_numeros)  # Exibe a tupla original
lista_ordenada = sorted(tupla_numeros)  # Cria uma lista ordenada a partir da tupla usando sorted()
print("Lista ordenada:", lista_ordenada)  # Exibe a lista ordenada
print("Tipo da variável ordenada:", type(lista_ordenada))  # Exibe o tipo da variável ordenada (deve ser <class 'list'>)

