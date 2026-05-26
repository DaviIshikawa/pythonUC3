soma = 0
valor = int(input("Digite um valor (0 para parar): "))

while valor != 0:
    soma = soma + valor
    valor = int(input("Digite um valor (0 para parar): "))

print("Total:", soma)