frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Acessando elementos 
print("Primeira fruta:", frutas[0])  # maçã
print("Última fruta:", frutas[-1])  # uva

# Alterando elementos
frutas[1] = "banana-nanica"
print("Após aletrar:", frutas)

# Adicinando elementos
frutas.append("morango")   # adiciona no final
frutas.insert(1, "pera")   # adiciona na posição 1

# Removendo elementos 
frutas.remove("uva")       # remove pelo valor
ultima = frutas.pop()      #remove e retornar o último
print("Após remover 'uva' e pop():", frutas, "| Última removida:", ultima)

# Tamanho (quantidade de elementos)
print("Tamanho da lista 'fruta':", len(frutas))

# Fatiamento (slicing)
print("Fatiamento [0:2]:", frutas [0:2])

# Verificar se um item está na lista
print("Tem maçã?", "maçã" in frutas)



