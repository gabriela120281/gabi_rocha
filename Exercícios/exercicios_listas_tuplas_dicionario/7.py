# [DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
# Adicionar uma nova chave nota
# Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
# Use: float(), input(), atribuição dict["nota"] = valor, print()
# Tipos: float, dict.
# Conceitos: atualização/adição de chave, tipos numéricos.
nome = input("Digite o nome do aluno: ")  # Lê o nome do aluno
idade = int(input("Digite a idade do aluno: "))  # Lê a idade do aluno e converte para int
aluno = {"nome": nome, "idade": idade}  # Cria o dicionário do aluno
nota = float(input("Digite a nota do aluno: "))  # Lê a nota do aluno e converte para float
aluno["nota"] = nota  # Adiciona a chave "nota" ao dicionário do aluno
print("Dicionário do aluno atualizado:", aluno)  # Exibe o dicionário atualizado do aluno   
