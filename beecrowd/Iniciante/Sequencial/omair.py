a, b, c = map(int, input().split())

maiorab = (a+b+abs(a-b))/2
maiorxc = int((maiorab+c+abs(maiorab-c))/2)
print("{} eh o maior".format(maiorxc))