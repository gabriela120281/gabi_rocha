# Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável). 
distancia_metros = int(input("Informe a distância em metros: "))
distancia = distancia_metros // 1000
metros_restantes = distancia_metros % 1000
print(f"A distância em km inteiros é: {distancia}")
print(f"A quantidade de metros restantes é: {metros_restantes}")

