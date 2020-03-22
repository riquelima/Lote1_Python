# **********************************************
#  Lote 01 - Exercício 12 - Estrutura Sequencial
#
#  12 - Receba o ano de nascimento e o ano atual.
#  Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
#
#  Programador: Henrique Souza Lima
# ***********************************************

print(" --------- CÁLCULO DE IDADE --------- ")
ano_nascimento = int(input("Digite o ano de nascimento:"))
ano_atual = int(input("Digite o ano atual:"))
idade_atual = ano_atual - ano_nascimento
idade_futura = idade_atual + 17

print("Sua idade atual é = ", idade_atual)
print("Sua idade em 17 anos será = ", idade_futura)
