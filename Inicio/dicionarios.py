# Criando dicionários
aluna = {"id": 1, "nome": "Gabriela", "nota": 9.5}
pessoa = {"nome": "Lucas", "idade": 25} 

# Acessar valores por chaves
print("_____________________________________________________")
print('\n' "O nome da aluna é:", aluna["nome"])
print("_____________________________________________________")
print('\n' "O nome da pessoa é:", pessoa["nome"])
print("_____________________________________________________")

# Adicionar e alterar chaves/valores
pessoa["cidade"] = "Florianópolis"    #adiciona nova chave
print("_____________________________________________________")
pessoa["idade"] = 26                  #altera valor existente
print("Pessoa atualizada:", pessoa)

# Remover chave
removido = pessoa.pop("idade")
print("_____________________________________________________")
print("Valor removido (idade):", removido)
print("_____________________________________________________")
print("Após pop('idade'):", pessoa)
print("_____________________________________________________")




