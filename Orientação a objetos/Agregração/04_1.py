class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero 
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            return ("o valor digitado é maior do que o contido")             
        else: 
            self.saldo -= valor
            return True
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else: 
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")
    def gerarsaldo(self):
        print(f"Numero:{self.numero} saldo: {self.saldo}")


#Um programa testecontas.py deve ser criado para ser usado na instanciação
#  dos objetos das duas classes e gerar as transações realizadas nas 
# contas dos clientes.

