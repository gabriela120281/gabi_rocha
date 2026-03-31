# [TUPLE] Dias da semana com tuplas
# Tarefa: Crie uma tupla com os dias da semana. Depois, peça ao usuário para digitar um número de 1 a 7 e exiba o dia correspondente.
# Orientações:
# use indices para acessar os elementos da tupla (lembre-se que os índices começam em 0)
# use input() para ler o número do usuário e print() para exibir o resultado
# usar input(), print()
# usar tupla no formato (valor1, valor2, ..., valor7)
# tipo trabalhado: str, tuple
# tamanho da tupla len()

dias_da_semana = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")  # Cria uma tupla com os dias da semana
numero_dia = int(input("Digite um número de 1 a 7 para saber o dia correspondente: "))  # Lê um número do usuário
if 1 <= numero_dia <= 7:  # Verifica se o número está entre 1 e 7
    dia_correspondente = dias_da_semana[numero_dia - 1]  # Acessa o dia correspondente na tupla (ajustando o índice)
    print(f"O dia correspondente ao número {numero_dia} é: {dia_correspondente}")  # Exibe o dia correspondente ao número
else:
    print("Número inválido. Por favor, digite um número de 1 a 7.")  # Informa que o número é inválido caso não esteja entre 1 e 7
    


