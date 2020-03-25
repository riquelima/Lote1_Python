# **********************************************
#  Lote 01 - Exercício 24 - Estrutura Decisão
#
#  24 - Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
#
#  Programador: Henrique Souza Lima
# **********************************************

num = int(input("Digite um número:"))

if(num%2==0)and(num%3==0):
    print('O valor é divisível por 2 e por 3.')
elif (num%2 == 0):
    print("O valor é divisível por 2.")
elif(num%3==0):
    print("O valor é divisível por 3.")



