#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

total18 = 0
totH=totM=0
while True:
    i=int(input("Informe a idade do usuário(a): "))
    if i>=18:
        total18+=1
    s = " "
    while s not in 'MF':
        s=str(input("Informe o sexo do usuário(a) [ M ] / [ F ]: ")).strip().upper()
    if s=='M':
        totH+=1
    if s=='F'or i<20:
        totM+=1
    c=" "
    while c not in 'SN':
        c=str(input("Usuário, você deseja continuar ? [ S ] / [ N ]")).strip().upper()
    if c=='N':
        break
print(f"Um total de {total18} pessoas tem idade acima de 18 anos")
print(f"Um total de {totH} homen foram/foi cadastrados")
print(f"Um total de {totM} possui menos de 20 anos de idade")
print("Fim")
