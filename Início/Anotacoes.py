nome = input("Informe seu nome?")
print("Olá, " , nome)
idade = input("Informe sua idade?")
print("Você tem ", idade, " anos.") 


# Exercicio 4 - Leia um numero e imprima o dobro dele.
numero = 2
dobro = numero * 2
print("O dobro de ", numero, " é ", dobro)


      
# Exercicio 13 - Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
# 1º ler um salário | 2º ler um percentual de aumento | 3º calcular o novo salário

salario = float("2000.00")
aumento = float(1.10)
novo_salario = (salario * aumento)
print("O novo salário é:", novo_salario)

# Exercicio 8 - Leia um número como string e imprima o seu tipo antes e depois de converter para inteiro.
# 1º ler como string | 2º imprimir tipo | 3º converter para inteiro | 4º imprimir tipo novamente
numero_str = "10"
print("Tipo antes da conversão:", type(numero_str))
numero_int = int(numero_str)    
print("Tipo após a conversão:", type(numero_int))


# Exercicio 10 - Leia o raio de um círculo (float) e calcule a área (A = π * r^2). Use π = 3.14.
# 1º Ler o raio | 2º Calcular a área | 3º Imprimir a área
raio = float(5.0)
Area = 3.14 * (raio ** 2)
print("A área do círculo é:", Area)

# Exercício 12 - Leia 3 notas (float) e imprima a média com duas casas decimais.
# 1º Ler a nota 1 (float) | 2º Ler a nota 2 (float) | 3º Ler a nota 3 (float) | 4º Calcular a média | 5º Imprimir a média com duas casas decimais
nota1 = float(7.0)
nota2 = float(5.0)
nota3 = float(9.0)
media = (nota1 + nota2 + nota3) / 3
print(f"A média é: {media:.2f}")

