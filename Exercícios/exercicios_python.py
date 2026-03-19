# Exercícios de fixação para desenvolvimento em Python
# 1. Peça ao usuário seu nome e cumprimente utilizando a função print(), ex.: "Olá, Carol!"
nome = input("Digite seu nome: ")
print("Olá", nome,"!")

# 2. Peça ao usuário sua idade e exiba na tela: "Você tem {idade} anos!"
idade = input("Digite sua idade: ")
print("Você tem", idade, "anos!")

# 3 Leia o nome e a cidade da pessoa e imprima: "{nome} mora em {cidade}."
cidade = input("Digite a cidade onde você mora: ")
print(nome, "mora em", cidade + ".")

# 4 Leia um número e imprima o dobro dele.
numero = float(input("Digite um número: "))
dobro = numero * 2
print("O dobro de", numero, "é", dobro)

# 5 Leia dois números inteiros e imprima a soma.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print("A soma de", num1, "e", num2, "é", soma)

# 6 Leia a altura (em metros) como float e imprima: "Sua altura é {altura}m"
altura = float(input("Altura (m): "))
print("Sua altura é", altura, "m")

# 7 Leia dois números decimais (float) e imprima a média.
num3 = float(input("Digite o primeiro número decimal: "))
num4 = float(input("Digite o segundo número decimal: "))
media = (num3 + num4)/2
print("A média de", num3, "e", num4, "é,", media)

# 8 Leia um número como string e imprima o seu tipo antes e depois de converter para int.
num_str = input("Digite um número: ")
print("Tipo antes da conversão:", type(num_str))
num_int = int(num_str)
print("Tipo depois da conversão:", type(num_int))

# 9 Leia o preço de um produto e imprima o preço com 10% de desconto.
preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.10
preco_com_desconto = preco - desconto
print("O preço com 10% de desconto é:", preco_com_desconto)

# 10 Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.
raio = float(input("Informe o raio do círculo: "))
area = 3.14 * (raio ** 2)
print("A área do círculo é:", area)

# 11 Leia a distância (km) e o tempo (h), calcule a velocidade média.
distancia = float(100.0)
tempo = float(2.0)
velocidade_media = distancia / tempo
print("A velocidade média é:", velocidade_media, "km/h")


# 12 Leia 3 notas (float) e imprima a média com duas casas decimais.
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média é: {media:.2f}")

# 13 Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Informe o salário: "))
aumento = float(input("Informe o percentual de aumento (ex: 10 para 10%): "))
novo_salario = salario * (1 + aumento / 100)
print(f"O novo salário é: R$ {novo_salario:.2f}")

# 14 Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(135)
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")

# 15 Leia o nome e a idade e imprima exatamente neste formato: 
# Nome: <nome> | Idade: <idade> anos
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
print(f"Nome: {nome} | Idade: {idade} anos")

# 16 Leia dois int (a e b) e imprima: 
# a + b = X | a - b = Y | a * b = Z
a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
print("a + b =", soma)
print("a - b =", subtracao)
print("a * b =", multiplicacao)

# 17 Leia um float e imprima com 2 casas decimais
numero = float(3.14159547)
print(f"O núemro com 2 cassas decimais é: {numero:.2f}")

# 18 Leia um nome e uma nota (float), com uma casa decimal, e imprima:
# Aluno <nome> ficou com nota <nota>
nome = input("Informe seu nome: ")
nota = float(input("Informe sua nota: "))
print(f"Aluno {nome} ficou com nota {nota:.1f}")

# 19 Leia o ano de nascimento (int) e imprima a idade estimada. (considere ano atual = 2026).
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"A idade estimada é: {idade} anos")


































