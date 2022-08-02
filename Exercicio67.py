#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.

from time import sleep
n=c=cont=0

while True:
    n=int(input("Digite um número: "))      #condição que se repete infitamente
    print('~'*50)
    if n<0:               #ocorre a verificação se o número informado pelo usuário é positivo e negativo
        break
    for c in range(1,11):       #condição for para estabelecer os intervalo da tabuada.
        cont+=1                 #para esse exercicio foi considerado o intervalo até 10
        print(f"{n} x {c} = {n * c}")   #número informado pelo usuário x contador
    print('~'*50)                       #o contador representa os números do intervalo de 1 a 10


print("FINALIZANDO O PROGRAMA")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(1)
print("\nFIM")

