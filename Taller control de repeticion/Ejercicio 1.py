#entradas
print("Tenga en cuenta que K < N")
K = int(input("Ingrese el valor de K: "))
N = int(input("Ingrese el valor de N: "))
i = 0
#caja negra
while N >= K:
    print(N)
    N -= 1
    i += 1