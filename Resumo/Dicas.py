# =========================================
# 📚 FLASHCARDS DE ESTUDO - PYTHON INICIANTE
# =========================================

# -------------------------------
# 🟢 NÍVEL BÁSICO
# -------------------------------

# 🔹 VARIÁVEL
# Explicação: É um nome que usamos para guardar um dado na memória do computador.
idade = 25
print("Exemplo de variável:", idade)

# Dica: Use nomes claros e em minúsculas


# 🔹 PRINT()
# Explicação: Serve para exibir informações na tela
print("Olá, Mundo!")

# Dica: Textos devem estar entre aspas


# 🔹 INPUT()
# Explicação: Captura dados digitados pelo usuário (sempre como texto)
nome = input("Digite seu nome: ")
print("Olá,", nome)

# Erro comum: esquecer de converter para número quando necessário
# Exemplo correto:
numero = int(input("Digite um número inteiro: "))
print("Número + 1:", numero + 1)


# 🔹 TIPOS DE DADOS (int e float)
# Explicação:
# int = número inteiro
# float = número decimal

estoque = 10       # int
preco = 19.90      # float

print("Estoque:", estoque)
print("Preço:", preco)

# Dica: usar ponto (.) para decimais


# 🔹 STRING
# Explicação: Representa textos
curso = "Python Iniciante"
print("Curso:", curso)

# Dica: pode usar aspas simples ou duplas


# -------------------------------
# 🟡 NÍVEL INTERMEDIÁRIO
# -------------------------------

# 🔹 LISTA (list)
# Explicação: Coleção de itens mutável
frutas = ["uva", "maçã"]
frutas.append("pera")

print("Lista de frutas:", frutas)

# Dica: usa colchetes []


# 🔹 TUPLA (tuple)
# Explicação: Igual à lista, mas imutável
cores = ("vermelho", "azul")

print("Tupla de cores:", cores)

# Dica: usa parênteses ()


# 🔹 DICIONÁRIO (dict)
# Explicação: Armazena dados em chave:valor
aluno = {"nome": "Ana", "nota": 10}

print("Nome do aluno:", aluno["nome"])
print("Nota do aluno:", aluno["nota"])

# Dica: usa chaves {}


# 🔹 CONDICIONAIS (if / else)
# Explicação: Permite tomar decisões

nota = 7

if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# Dica: atenção na indentação!


# 🔹 ÍNDICE
# Explicação: Posição do item (começa em 0)

nomes = ["Caio", "Bia"]

print("Primeiro nome:", nomes[0])

# Erro comum: achar que começa em 1

# 🔹 LAÇO FOR
# Explicação: percorre uma sequência (lista, string, range)

for i in range(5):
    print("Número:", i)

# Dica: o range(5) gera valores de 0 até 4


# 🔹 LAÇO WHILE
# Explicação: repete enquanto a condição for verdadeira

contador = 0

while contador < 3:
    print("Contagem:", contador)
    contador += 1

# Erro comum: esquecer de atualizar a variável → loop infinito!


# 🔹 BREAK
# Explicação: interrompe o laço antes do fim

for letra in "Python":
    if letra == "h":
        break
    print(letra)

# Dica: útil para parar quando encontra o que procura


# 🔹 CONTINUE
# Explicação: pula para a próxima iteração

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Dica: ignora apenas o caso específico, mas continua o laço


# 🔹 LISTA DE COMPRAS
# Explicação: percorrer itens de uma lista

compras = ["Arroz", "Feijão", "Leite", "Pão"]

for item in compras:
    print("Comprar:", item)

# Dica: o for facilita quando temos várias tarefas repetitivas


# 🔹 CONTAGEM DE MOEDAS
# Explicação: somar valores com while

moedas = 0

while moedas < 5:
    print("Coloquei uma moeda")
    moedas += 1

print("Total de moedas:", moedas)

# Erro comum: esquecer de atualizar a variável → loop infinito


# 🔹 VERIFICAR SENHA
# Explicação: repetir até acertar

senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")

print("Acesso liberado!")

# Dica: usar while quando não sabemos quantas vezes será repetido


# 🔹 TABUADA
# Explicação: gerar cálculos automaticamente

numero = 7

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Dica: range ajuda a criar sequências numéricas


# 🔹 FILTRAR NOMES
# Explicação: pular nomes indesejados

nomes = ["Ana", "João", "Maria", "Pedro"]

for nome in nomes:
    if nome == "Maria":
        continue
    print("Nome válido:", nome)

# Dica: continue serve para ignorar casos específicos


