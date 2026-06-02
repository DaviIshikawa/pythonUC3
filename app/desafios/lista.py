""""
nome = "Bruno"
listaNomes = [ "Bruno", "Maria", "Marta", "Luiz", "Rafael"]
print(nome)
print(listaNomes)
print(len(listaNomes)) # contar quantos elementos existem
listaNomes.append("Ana") # adicionar novo elemento na lista
print(listaNomes)
print(listaNomes.index("Bruno")) # recuperar o index da pesquisa
nova_lista = [1, 5, "Kyo", "Iory"] # lista heterogenica
print(nova_lista)
#nova_lista.remove(1) # remover item da lista
#nova_lista.remove("Kyo") # remover item da lista
nova_lista.reverse()
print(nova_lista)
nova_lista.append([10,56,9]) # adiciona uma lista dentro de outra lista
print(nova_lista)
"""

supermercado = ["Pão", "Arroz", "Feijão", "Refrigerante"]
print("Arroz" in supermercado) # verifica se o elemento está na lista
print(supermercado)
print(supermercado[0]) # retorna ao primeiro item da lista
print("Uva" not in supermercado) # verifica se um elemento especifico nao esta na lista
print(supermercado[-1])
print(supermercado[-4])
numeros = [5,3,1,4,2]
#print(numeros.sort()) # ordem crescente
#numeros.sort(reverse=True) # odem decrescente

listaNumero2 = numeros.copy() # copiar lista

# fatiar lista
n1 = numeros[0]
n2 = numeros[1]
# ou
print(numeros[0:3])

print(numeros.clear) # remove todos itens da lista

# remover elementos da lista
print(numeros.pop(4)) # remover pelo index
del numeros[1]
print(numeros)
