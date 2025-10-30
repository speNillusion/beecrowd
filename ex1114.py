import sys

while True:
    try:
        senha = int(sys.stdin.readline())
        if senha == 2002:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break
