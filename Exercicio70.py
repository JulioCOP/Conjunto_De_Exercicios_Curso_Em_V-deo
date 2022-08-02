#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.
soma=contp=menorpreco=cont=0
barato=" "
while True:
    produto=str(input("Informe o nome do produto que deseja comprar: ")).strip().upper()
    preco=float(input("Informe o preço do produto: R$ "))
    cont+=1
    soma+=preco
    if preco>1000:
        contp+=1
    if cont==1:
        menorpreco=preco
        barato=produto
    else:
        if preco<menorpreco:
            menorpreco=preco
            barato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input("Usuário, você deseja continuar essa operação [ S ] / [ N ] ? ")).strip().upper()[0]
    if resp=='N':
        break


print(f"O total a pagar nessa compra foi de R$ {soma:.2f}")
print(f"Um total de {contp} produtos, custam acima de R$ 1000,00")
print(f"O produto com menor preço é  {barato}")
print("FIM")