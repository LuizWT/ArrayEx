A = []

# Loop para ler os números
for i in range(10):
    num = int(input("Digite o número %d: " % (i+1)))
    A.append(num)

# Calculando a soma dos quadrados dos números
soma_quadrados = 0
for num in A:
    soma_quadrados += num ** 2

# Imprimindo o resultado
print("Vetor A: ", A)
print("Soma dos quadrados dos elementos do vetor A: ", soma_quadrados)
