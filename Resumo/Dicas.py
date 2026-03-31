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



# -------------------------------
# ✅ FINAL
# -------------------------------
