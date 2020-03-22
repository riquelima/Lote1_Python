# **********************************************
#  Lote 01 - Exercício 5 - Estrutura Sequencial
#
#  5 - Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0).
#  Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
#
#  Programador: Henrique Souza Lima
# **********************************************

print(' ------ CÁLCULO RAIZ QUADRADA ----- ')

#Coletando os valores de a, b e c
a = int(input("Digite um valor para a:"))
b = int(input("Digite um valor para b:"))
c = int(input("Digite um valor para c:"))

#Calculando o valor de delta
delta = ((b*b) - 4*a*c)

#Calculando as raízes
import math
raiz1 = (-(b) + math.sqrt(delta))/2*a
raiz2 = (-(b) - math.sqrt(delta))/2*a

#Mostrando o resultado
print("Raiz 1 = ", raiz1)
print("Raiz 2 = ", raiz2)