# -------------------------------
# ✅ FINAL
# -------------------------------

print("\n--- Fim dos estudos de laços de repetição ---")

# 🎯 Conceitos importantes

# 📌 Lista
# Estrutura que guarda vários valores em uma única variável.
# Exemplo:
# notas = [7.5, 8.0, 6.0]
# print(notas)  # [7.5, 8.0, 6.0]

# 📌 Mutabilidade
# Listas podem ser alteradas depois de criadas (adicionar, remover, substituir valores).
# Exemplo:
# notas = [7.5, 8.0, 6.0]
# notas[2] = 9.0   # substitui o valor da posição 2
# print(notas)     # [7.5, 8.0, 9.0]

# 📌 Funções úteis
# append() → adiciona elemento no final da lista
# notas = []
# notas.append(7.5)
# print(notas)  # [7.5]

# sum() → soma todos os elementos da lista
# notas = [7.5, 8.0, 6.0]
# print(sum(notas))  # 21.5

# len() → retorna a quantidade de elementos
# notas = [7.5, 8.0, 6.0]
# print(len(notas))  # 3

# min() → retorna o menor valor da lista
# notas = [7.5, 8.0, 6.0]
# print(min(notas))  # 6.0

# index() → retorna a posição de um valor na lista
# notas = [7.5, 8.0, 6.0]
# print(notas.index(6.0))  # 2

# sort() → ordena a lista em ordem crescente
# notas = [9.0, 7.5, 8.0]
# notas.sort()
# print(notas)  # [7.5, 8.0, 9.0]

# 📌 Média aritmética
# Soma dos valores dividida pela quantidade de elementos.
# Exemplo:
# notas = [7.5, 8.0, 6.0]
# media = sum(notas) / len(notas)
# print(media)  # 7.166...

# 📌 f-string
# Forma prática de inserir variáveis dentro de textos.
# Exemplo:
# media = 7.1666
# print(f"A média das notas é: {media:.2f}")
# Saída: A média das notas é: 7.17


# 🎯 Conceitos importantes - Estrutura de Fila

# 📌 Lista como fila
# Uma lista pode representar uma fila de atendimento.
# O primeiro elemento (posição 0) é sempre o próximo a ser atendido.
# Exemplo:
# fila = ["Ana", "Bruno"]

# 📌 extend()
# Adiciona vários elementos de uma vez ao final da lista.
# Exemplo:
# fila = ["Ana", "Bruno"]
# fila.extend(["Carlos", "Daniela"])
# print(fila)  # ['Ana', 'Bruno', 'Carlos', 'Daniela']

# 📌 insert()
# Insere um elemento em uma posição específica da lista.
# Exemplo:
# fila = ["Ana", "Bruno", "Carlos"]
# fila.insert(1, "Fernanda")  # insere na posição 1
# print(fila)  # ['Ana', 'Fernanda', 'Bruno', 'Carlos']

# 📌 pop()
# Remove e retorna o elemento da posição indicada.
# Usar pop(0) remove o primeiro da fila (simulando atendimento).
# Exemplo:
# fila = ["Ana", "Bruno", "Carlos"]
# atendido = fila.pop(0)
# print(atendido)  # 'Ana'
# print(fila)      # ['Bruno', 'Carlos']

# 📌 print()
# Exibe o estado atual da fila em cada etapa.
# Exemplo:
# print("Fila atual:", fila)


# 🎯 Conceitos importantes - Dicionário em Python

# 📌 Dicionário
# Estrutura que guarda pares de chave-valor.
# Cada chave aponta para um valor específico.
# Exemplo:
# aluno = {"nome": "Ana", "idade": 20}

# 📌 input()
# Lê dados digitados pelo usuário.
# Exemplo:
# nome = input("Digite o nome: ")

# 📌 int()
# Converte um valor para número inteiro.
# Exemplo:
# idade = int(input("Digite a idade: "))

# 📌 Literal {}
# Cria um dicionário usando chaves {}.
# Exemplo:
# aluno = {"nome": "Ana", "idade": 20}

# 📌 Acesso por chave
# Para acessar um valor, usamos a chave entre colchetes.
# Exemplo:
# print(aluno["nome"])   # Ana
# print(aluno["idade"])  # 20

# 📌 print()
# Exibe valores na tela.
# Exemplo:
# print("Dicionário do aluno:", aluno)

