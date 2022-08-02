#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

n1=int(input("Digite o primeiro termo de uma PA: "))
r=int(input("Digite o valor da razão dessa PA: "))
cont=1
term=n1
total=0 #variavel total, é quantidade de termos que será mostrada, iniciando em 0
mais=10 #programa começa com 10 termos, variavel que mostra a qtd de termos
while mais!=0:            #enquanto o mais for diferente de 0
    total=total+mais #variavel a ser mostrado é igual ao total + variavel mais( que é da quantidade t4ermos que usuario deseja)
    while cont<total:
        term+=r
        cont+=1
        print("{}".format(term), end="->")
    print("PAUSA")
    mais= int(input("Quantos termos a mais você deseja colocar na PA: "))
print("PA finalizada com {} termos" .format(total))