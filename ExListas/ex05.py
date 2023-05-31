# Criando os vetores vazios
PAR = []
IMPAR = []

# Loop para ler os 20 números
for i in range(20):
    num = int(input("Digite um número inteiro: "))
    
    # Verificando se é par ou ímpar e adicionando ao vetor correspondente
    if num % 2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

# Imprimindo os vetores resultantes
print("Números pares: ", PAR)
print("Números ímpares: ", IMPAR)
