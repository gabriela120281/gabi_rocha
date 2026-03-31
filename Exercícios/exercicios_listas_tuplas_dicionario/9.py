# [DICT - desafio] Atualizar preço e quantidade; calcular o total 

# Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
# Use: float(), int(), input(), acesso/atribuição por chave, print()
# Tipos: str, float, int, dict.
# Conceitos: operadores aritméticos (*, +), atualização de valores no dict.

produto = {
    "nome": input("Digite o nome do produto: "),  # Lê o nome do produto
    "preco": float(input("Digite o preço do produto: ")),  # Lê o preço do produto e converte para float
    "quantidade": int(input("Digite a quantidade do produto: "))  # Lê a quantidade do produto e converte para int
}   
aumento_percentual = float(input("Digite o aumento percentual para o preço (ex: 10 para 10%): "))  # Lê o aumento percentual e converte para float
produto["preco"] += produto["preco"] * (aumento_percentual / 100)  # Aplica o aumento percentual ao preço
produto["quantidade"] += 2  # Soma 2 unidades na quantidade
total = produto["preco"] * produto["quantidade"]  # Calcula o total
print(f"Produto: {produto['nome']}")
print(f"Preço atualizado: {produto['preco']:.2f}")
print(f"Quantidade atualizada: {produto['quantidade']}")
print(f"Total: {total:.2f}")

