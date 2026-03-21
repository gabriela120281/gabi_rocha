frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Outras Operações
print("Lista original 'numeros':" , numeros)
print("Soma dos números:" , sum(numeros))
print("Maior número:" , max(numeros))
print("Menor número:" , min(numeros))
numeros.reverse()
print ("Reversa:", numeros)
numeros.sort()
print("Ordenada crescente:", numeros)
numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)

# Iterar sobre lista
for fruta in frutas:
    print("Fruta:", fruta)

# Lis comprehension (exemplo simples)
quadrados = [n * n for n in [1, 2, 3, 4, 5]]
print("Quadrados:", quadrados)

# Crie uma lista 
lista_compras = ["leite", "arroz", "feijão"]
numeros = [1, 2, 3, 4]
print("Lista de hoje", lista_compras)

# Adicionando elementos
lista_compras.append("Sal")          # Adiciona no final
lista_compras.insert(1, "Macarrão")  # Adiciona na posição 1
print("Após adicionar:", lista_compras)

# Remover elementos
lista_compras.remove("Macarrão")    # Remove pelo valor
ultima = lista_compras.pop()        # Remove e retorna a ultima
print("Após remover 'Macarrão' e pop():", lista_compras, "| ùltima removida:" , ultima)

# Teste



