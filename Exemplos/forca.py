# Palavra secreta
palavra = "python"

# Variáveis
letras_descobertas = ""
tentativas = 0

print("=== JOGO DA FORCA ===")

# Enquanto o usuário não acertar toda a palavra
while len(letras_descobertas) < len(palavra):

    letra = input("Digite uma letra: ")
    tentativas += 1

    resultado = ""

    # Percorre cada letra da palavra
    for caractere in palavra:

        # Verifica se a letra digitada existe na palavra
        if letra == caractere:
            resultado += letra
        else:
            resultado += "*"

    print("Resultado:", resultado)
    print("Tentativas:", tentativas)

    # Se a letra estiver na palavra
    if letra in palavra and letra not in letras_descobertas:
        letras_descobertas += letra

# Mensagem final
print("\nParabéns! Você descobriu a palavra.")
print("Palavra secreta:", palavra)
print("Total de tentativas:", tentativas)