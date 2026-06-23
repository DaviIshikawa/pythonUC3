def imprimir_impares():
    for i in range(1, 51):
        if i % 7 == 0:
            continue

        if i % 2 != 0:
            print(i)

imprimir_impares()