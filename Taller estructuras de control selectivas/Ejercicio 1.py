#entradas
ci=float(input("Digite el capital a invertir"))
ti=float(input("Digite la tasa de interes"))
#caja negra
if(ci>100000):
 g=(ci*ti)
 #salidas
print("La ganancia sera de: "+str(g))
g1=ci+g
print("El dinero total que esta en la cuenta sera de: " +str(g1))