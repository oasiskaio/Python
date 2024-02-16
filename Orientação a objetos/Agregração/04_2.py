from contas import Conta
from clientes import Cliente
client1 = Cliente(123, "Joao", "Rua 1")
client2 = Cliente(345, "Maria", "Rua 2")
conta1 = conta([cliente1,client2], 1, 0)
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()