password = 2002
attempt = 0
while attempt != password:
    attempt = int(input(""))
    if attempt == password:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")