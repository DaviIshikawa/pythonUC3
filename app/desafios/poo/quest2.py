class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(self.nome, "Estudando.")
        

aluno1 = Aluno("Pedro")

aluno1.estudar()