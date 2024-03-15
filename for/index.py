
nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra)




nomes = ["Kaio", "luiz", "carlos", "Guilherme", "joão"]
for nome in nomes:
    print(nome)




for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')