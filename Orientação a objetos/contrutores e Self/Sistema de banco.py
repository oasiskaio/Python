class Conta:
   def __init__(self, numero, cpf, nome_titular, saldo):
      self.numero = numero
      self.cpf = cpf
      self.nomeTitular = nome_titular
      self.saldo = saldo
   def depositar(self, valor):
      self.saldo += valor
   def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         return True

   def gerar_extrato(self):
        print(f"Número: {self.numero}\n nCpf: {self.cpf}\n nSaldo:{self.saldo}")

   def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
           return "Não existe saldo suficiente"
        else:
           conta_destino.depositar(valor)
           self.saldo -= valor
        return "Transferencia Realizada"


conta1 = Conta(numero="1234", cpf="211714747", nome_titular="Kaio", saldo=1000.0)

conta1.depositar(500.0)
conta1.sacar(200.0)

conta2 = Conta(numero="4444", cpf="108797707", nome_titular="patricia", saldo=500.0)

resultado_transferencia = conta1.transfere_valor(conta_destino=conta2, valor=300.0)

conta1.gerar_extrato()
conta2.gerar_extrato()

print(resultado_transferencia)