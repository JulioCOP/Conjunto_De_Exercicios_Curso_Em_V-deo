#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução,s mostre a média entre todos os valore e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

media=cont=soma=0
maior=0
menor=0
r='S'
while r=='S':
    n = int(input("Digite um valor: "))
    r = str(input("Você deseja continuar ? [ S ] / [ N ]: ")).upper()
    cont+=1
    soma+=n
    media=soma/cont
    if cont==1:
        maior=menor=n       #o primeiro valor informado é sempre o maior e o menor numero
    else:
        if n>maior:         #a partir da primeira condição if, o numeros subsequentes, serão avaliados
            maior=n         #em maior e menor número de acordo com que o usuário informa ao programa
        if n<cont:
            menor=n

print("A média dos valores {} é {:.2f}".format(cont,media))
print("O menor valor é {}, enquanto que o maior valor é {}".format(menor, maior))
print("FIM DO PROGRAMA")