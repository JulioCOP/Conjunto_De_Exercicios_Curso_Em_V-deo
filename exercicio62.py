#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
#     a   b   c

print("-="*200)
n=int(input("Escreva a quantidade de termos que você deseja mostrar: "))
print("-="*200)
a=0
b=1
print("~" *200)
print("{} -> {}".format(a,b), end="" )
cont=3 #ja foram mostrados o primeiro e segundo termos em a e b
while cont<=n:
    c=a+b
    print("->{}".format(c), end="")
    a=b
    b=c
    cont+=1 #contador recebe +1, para contar os valores -> valor + 1, para assim não entrar em looping
    #ex: termo 3, assim o programa ira sempre mostrar o proximo valor até o valor limite informado em n
    #inicia no 3º termo e vai até 10º
    #sem ele teriamos números infinitos, pois o programa não iria saber o intervalor que se deseja
print("-> FIM", end="")