# 📌 type()
# Mostra o tipo de uma variável.
# Exemplo:
# aluno = {"nome": "Ana", "idade": 20}
# print(type(aluno))  # <class 'dict'>
#
# Outros exemplos:
# nome = "Ana"
# print(type(nome))   # <class 'str'>
#
# idade = 20
# print(type(idade))  # <class 'int'>
#
# notas = [7.5, 8.0, 6.0]
# print(type(notas))  # <class 'list'>
#
# Assim você consegue identificar rapidamente se uma variável é string, inteiro, lista ou dicionário.



# 🎯 Conceitos importantes - Remoção segura em dicionários

# 📌 pop()
# Remove uma chave do dicionário e retorna o valor associado.
# Exemplo:
# produto = {"nome": "Caderno", "preco": 15.0, "desconto": 5}
# valor_removido = produto.pop("desconto")
# print(valor_removido)  # 5
# print(produto)         # {'nome': 'Caderno', 'preco': 15.0}

# 📌 Remoção segura com valor padrão
# Se a chave não existir, o Python normalmente gera erro.
# Para evitar isso, usamos um valor padrão como segundo argumento.
# Exemplo:
# produto = {"nome": "Caderno", "preco": 15.0}
# produto.pop("desconto", None)  # não existe 'desconto', mas não dá erro
# print(produto)  # {'nome': 'Caderno', 'preco': 15.0}

# 📌 Conceito
# - Usar dict.pop("chave", valor_padrao) garante que o programa não quebre
#   caso a chave não exista.
# - O valor padrão (ex.: None) é retornado quando a chave não é encontrada.
# - Isso é útil quando não temos certeza se uma chave está presente no dicionário.


# 🎯 Conceitos importantes - Atualização de dicionário

# 📌 Criação de dicionário com chaves
# produto = {"nome": "Caneta", "preco": 10.0, "quantidade": 5}

# 📌 Acesso e atribuição por chave
# produto["preco"] → acessa o preço
# produto["preco"] = 12.0 → altera o preço

# 📌 Operadores aritméticos
# * → multiplicação
# + → adição
# Exemplo: preco * quantidade

# 📌 Atualização de valores
# produto["preco"] += produto["preco"] * (percentual / 100)
# → aumenta o preço em uma porcentagem
#
# produto["quantidade"] += 2
# → soma 2 unidades à quantidade

# 📌 Cálculo do total
# total = produto["preco"] * produto["quantidade"]

# 📌 f-string
# Usada para exibir variáveis dentro de textos formatados.
# Exemplo:
# print(f"Preço atualizado: {produto['preco']:.2f}")
# → mostra o preço com 2 casas decimais


# 🎯 Conceitos importantes - Agenda (CRUD simples)

# 📌 Dicionário como agenda
# Cada chave é o nome do contato, cada valor é o telefone.
# Exemplo: agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}

# 📌 Adicionar contato
# agenda[nome] = telefone
# Exemplo: agenda["Carlos"] = "3333-3333"

# 📌 Atualizar contato
# if nome in agenda:
#     agenda[nome] = novo_telefone
# else:
#     print("Contato não encontrado")

# 📌 Remover contato
# if nome in agenda:
#     agenda.pop(nome)
# else:
#     print("Contato não encontrado")

# 📌 Ordenar nomes
# nomes_ordenados = sorted(agenda.keys())
# print(nomes_ordenados)  # ['Ana', 'Bruno', 'Carlos']

# 📌 Conceitos usados
# - CRUD em dicionários: Create, Read, Update, Delete
# - Teste de existência com "in"
# - Remoção com pop()
# - Ordenação de chaves com sorted()


# 🎯 Conceitos importantes - Tupla

# 📌 Tupla
# Estrutura de dados imutável (não pode ser alterada depois de criada).
# Sintaxe: (valor1, valor2, valor3, ...)
# Exemplo: tupla = ("Ana", "Bruno")

# 📌 input()
# Lê dados digitados pelo usuário.
# Exemplo: nome = input("Digite o nome: ")

# 📌 Criação de tupla
# tupla_nomes = (nome1, nome2)

# 📌 print()
# Exibe valores na tela.
# Exemplo: print("Tupla de nomes:", tupla_nomes)

# 📌 type()
# Mostra o tipo de uma variável.
# Exemplo: print(type(tupla_nomes))  # <class 'tuple'>

# 📌 Quando usar tupla
# - Quando os dados não devem ser alterados (imutabilidade).
# - Para representar pares ou grupos fixos de valores.
# Exemplo: coordenadas = (10, 20), data = (31, 3, 2026)

# 🎯 Conceitos importantes - Tupla e operador "in"

