"""
for numero in range(5):
    print(numero)
    
for numero in range(0,11,2):
    print(numero)
"""

numero = int(input("digite um valor:"))

for y in range(1, 11):
    print(numero, "x", y, "=", numero * y)

contador = 0
while contador<5:
    print(contador)
    contador += 1
    #contador = contador +1

for numero in range(0):
    if numero == 5:
        break
    print(numero)

for numero in range(10):
    if numero == 5:
        continue
    print(numero)