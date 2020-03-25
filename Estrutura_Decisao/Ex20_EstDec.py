# **********************************************
#  Lote 01 - Exercício 20 - Estrutura Decisão
#
#  20 - Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula AX²+BX+C=0.
#  Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
#
#  Programador: Henrique Souza Lima
# **********************************************

print("------------ CALCULADORA DE EQUAÇÃO 2º GRAU ----------------")


a = int(input("Digite um valor para a:"))
b = int(input("Digite um valor para b:"))
c = int(input("Digite um valor para c:"))

delta = (b**2)-(4*a*c)

if (delta < 0):
    print("Valor de delta menor que 0: Não existe raiz real.")
elif(delta == 0):
    import math
    raiz1 = -(b) + math.sqrt(delta)/2*a
    print("Valor de delta igual a 0: Duas raizes reais = ", raiz1)
elif(delta > 0):
    raiz1 = -(b) + math.sqrt(delta) / 2*a
    raiz2 = -(b) - math.sqrt(delta) / 2*a
    print("Valor de delta maior que 0: Duas raizes reais:")
    print("Raizes: ", raiz1, " e ", raiz2)
