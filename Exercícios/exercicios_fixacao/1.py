# Lista de Exercícios - Operadores de atribuição
# 2 -Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado; 
# ambos os valores devem ser do tipo FLOAT. Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela.  
saldo = float(input("Informe o saldo da sua conta: R$ "))
deposito = float(input("Informe o valor do depósito: R$ "))
saldo += deposito
print(f"O novo saldo da sua conta é: R$ {saldo:.2f}")