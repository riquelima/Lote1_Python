# **********************************************
#  Lote 01 - Exercício 25 - Estrutura Decisão
#
#  25 - Receba a hora de início e de final de um jogo (HH,MM) sabendo que o tempo máximo
#  é de 24 horas e pode começar num dia e terminar noutro.
#
#  Programador: Henrique Souza Lima
# **********************************************

hora_inicio = int(input("Digite a hora inicial do jogo:"))
min_inicial = int(input("Digite o minuto inicial do jogo:"))
hora_final = int(input("Digite a hora final do jogo:"))
min_final = int(input("Digite o minuto final do jogo:"))

hora_jogo = hora_final - hora_inicio
min_jogo = min_final - min_inicial

print("O tempo total do jogo foi de ", hora_jogo, ":", min_jogo)
