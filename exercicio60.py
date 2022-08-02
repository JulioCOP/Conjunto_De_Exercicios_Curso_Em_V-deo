#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
#termo progressão aritimética an=a1+(n-1)*r

n1=int(input("Informe o primeiro termo da PA: "))
r=int(input("Informe a razão da PA: "))
cont=1
term=n1
while cont<=10:
    term += r
    cont+=1

    print("{}".format(term),end="->")
print("FIM")
