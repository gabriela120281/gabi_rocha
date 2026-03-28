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


# -------------------------------
# ✅ FINAL
# -------------------------------

print("\n--- Fim dos estudos básicos de Python ---")