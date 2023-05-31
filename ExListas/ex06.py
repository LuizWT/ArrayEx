# Criando um vetor vazio para armazenar as médias
medias = []

# Loop para ler as notas de cada aluno
for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input("Digite a nota do aluno %d na prova %d: " % (i+1, j+1)))
        notas.append(nota)
    
    # Calculando a média do aluno e adicionando ao vetor de médias
    media = sum(notas) / len(notas)
    medias.append(media)

# Contando o número de alunos com média maior que 7
num_alunos_aprovados = 0
for media in medias:
    if media > 7:
        num_alunos_aprovados += 1

# Imprimindo o resultado
print("Número de alunos com média maior que 7: %d" % num_alunos_aprovados)
