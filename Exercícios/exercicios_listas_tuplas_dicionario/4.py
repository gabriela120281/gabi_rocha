
# 4 [LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média
# Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
 # Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
 # Tipos: float, list.
 # Conceitos: mutabilidade, ordenação in-place, média aritmética.
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
notas = [nota1, nota2, nota3]
print(f"Notas: {notas}")
soma = sum(notas)
media_inicial = sum(notas) / len(notas)
print(f"Média: {media_inicial:.2f}")
menor_nota = min(notas)
indice_menor = notas.index(menor_nota)
nova_nota = float(input("Informe a nova nota para substituir a menor: "))
notas[indice_menor] = nova_nota
print(f"Notas atualizadas: {notas}")
notas.sort()
print("Notas ordenadas: ", notas)
media_final = sum(notas) / len(notas)
print(f"Nova média: {media_final:.2f}")