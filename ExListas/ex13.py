alunos = []

qnt = int(input("Quantos alunos você quer cadastrar? "))

for i in range(qnt):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    curso = str(input("Digite o nome do seu curso: "))
    sem = str(input("Em qual semestre você está? "))
    print('\n')

    aluno = {"Nome": nome, "Idade": idade, "Curso": curso, "Semestre": sem}
    alunos.append(aluno)

print("Nome dos alunos:")
for aluno in alunos:
    print(aluno["Nome"])