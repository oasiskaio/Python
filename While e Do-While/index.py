palavra = ('sair')
while (palavra != 'sair'):
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')



while True: 
    palavra = ('sair')
    if palavra == 'sair':
     print("Voce digitou sair e agora está fora do laço")
     break
    else: 
     print("Digite 'sair' para sair do laço")



#exercicio
s = 0 
a = 1
while s < 5:
   s = 3*a
   a += 1
   print(s)  #resultado = (3,6)


#exercicio 2
s = 0
for i in range(5): #(i vai receber 0,1,2,3,4)
  s += 3*i #s vai ganhar o priprio valor * a crescente dos valores i
print(s) #print esta fora do laço, entao executará só uma vez



     