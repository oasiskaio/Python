class conta:
    def __init__(self, nome, cpf, nRua, idade):
        self.nome = nome
        self.cpf = cpf
        self.nRua = nRua
        self.idade = idade
    def imprimir(self):
        print (self.nome,"tem", self.idade ,"mora no endereço", self.nRua ,"e seu cpf é,", self.cpf);
    
p = conta("Kaio", "22222", 6, "19")