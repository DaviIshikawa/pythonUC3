"""
op1          logico op2
operando1    >      operando2
operando1    >=      operando2
operando1    <      operando2
operando1    <=      operando2
operando1    ==      operando2
operando1    NOT      operando2
Resultados valor Trua/False
"""

num1 = float(input("Digite um número "))
num2 = float(input("Digite o segundo número "))

print("-------------------------------------")
offline = True

print("Operador > ", num1 > num2)
print("Operador >= ", num1 >= num2)
print("Operador < ", num1 < num2)
print("Operador <= ", num1 <= num2)
print("Operador == ", num1 == num2)
print("Operador != ", num1 != num2)
print(num1>num2 and num1==num2)#duas operações verdadeira(V)
print(num1>num2 or num1==num2)#uma operação verdadeira(V)

print(not offline)
