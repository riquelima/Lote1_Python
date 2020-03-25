# **********************************************
#  Lote 01 - Exercício 18 - Estrutura Decisão
#
#  18 - Receba 2 valores inteiros.
#  Calcule e mostre o resultado da diferença do maior pelo menos valor.
#
#  Programador: Henrique Souza Lima
# **********************************************

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

if(num1 < num2):
    resultado = num2 - num1
    print("A diferença entre", num2, " e ", num1, " = ", resultado)
elif(num2 < num1):
    resultado = num1 - num2
    print("A diferença entre", num1, " e ", num2, " = ", resultado)


