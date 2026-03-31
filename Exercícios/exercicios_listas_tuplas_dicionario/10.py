# [DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes

# Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
# Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
#Exibir a lista ordenada de nomes de contatos
#Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}  # Agenda inicial
print("Agenda inicial:", agenda)  # Exibe a agenda inicial
# Adicionar um novo contato
novo_nome = input("Digite o nome do novo contato: ")  # Lê o nome do novo contato
novo_telefone = input("Digite o telefone do novo contato: ")  # Lê o telefone do novo contato
agenda[novo_nome] = novo_telefone  # Adiciona o novo contato à agenda
print("Agenda após adicionar novo contato:", agenda)  # Exibe a agenda após adição
# Atualizar o telefone de um contato informado (se existir)
nome_atualizar = input("Digite o nome do contato para atualizar o telefone: ")  # Lê o nome do contato para atualizar
if nome_atualizar in agenda:  # Verifica se o contato existe na agenda
    novo_telefone_atualizado = input("Digite o novo telefone para o contato: ")  # Lê o novo telefone para o contato
    agenda[nome_atualizar] = novo_telefone_atualizado  # Atualiza o telefone do contato na agenda
    print(f"Telefone do contato '{nome_atualizar}' atualizado.")  # Informa que o telefone foi atualizado

else:
    print(f"Contato '{nome_atualizar}' não encontrado na agenda.")  # Informa que o contato não foi encontrado  
# Remover um contato pelo nome (se existir)
nome_remover = input("Digite o nome do contato para remover: ")  # Lê o nome do contato para remover
if nome_remover in agenda:  # Verifica se o contato existe na agenda
    agenda.pop(nome_remover)  # Remove o contato da agenda
    print(f"Contato '{nome_remover}' removido.")  # Informa que o contato foi removido
else:
    print(f"Contato '{nome_remover}' não encontrado na agenda.")  # Informa que o contato não foi encontrado
# Exibir a lista ordenada de nomes de contatos
nomes_ordenados = sorted(agenda.keys())  # Obtém a lista de nomes ordenados
print("Lista ordenada de contatos:", nomes_ordenados)  # Exibe a lista ordenada de nomes de contatos

