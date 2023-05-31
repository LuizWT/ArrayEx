# Criando vetores vazios
idades = []
alturas = []

# Loop para ler as informações de cada pessoa
for i in range(5):
    idade = int(input("Digite a idade da pessoa %d: " % (i+1)))
    altura = float(input("Digite a altura da pessoa %d em metros: " % (i+1)))
    idades.append(idade)
    alturas.append(altura)

# Imprimindo as informações na ordem inversa
print("Idades na ordem inversa: ", end="")
for idade in reversed(idades):
    print(idade, end=" ")

print("\nAlturas na ordem inversa: ", end="")
for altura in reversed(alturas):
    print("%.2f" % altura, end="m ")
