# Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6. 
estoque = int(input("Informe o valor do estoque: "))
vendas = int(input("Informe a quantidade de vendas: "))
print(f"O valor do estoque após as vendas é: {estoque - vendas}")
reposicao = int(input("Informe a quantidade de reposicao do estoque: "))
estoque -= vendas
estoque += reposicao
estoque %= 6
print(f"O valor final do estoque é: {estoque}")

