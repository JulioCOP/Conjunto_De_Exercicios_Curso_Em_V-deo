#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont=soma=n=0

n=int(input("Digite um número inteiro: "))
print("DIGITE 999, CASO DESEJA PARAR !")
while n!=999:
    soma += n
    cont += 1
    n=int(input("Digite um número inteiro: "))
    print("DIGITE 999, CASO DESEJA PARAR !")
#O comando n, para digitar um valor, deve ficar após os comandos de soma e cont, pois assim
# essa condção não entra no intervalo. Ou seja, ao digitar um valor igual a 999, o programa
#obrigatoriamente exclui 999, pois ele está fora da condição imposta por "while"

print("\nForam digitados {} numeros".format(cont))
print("Totalizando uma soma de {}" .format(soma))
print("FIM")

