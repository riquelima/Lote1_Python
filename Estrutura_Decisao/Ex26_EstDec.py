# **********************************************
#  Lote 01 - Exercício 26 - Estrutura Decisão
#
#  26 - Receba 2 números inteiros.
#  Verifique e mostre se o maior número é múltiplo do menor.
#
#  Programador: Henrique Souza Lima
# **********************************************

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if(num2 > num1):
    multiplo = num2%num1
if(multiplo==0):
    print("O número ", num2, " é múltiplo de ", num1)
elif(multiplo >= 1):
    print("O número ", num2, " não é múltiplo de ", num1)

if (num1 > num2):
    multiplo = num2 % num1
if(multiplo==0):
    print("O número ", num1, " é múltiplo de ", num2)
elif (multiplo >= 1):
    print("O número ", num1, " não é múltiplo de ", num2)



