valor = 20 

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero = int(input("SELECIONE UM NUMERO"))
    multiplica(numero)

if __name__ == "__name__":
    main()
#
# # Quando um script python é executado, a variável reservada
# # NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE,
# então o que está no corpo do IF será executado. 
# No caso, é um chamado ao método main do script