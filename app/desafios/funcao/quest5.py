def soma_valores():
    soma = 0

    while True:
        num = int(input("Digite um número: "))

        if num == 0:
            break

        soma += num

    print("Soma:", soma)

soma_valores()