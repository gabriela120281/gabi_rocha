# [LIST] Remova um número se ele existir
'''Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
 Use: int(), input(), in, remove(), len(), print()
 Tipos: int, list.
 Conceitos: teste de pertencimento, tratamento simples de remoção, função len().
'''

lista = [1, 2, 3, 4]
a = 1
print("Antes da remoção:", len(lista))
lista.remove(a)
print("Depois da remoção:" , len(lista))


nome1= input("Informe o nome do seu pai: ")
nome2 = input("Informe o nome da sua mae: ")
nome3 = input("Informe o seu nome: ")
nome4 = input("Informe o nome da sua avó paterna: ")

lista_completa = [nome1, nome2, nome3, nome4]

print("Total da lista completa:" , len(lista_completa))
print("A lista completa é: ", (lista_completa))

lista_completa.remove(nome4)
print("Quantidade de nomes depois da remoção:", len(lista_completa))
print("A lista depois da remoção é:", lista_completa)









