class Veiculo: 
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome 
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'Quilometros percorridos por litros = ^{self.quilometro_litro}')

    def capacidade_assentos(self, capacidade):
        print(f'Capacidade de assentos: {capacidade}')


modelo_carro = Veiculo("fusca", 180, 10)
modelo_carro.toStr()


#Exercicio-01  Crie uma classe filha (onibus) que herdará todos os atributos de veiculos

class Onibus(Veiculo):
    pass


#Exercicio-02  Modificar a classe filha "Onibus", de modo que ela forneça a quantidade 
#de assentos. Além disso, o valor desse parâmetro deve ser 70.


Onibus_escolar = Onibus("Scania", 120, 8)
Onibus_escolar.toStr()
Onibus_escolar.capacidade_assentos(72)