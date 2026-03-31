# [DICT] Remover uma chave com segurança

# Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
# Use: input(), float(), dict.pop("chave", valor_padrao), print()
# Tipos: str, float, dict.
# Conceitos: remoção segura, estado antes/depois.

produto = {"nome": input("Digite o nome do produto: "), "preco": float(input("Digite o preço do produto: "))}  # Cria o dicionário do produto
print("Dicionário do produto antes de remover 'desconto':", produto)  # Exibe o dicionário antes de tentar remover a chave "desconto"
produto.pop("desconto", None)  # Tenta remover a chave "desconto"   # sem gerar erro, usando None como valor padrão
print("Dicionário do produto após tentar remover 'desconto':", produto)  # Exibe o dicionário após tentar remover a chave "desconto" (sem alteração)

