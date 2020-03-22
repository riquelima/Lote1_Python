# **********************************************
#  Lote 01 - Exercício 4 - Estrutura Sequencial
#
#  4 - Receba a temperatura em graus Celsius.
#  Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.
#
#  Programador: Henrique Souza Lima
# **********************************************

print("---- CONVERSÃO DE TEMPERATURA ---- ")
temperatura_celsius = int(input("Digite a temperadura em Celsius:"))
temperatura_fahrenheit = (9 * temperatura_celsius + 160)/5
print("A tempradura em fahrenheit = ", temperatura_fahrenheit)
