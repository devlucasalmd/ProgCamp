n, qtd = map(int,input().split())

if n == 1:
    print("Total: R$ {:.2f}".format(4.00*qtd))
elif n == 2:
    print("Total: R$ {:.2f}".format(4.50*qtd))
elif n == 3:
    print("Total: R$ {:.2f}".format(5.00*qtd))    
elif n == 4:
    print("Total: R$ {:.2f}".format(2.00*qtd))
elif n == 5:
    print("Total: R$ {:.2f}".format(1.50*qtd))        

