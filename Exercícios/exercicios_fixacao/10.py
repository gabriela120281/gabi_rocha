# Solicite ao usuário que informe os tempos em segundos (int). Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.  
segundos = int(input("Informe a quantidade de segundos: "))
minutos = segundos // 60
segundos_restantes = segundos % 60
print(f"A quantidade de minutos inteiros é: {minutos}")
print(f"A quantidade de segundos restantes é: {segundos_restantes}")

