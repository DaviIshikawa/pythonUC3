def contar_pares(inicio, fim):
    contador = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            contador += 1

    return contador

print(contar_pares(1, 20))