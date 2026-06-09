import subprocess
#arquivo = open("Exemplos\dados.txt","r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close
try:
    with open("Exemplos\dados.txt","r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileExistsError:
   print("Arquivo não encontrado")


#sobreescrita
with open("Exemplos\dados.txt","w") as arquivo:
    arquivo.write("Bem vindo ao python")

#adicionar novo conteúdo
with open("Exemplos\dados.txt","a") as arquivo:
    arquivo.write(" Usuário logado com suceso\n")

#abrindo em uma da minha escolha
subprocess.Popen(["code","Exemplos\dados.txt"])