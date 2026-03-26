# Solicite um número (int), aplique n %= 2 e exiba o valor na tela. Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar.  
numero = int(input("Informe um número: "))
numero %= 2
print(f"O resultado da operação é: {numero}")
if numero == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
