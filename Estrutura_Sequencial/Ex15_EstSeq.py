# **********************************************
#  Lote 01 - Exercício 15 - Estrutura Sequencial
#
#  15 - Receba os valores de 2 catetos de um triângulo retângulo.
#  Calcule e mostre a hipotenusa.
#
#  Programador: Henrique Souza Lima
# ***********************************************
import math
cateto1= int(input("Digite o valor do primeiro cateto:"))
cateto2= int(input("Digite o valor do segundo cateto:"))
hipotenusa = ((cateto1**2) + (cateto2**2))
hipotenusa = math.sqrt(hipotenusa)

print("A hipotenusa do triângulo = ", hipotenusa)