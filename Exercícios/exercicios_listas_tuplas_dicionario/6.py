# [DICT] Criar e exibir dicionário de aluno

# Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
# Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
# Tipos: str, int, dict.
# Conceitos: mapeamento chave-valor, criação e exibição.

nome = input("Digite o nome do aluno: ")  # Lê o nome do aluno
idade = int(input("Digite a idade do aluno: "))  # Lê a idade do aluno e converte para int
aluno = {"nome": nome, "idade": idade}  # Cria o dicionário do aluno
print("Dicionário do aluno:", aluno)  # Exibe o dicionário do aluno
print("Tipo do dicionário:", type(aluno))  # Exibe o tipo do dicionário do aluno

