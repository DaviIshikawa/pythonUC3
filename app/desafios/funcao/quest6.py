def menu():
    while True:
        print("\n1 - Somar")
        print("2 - Subtrair")
        print("0 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            a = int(input("Primeiro número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", a + b)

        elif opcao == 2:
            a = int(input("Primeiro número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", a - b)

        elif opcao == 0:
            print("Saindo...")
            break

menu()