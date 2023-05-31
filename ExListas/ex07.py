numeros = []

# Loop para ler os números
for i in range(5):
    num = int(input("Digite o número %d: " % (i+1)))
    numeros.append(num)

# Calculando a soma e a multiplicação dos números
soma = sum(numeros)
multiplicacao = 1
for num in numeros:
    multiplicacao *= num

# Imprimindo o resultado
print("Números: ", numeros)
print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)
