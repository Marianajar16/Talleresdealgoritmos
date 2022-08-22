#entrada
c=int(input("Digita la cantidad de estudiantes: "))
a=0
for i in range(1,c+1):
    altura=float(input("Digite  la altura: "))
    if(a<=altura):
        a=altura
print(a)