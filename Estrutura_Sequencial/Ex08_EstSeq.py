# **********************************************
#  Lote 01 - Exercício 8 - Estrutura Sequencial
#
#  8 -Receba o valor de um depósito em poupança.
#  Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
#
#  Programador: Henrique Souza Lima
# ***********************************************

print(" ----------- CÁLCULO RENDIMENTO POUPANÇA ---------------- ")
valor = float(input("Digite o valor depositado:"))
rendimento = ((valor*0.13)+valor)

print("O valor após um mês de rendimento é = ", rendimento)