      #exercicio de somatiro de numeros pares
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
def ehPar(numero):
    r = (numero%2==0)
    return r

def somar_par(lst):
   soma = 0
   for num in lst:
      if(ehPar(num)):
        soma= soma + num
   return soma

resultado = somar_par(lst)
print(resultado)
   