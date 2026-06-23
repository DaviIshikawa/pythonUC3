def login():
    tentativas = 0

    while tentativas < 3:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "123":
            print("Login realizado!")
            return

        print("Dados incorretos!")
        tentativas += 1

    print("Número de tentativas excedido!")

login()