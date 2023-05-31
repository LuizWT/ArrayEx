# Criando dois vetores vazios
vetor1 = []
vetor2 = []

# Loop para ler os elementos do primeiro vetor
print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input("Elemento %d: " % (i+1)))
    vetor1.append(elemento)

# Loop para ler os elementos do segundo vetor
print("Digite os elementos do segundo vetor:")
for i in range(10):
    elemento = int(input("Elemento %d: " % (i+1)))
    vetor2.append(elemento)

# Criando um terceiro vetor com os elementos intercalados
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Imprimindo os vetores
print("Vetor 1: ", vetor1)
print("Vetor 2: ", vetor2)
print("Vetor 3 (intercalado): ", vetor3)
