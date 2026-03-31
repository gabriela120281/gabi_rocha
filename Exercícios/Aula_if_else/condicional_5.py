# Solicite ao usuario que digite uma nota
nota = int(input("Digite uma nota de 0 a 10: "))

# Classifica a nota de acordo com as faixas
if nota >= 9 and nota <= 10:
    print("Excelente")
elif nota >= 7 and nota < 9:
    print("Bom")
elif nota >= 5 and nota < 7:
    print("Regular")
elif nota >= 0 and nota < 5:
    print("Reprovado")
else:    
    print("Nota inválida")

    



