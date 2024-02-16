           #Exercicio 01

lista = [13,2,3,4,5,6,7,8,9,10,12,13,14,15]

def encontrar_minimmo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo

print(encontrar_minimmo(lista));