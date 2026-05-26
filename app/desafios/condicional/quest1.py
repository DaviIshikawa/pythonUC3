usuario = input("Digite o nome de usuário: ")
try:
    if usuario == "admin":
        print("Acesso permitido")
except ValorError:
    print("Acesso negado")