# 1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.
# 2. Solicite ao usuário que informe a sua idade e depois exiba se é maior ou menor de idade.
# 3. Solicite ao usuário que informe a sua idade e depois classifique em:
# a. Menor ou igual a 11 anos = criança.
# b. Maior do que 11 e menor ou igual a 17 = adolescente.
# c. Maior do que 17 e menor ou igual a 59 = adulto
# d. Maior do que 59 = idoso.
# 4. Solicite ao usuário que informe um número e depois exiba se é par ou ímpar.
# 5. Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.
# 6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

numero = float(input("Digite um número: "))  # Solicita ao usuário que informe um número e converte para float
if numero > 0:  # Verifica se o número é positivo
    print("O número é positivo.")
elif numero < 0:  # Verifica se o número é negativo
    print("O número é negativo.")
else:  # Caso contrário, o número é zero
    print("O número é zero.")

idade = int(input("Digite sua idade: "))  # Solicita ao usuário que informe a idade e converte para inteiro
if idade >= 18:  # Verifica se a idade é maior ou igual a 18
    print("Você é maior de idade.") 
else:  # Caso contrário, a idade é menor que 18
    print("Você é menor de idade.")
    