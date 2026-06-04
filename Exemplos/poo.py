# criando base(planta do objeto)
class Carro:
    def __init__(self,motor,quant_rodas):
        self.motor = motor
        self.quant_rodas = quant_rodas

    #def __init__(self):
       # pass

    def andar(self):
        print("carro está andando")

# sem valores obrigatórios
class Conta:
    def __init__(self):
        pass

# iniciar classe com valores padrão
class funcionario:
    nome = ""
    idade = 0
    cargo = ""

# criando objeto
car1 = Carro("v8",4)
car2 = Carro("V6",4)
#car3 = Carro() # criando carro 3
#car3.motor = "V12" # atribuindo o valor a propriedade do objeto
#print(car3.motor)
#car3.andar() # executando a função(ação) do objeto

# mostrar informações do objeto
print("Carro 1 tem o motor:",car1.motor)
print("Carro 2 tem o motor:",car2.motor)

class Cliente:
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

cliente = Cliente(nome="Maria",cpf="108.454.654-35",telefone="(21)99568-6584",email="mari@gmail.com")

print("Nome:",cliente.nome)
print("CPF:",cliente.cpf)
print("Telefone:",cliente.telefone)
print("E-Mail:",cliente.email)

class aspirador:
    def aspirar(self):
        for i in range(5):
            print("O aspirador de pó está aspirando!")

    def confirmacao(self,resposta):
        if resposta =="sim":
            print("Ok,aspirador aspirando!")
        else:
            print("Ok,deixa pra outra hora!")


Aspirador = aspirador()
Aspirador.aspirar()
resposta = input("Deseja ativar o aspirador de pó?")
Aspirador.confirmacao(resposta)