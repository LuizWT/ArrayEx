notas = []
i = 0
while i <= 3:
    notas.append(float(input("Digite a {}° nota: ".format(i))))
    #verificar se o valor de notas está entre 0 e 10
    if notas[i-1] < 0 or notas[i-1] > 10:
        print("O valor deve ser um número entre 0 e 10")
        #realizar a média das notas
        media = (notas[i-1] + notas[i-1] + notas[i-1]) / 4
        print(f'A média das notas é {media}')
        notas.remove(notas[i-1]) # remove o valor errado
    else:
        i = i + 1
print(notas)