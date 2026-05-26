palavra = "python"

letras_descobertas = ""
tentativas = 0

print("=== Jogo da Forca ===")

while len(letras_descobertas) < len(palavra):

    letra = input("Digite uma letra: ")
    tentativas += 1

    resultado = ""

    for caractere in palavra:

        if letra == caractere:
            resultado += letra
        else:
            resultado += "*"

    print("Resultado:", resultado)
    print("Tentativas:", tentativas)

    if letra in palavra and letra not in letras_descobertas:
        letras_descobertas += letra

print("\nParabéns! Você descobriu a palavra.")
print("Palavra secreta:", palavra)
print("Total de tentativas:", tentativas)