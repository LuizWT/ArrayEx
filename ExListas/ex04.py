# Definir o vetor de caracteres
vetor = []

# Solicitar ao usuário para digitar os 10 caracteres
for i in range(10):
  vetor.append(input("Digite um caractere: "))

# Inicializar a variável de contagem de consoantes
consoantes = 0

# Inicializar a lista para armazenar as consoantes
lista_consoantes = []

# Verificar cada caractere no vetor e contar as consoantes
for caractere in vetor:
  if caractere.isalpha() and caractere not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    consoantes += 1
    lista_consoantes.append(caractere)

# Imprimir o número de consoantes encontradas e as próprias consoantes
print("Número de consoantes: ", consoantes)
print("Consoantes encontradas: ", lista_consoantes)