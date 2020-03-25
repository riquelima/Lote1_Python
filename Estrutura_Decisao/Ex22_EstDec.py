# **********************************************
#  Lote 01 - Exercício 22 - Estrutura Decisão
#
#  22 - Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
#
#  Programador: Henrique Souza Lima
# **********************************************

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

if (num1 < num2):
    print(" A ordem crescente é: ", num1, num2)
else:
    print(" A ordem crescente é: ", num2, num1)

