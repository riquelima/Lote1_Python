# **********************************************
#  Lote 01 - Exercício 23 - Estrutura Decisão
#
#  23 - Receba 3 valores obrigatoriamente em ordem crescente
#  e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
#
#  Programador: Henrique Souza Lima
# **********************************************

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
num3 = int(input("Digite o terceiro valor:"))
num4 = int(input("Digite o quarto valor:"))

if (num2 < num1)or(num3 < num2)or(num3<num1):
    print("Os valores precisam ser inseridos em ordem crescente! Tente de novo")
elif(num4 < num1):
    print("A ordem crescente é:", num4, num1, num2, num3)
elif(num4 < num2):
    print("A ordem crescente é:", num1, num4, num2, num3)
elif (num4 < num3):
    print("A ordem crescente é:", num1, num2, num4, num3)
else:
    print("A ordem crescente é:", num1, num2, num3, num4)






