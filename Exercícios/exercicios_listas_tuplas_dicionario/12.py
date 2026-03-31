# [TUPLE] Acessar elementos da tupla

# Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
# Orientações: 
 
# usar in
 
# usar input()
 
# tipo: str, tuple
 
# conceito: operador de pertinência

fruta1 = input("Digite a primeira fruta: ")  # Lê a primeira fruta do usuário
fruta2 = input("Digite a segunda fruta: ")  # Lê a segunda fruta
fruta3 = input("Digite a terceira fruta: ")  # Lê a terceira fruta
tupla_frutas = (fruta1, fruta2, fruta3)  # Cria uma tupla com as três frutas
fruta_busca = input("Digite uma fruta para verificar se está na tupla: ")  # Lê a fruta a ser verificada
if fruta_busca in tupla_frutas:  # Verifica se a fruta está na  tupla
    print(f"A fruta '{fruta_busca}' está na tupla.")  # Informa que a fruta está na tupla
else:
    print(f"A fruta '{fruta_busca}' não está na tupla.")  # Informa que a fruta não está na tupla   
    