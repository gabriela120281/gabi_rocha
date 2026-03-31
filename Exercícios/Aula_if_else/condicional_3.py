nota_matematica = int(input("Digite a nota de matemática: "))
nota_portugues = int(input("Digite a nota de português: "))
nota_geografia = int(input("Digite a nota de geografia: "))

aprovados = []  # lista para armazenar as matérias aprovadas

# Verificar a nota de matemática
if nota_matematica >= 0 and nota_matematica <= 5:
    print("Reprovado em matemática")
elif nota_matematica > 5 and nota_matematica < 7:
    print("Recuperação em matemática")
elif nota_matematica >= 7 and nota_matematica <= 10:
    print("Aprovado em matemática")


# Verificar a nota de portugues
if nota_portugues >= 0 and nota_portugues <= 5:
    print("Reprovado em portugues")
elif nota_portugues > 5 and nota_portugues < 7:
    print("Recuperação em portugues")
elif nota_portugues >= 7 and nota_portugues <= 10:
    print("Aprovado em portugues")


# Verificar a nota de geografia
if nota_geografia >= 0 and nota_geografia <= 5:
    print("Reprovado em geografia")
elif nota_geografia > 5 and nota_geografia < 7:
    print("Recuperação em geografia")
elif nota_geografia >= 7 and nota_geografia <= 10:
    print("Aprovado em geografia")  

# Mostrar as matérias aprovadas
if nota_matematica >= 7:
    aprovados.append("Matemática")
if nota_portugues >= 7:
    aprovados.append("Português")
if nota_geografia >= 7:
    aprovados.append("Geografia")

print("\nMaterias aprovadas:")
for materia in aprovados:
    print(materia)  




