# Criando tuplas
coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

# Acessando elementos
print("X:", coordenadas[0], "| Y:", coordenadas[1])

# Slicing (fatiamento) em tuplas
print("Primeiros 3 dias:", dias[ :3])

# Tamanho
print("Tamanho da tupla 'dias':" , len(dias))

# Verificar se um elemento está na tupla
print("Tem 'segunda'?", "segunda" in dias)

# Contagem e índice em tuplas
print("Contagem de 'terça':", dias.count("terça"))
print("Índice de 'quarta':", dias.index("quarta"))


dias = ("segunda", "terça", "quarta", "quinta", "sexta")
print("_____________________________________________________")
print('\n' "Os dias da semana são:", dias)
print("_____________________________________________________")
print('\n' "O primeiro dia da semana é:" , dias[0])
print("_____________________________________________________")
print('\n' "O útlimo dia da semana é:", dias[-1])
print("_____________________________________________________")
print('\n' "O tamanho da tupla é:", len(dias))
print("_____________________________________________________")

