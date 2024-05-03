valor = float(input())

centavos = int(valor * 100)

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    qtd_notas = centavos // nota
    print("{} nota(s) de R$ {:.2f}".format(qtd_notas, nota / 100))
    centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = centavos // moeda
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda / 100))
    centavos %= moeda