class Salario:
    def __init__(self, base, bonus):
        self.base = base   #1000
        self.bonus = bonus  #700
    
    def salario_anual(self):
        return (self.base*12)+self.bonus
          #1000 x 12 + 700 = 12700
class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade 
        self.salario_agregado = salario
     
    def salario_total(self):
        return self.salario_agregado.salario_anual()
    
salario = Salario(1000, 700)
emp = Empregado('Kaio', 46, salario)
print(emp.salario_total())