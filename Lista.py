frutas = ["maça", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Acessando elementos
print("Primeira fruta", frutas [0])     # "maçã"
print("Última fruta"), frutas [-1]      # "uva"


# Alterando elementos
frutas [1] = "banana-nanica"
print("Após alterar", frutas)

# Adicionando elementos
frutas.append("morango")        # adiciona no final
frutas.insert(1, "pera")        #adiciona na posição 1
print("Após adicionar", frutas)

# Removendo elementos
frutas.remove("uva")            # remove pelo valor
ultima = frutas.pop ()          #remove e retorna o último
print("Após remover 'uva' e pop ()", frutas, "|Última removida", ultima)
    