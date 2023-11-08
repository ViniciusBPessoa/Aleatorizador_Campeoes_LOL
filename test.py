import time

# Obtém o tempo inicial
inicio = time.time()

resultado = 2 ** 1000000000

# Obtém o tempo final
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Imprime o tempo total de execução
print(f"Tempo total de execução: {tempo_total:.10f} segundos")
