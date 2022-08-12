#entradas
p=int(input("Digite el valor del entero P: "))
q=int(input("Digite el valor del entero Q: "))
#caja negra
expre=(p**3+q**4-2*p**2)
if (expre<=680):
   print("P y Q satisfacen la expresión "+str(expre)) 
elif(expre>=680):
    print("P y Q no satisfacen la expresion ")