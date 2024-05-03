n = int(input())

anos = n // 365
n %= 365
meses = n // 30
n %=30
dias = n

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
