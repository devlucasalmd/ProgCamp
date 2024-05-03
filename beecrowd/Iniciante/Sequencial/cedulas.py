valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    qtd_notas = valor // nota
    print("{} nota(s) de R$ {:,.2f}".format(qtd_notas, nota).replace('.', ','))
    valor %= nota