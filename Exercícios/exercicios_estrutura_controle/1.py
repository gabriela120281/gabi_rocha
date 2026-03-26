#  Calculadora de IMC (Índice de Massa Corporal)
#  Solicitar o peso e ler o valor   
# Solicitar a altura(m) e ler o valor
# Solicitar o IMC utilizando a fórmula: peso / (altura * altura)
# Se o IMC for menor que 18.5, exibir "Abaixo do peso"
# Se o IMC for entre 18.5 e 25, exibir "Peso normal"
# Se o IMC for entre 25 e 30, exibir "Sobrepeso"
# Senão, exibir "Obesidade"
# Encerrar o algoritmo

# Entrada de dados
peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

# Cálculo do IMCS
imc = peso / (altura * altura)

# Classificação

if imc < 18.5:
    categoria = "Magreza"
elif imc >= 18.5 and imc <25: # já sabemos que é >= 18.5 aqui
    categoria = "Normal"
elif imc >=25 and icm < 30: # já sabemos que é >= 25 aqui
    categoria = "Sobre peso"
else: 
    categoria = "Obesidade"

# Saída formatada
print(f"IMC = {imc:.2f} - {categoria}")




