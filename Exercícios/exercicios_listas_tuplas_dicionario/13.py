# [TUPLE] Contar quantas vezes um número aparece

# Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
# Orientações: 
 
# método: tuple.count()
 
# tipos: int, tuple

num1 = int(input("Digite o primeiro número inteiro: "))  # Lê o primeiro número inteiro
num2 = int(input("Digite o segundo número inteiro: "))  # Lê o segundo
num3 = int(input("Digite o terceiro número inteiro: "))  # Lê o terceiro número inteiro
num4 = int(input("Digite o quarto número inteiro: "))  # Lê o quarto número inteiro
tupla_numeros = (num1, num2, num3, num4)  # Cria uma tupla com os quatro números inteiros
numero_busca = int(input("Digite um número para contar quantas vezes aparece na tupla: "))  # Lê o número a ser contado
contador = tupla_numeros.count(numero_busca)  # Conta quantas vezes o número aparece na tupla
print(f"O número {numero_busca} aparece {contador} vezes na tupla.")

