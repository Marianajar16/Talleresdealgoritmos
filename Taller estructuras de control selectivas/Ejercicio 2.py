#entrada
sb=float(input("Digite salario bruto: "))
#caja negra
if(sb<900000):
  cn=sb+(sb*0.15)
  print("salario neto es igual: "+str(cn))
else:
  cn=sb+(sb*0.12)
  print("salario neto es igual: "+str(cn))
