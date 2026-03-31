# [TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)

# Tarefa: Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.
# Use: float(), sum(), len(), print()
# Sem alterar tupla.

nota1 = float(input("Digite a primeira nota: "))  # Lê a primeira nota do usuário
nota2 = float(input("Digite a segunda nota: "))  # Lê a segunda nota
nota3 = float(input("Digite a terceira nota: "))  # Lê a terceira nota
tupla_notas = (nota1, nota2, nota3)  # Cria uma tupla com as três notas
media = sum(tupla_notas) / len(tupla_notas)  # Calcula a média das notas usando sum() e len()
print("Tupla de notas:", tupla_notas)  # Exibe a tupla de notas
print(f"A média das notas é: {media:.2f}")  # Exibe a média das notas formatada com 2 casas decimais