# 📌 Tupla
# Estrutura imutável (não pode ser alterada depois de criada).
# Sintaxe: (valor1, valor2, valor3, ...)
# Exemplo: tupla_frutas = ("maçã", "banana", "uva")

# 📌 input()
# Lê dados digitados pelo usuário.
# Exemplo: fruta = input("Digite uma fruta: ")

# 📌 Operador de pertinência "in"
# Verifica se um elemento está dentro da tupla.
# Exemplo:
# if "banana" in tupla_frutas:
#     print("Está na tupla")
# else:
#     print("Não está na tupla")

# 📌 print()
# Exibe valores na tela.
# Exemplo: print("Tupla de frutas:", tupla_frutas)

# 📌 type()
# Mostra o tipo da variável.
# Exemplo: print(type(tupla_frutas))  # <class 'tuple'>

# 📌 Quando usar tupla
# - Para dados que não devem ser alterados.
# - Para representar grupos fixos de valores.
# Exemplo: coordenadas = (10, 20), data = (31, 3, 2026)


# 🎯 Conceitos importantes - Tupla e método count()

# 📌 Tupla
# Estrutura imutável que guarda valores em ordem.
# Exemplo: tupla_numeros = (2, 5, 2, 7)

# 📌 input() e int()
# input() lê dados do usuário como string.
# int() converte para número inteiro.
# Exemplo: num = int(input("Digite um número: "))

# 📌 Método count()
# Conta quantas vezes um valor aparece na tupla.
# Exemplo:
# tupla = (2, 5, 2, 7)
# tupla.count(2) → 2

# 📌 print() com f-string
# Exibe valores formatados.
# Exemplo:
# print(f"O número {numero_busca} aparece {contador} vezes na tupla.")

# 🎯 Conceitos importantes - Tupla e índices

# 📌 Tupla
# Estrutura imutável que guarda valores em ordem.
# Exemplo: dias_da_semana = ("Domingo", "Segunda-feira", ..., "Sábado")

# 📌 Índices
# Os elementos da tupla são acessados por posição.
# O primeiro elemento tem índice 0.
# O último elemento tem índice -1 ou 6 (no caso de 7 dias).
# Exemplo:
# dias_da_semana[0] → "Domingo"
# dias_da_semana[6] → "Sábado"

# 📌 Ajuste de índice
# Como o usuário digita de 1 a 7, precisamos ajustar:
# numero_dia - 1 → índice correto da tupla.
# Exemplo: se o usuário digita 1 → índice 0 → "Domingo"

# 📌 Validação
# if 1 <= numero_dia <= 7:
#     dia_correspondente = dias_da_semana[numero_dia - 1]
# else:
#     print("Número inválido")

# 📌 len()
# Retorna o tamanho da tupla.
# Exemplo: len(dias_da_semana) → 7

# 🎯 Conceitos importantes - Tupla de notas com média

# 📌 Tupla
# Estrutura imutável que guarda valores em ordem.
# Exemplo: tupla_notas = (7.5, 8.0, 6.0)

# 📌 float()
# Converte entrada para número decimal.
# Exemplo: nota = float(input("Digite a nota: "))

# 📌 sum()
# Soma todos os elementos da tupla.
# Exemplo: sum((7.5, 8.0, 6.0)) → 21.5

# 📌 len()
# Retorna o tamanho da tupla (quantos elementos).
# Exemplo: len((7.5, 8.0, 6.0)) → 3

# 📌 Média
# media = sum(tupla_notas) / len(tupla_notas)

# 📌 print() com f-string
# Exibe valores formatados.
# Exemplo: print(f"A média é: {media:.2f}")
# → mostra a média com 2 casas decimais

# 🎯 Conceitos importantes - Tupla vs Lista

# 📌 Tupla ()
# Estrutura imutável (não pode ser alterada).
# Exemplo: tupla = (7, 3, 9, 1)

# 📌 Lista []
# Estrutura mutável (pode ser alterada).
# Exemplo: lista = [7, 3, 9, 1]
# lista.append(5) → [7, 3, 9, 1, 5]

# 📌 sorted()
# Cria uma lista ordenada a partir de uma tupla ou lista.
# Exemplo: sorted((7, 3, 9, 1)) → [1, 3, 7, 9]

# 📌 type()
# Mostra o tipo da variável.
# Exemplo: type(lista_ordenada) → <class 'list'>

# 📌 Diferença prática
# - Tupla: dados fixos, não mudam.
# - Lista: dados que podem ser alterados.


# -------------------------------
# ✅ FINAL
# -------------------------------
