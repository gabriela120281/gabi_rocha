# [LIST - desafio] Fila: chegadas, prioridade e atendimento

# Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

fila = ["Ana", "Bruno"]                  # fila inicial
print("Fila iniciaal:", fila)            # Exibe a fila inicial
fila.extend(input("Digite dois nomes separados por espaço: ").split()) # Adiciona dois nomes à fila
print("Fila após adicionar dois nomes:", fila)                     # Exibe a fila após adição
cliente_prioritario = input("Digite o nome do cliente prioritário: ") # Lê o cliente prioritário
fila.insert(1, cliente_prioritario)       # Insere o cliente prioritário na posição 1
print("Fila após inserir cliente prioritário:", fila)                 # Exibe a fila após inserir
atendido = fila.pop(0)                   # Atende o primeiro cliente (remove e captura)
print(f"Cliente atendido: {atendido}")    # Exibe o cliente atendido
print("Fila final:", fila)               # Exibe a fila final


