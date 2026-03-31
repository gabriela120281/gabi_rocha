# [LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

# Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
# Tipos: float, list.
# Conceitos: mutabilidade, ordenação in-place, média aritmética.

nota = []
nota.append(float(input("Digite a primeira nota: ")))
nota.append(float(input("Digite a segunda nota: ")))
nota.append(float(input("Digite a terceira nota: ")))
media = sum(nota) / len(nota)
print(f"A média das notas é: {media:.2f}")

menor_nota = min(nota)
nova_nota = float(input("Digite a nova nota para substituir a menor: "))
index_menor = nota.index(menor_nota)
nota[index_menor] = nova_nota
nota.sort()
nova_media = sum(nota) / len(nota)
print(f"As notas ordenadas são: {nota}")
print(f"A nova média das notas é: {nova_media:.2f}")

