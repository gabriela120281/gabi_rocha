# Solicite ao usuário que informe um orçamento (float) e um gasto (float). Utilize atribuição -= 
# para descontar o gasto do orçamento.  
orçamento = float(input("Informe o orçamennto: R$ "))
gasto = float(input("Informe o valor do gasto: R$ "))
orçamento -= gasto
print(f"O orçamento restante é: R$ {orçamento:.2f}")

