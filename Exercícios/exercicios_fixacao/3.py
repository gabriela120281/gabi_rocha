# Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). 
# Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.  
estoque_inicial = int(input("Informe o estoque no início do dia: "))
quantidade_vendida = int(input("Informe a quantidade vendida ao final do dia: "))
estoque_final = estoque_inicial - quantidade_vendida
print(f"O estoque final é: {estoque_final}")
