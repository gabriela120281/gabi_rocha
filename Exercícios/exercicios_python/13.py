

# 13 Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Informe o salário: "))
aumento = float(input("Informe o percentual de aumento (ex: 10 para 10%): "))
novo_salario = salario * (1 + aumento / 100)
print(f"O novo salário é: R$ {novo_salario:.2f}")
