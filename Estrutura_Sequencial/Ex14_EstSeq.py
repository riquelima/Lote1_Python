# **********************************************
#  Lote 01 - Exercício 14 - Estrutura Sequencial
#
#  14 - Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
#
#  Programador: Henrique Souza Lima
# ***********************************************

angulo1 = int(input("Digite o valor do primeiro ângulo do triângulo:"))
angulo2 = int(input("Digite o valor do segundo ângulo do triângulo:"))
angulo3 = 180 - (angulo1 + angulo2)
print("O valor do terceiro ângulo = ", angulo3, " graus")