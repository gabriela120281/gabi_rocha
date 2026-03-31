# [LIST] Atualizar elemento com uma operação
# Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

numeros = []  # Cria uma lista vazia para armazenar os números
numeros.append(int(input("Digite o primeiro número inteiro: ")))  # Lê o primeiro número inteiro e adiciona à lista
numeros.append(int(input("Digite o segundo número inteiro: ")))  # Lê o segundo número inteiro e adiciona à lista
numeros.append(int(input("Digite o terceiro número inteiro: ")))  # Lê o terceiro número inteiro e adiciona à lista
numeros[2] = numeros[0] + numeros[1]  # Atualiza    o último elemento da lista para a soma dos dois primeiros
print("Lista atualizada:", numeros)  # Exibe a lista atualizada 



