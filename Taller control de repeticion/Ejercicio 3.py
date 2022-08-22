#entradas
A = int(input("Ingrese un numero A: ")) 
B = int(input("Ingrese un numero B: "))
i = 0
total = 0
lista_numeros = []
#caja negra
if A < B:
    i = A
    while i < B:
        if (i % 2) == 0:
            lista_numeros.append(i)
            total += i
        i += 1
    print(f"Los numeros pares entre {A} y {B} son: {lista_numeros} ")
    print(f"Y su sumatoria es igual a: {total}")
if B < A:
    i = B
    while i < A:
        if (i % 2) == 0:
            lista_numeros.append(i)
            total += i
        i += 1
    print(f"Los numeros pares entre {A} y {B} son: {lista_numeros} ")
    print(f"Y su sumatoria es igual a: {total:,}")

    

