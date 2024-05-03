A, B, C = map(float, input().split())
t = (A*C)/2
c = 3.14159 * (C**2)
tra = ((A+B)*C)/2
q = B**2
r = A*B
print("TRIANGULO: {:.3f}".format(t))
print("CIRCULO: {:.3f}".format(c))
print("TRAPEZIO: {:.3f}".format(tra))
print("QUADRADO: {:.3f}".format(q))
print("RETANGULO: {:.3f}".format(r))