class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base*12)+self.bonus


class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario
     
    def salario_total(self):
        return self.salario_agregado.salario_anual()
    

salario = Salario(1000, 700)
emp = Empregado('Kaio', 46, salario )
print(emp.salario_total())

#Classe Salario: Esta classe tem um método de inicialização __init__ que aceita dois parâmetros, base e bonus, e atribui esses valores aos atributos self.base e self.bonus.
#Há um método chamado salario_anual, que calcula e retorna o salário anual somando o salário base multiplicado por 12 e o bônus.
#Classe Empregado:
#Esta classe também tem um método de inicialização __init__, que aceita três parâmetros: nome, idade e salario. O valor de salario é atribuído ao atributo self.salario_agregado.
#Possui um método chamado salario_total, que retorna o salário anual total do empregado, invocando o método salario_anual da instância de Salario armazenada em self.salario_agregado.
#Instanciação e Uso:
#Uma instância da classe Salario é criada com um salário base de 1000 e um bônus de 700: salario = Salario(1000, 700).
#Uma instância da classe Empregado é criada com o nome 'Kaio', idade 46 e o objeto salario como salário: emp = Empregado('Kaio', 46, salario).
#O método salario_total da instância de Empregado é chamado: emp.salario_total().
#O resultado é impresso, que é o salário anual total do empregado.