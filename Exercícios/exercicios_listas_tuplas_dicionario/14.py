# [TUPLE] Exibir maior e menor valor
# Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
# Orientações: 
 
# funções: max(), min()
 
# tipos: int, tuple
 
# conceito: operações básicas de agregação

num1 = int(input("Digite o primeiro número inteiro: "))  # Lê o primeiro número inteiro
num2 = int(input("Digite o segundo número inteiro: "))  # Lê o segundo número inteiro
num3 = int(input("Digite o terceiro número inteiro: "))  # Lê o terceiro número inteiro
num4 = int(input("Digite o quarto número inteiro: "))  # Lê o quarto número inteiro
tupla_numeros = (num1, num2, num3, num4)  # Cria uma tupla com os quatro números inteiros
maior_numero = max(tupla_numeros)  # Encontra o maior número na tupla
menor_numero = min(tupla_numeros)  # Encontra o menor número na tupla
print(f"O maior número é: {maior_numero}")  # Exibe o maior número
print(f"O menor número é: {menor_numero}")  # Exibe o menor número

