# **********************************************
#  Lote 01 - Exercício 13 - Estrutura Sequencial
#
#  13 - Receba a quantidade de alimento em quilos.
#  Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
#
#  Programador: Henrique Souza Lima
# ***********************************************

quantidadekg = int(input("Digite a quantidade de alimento em quilos:"))
quantidadeg = quantidadekg*1000
duracao = quantidadeg/50

print("A quantidade ", quantidadekg, "Kg durará ", duracao, " dias")

