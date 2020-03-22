# **********************************************
#  Lote 01 - Exercício 16 - Estrutura Sequencial
#
#  16 - Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes.
#  Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto).
#  A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
#
#  Programador: Henrique Souza Lima
# ***********************************************

quantidade_horas = int(input("Digite a quantidade de horas trabalhadas:"))
valor_hora = float(input("Digite o valor/hora trabalhada:"))
desconto = int(input("Digite o percentual de desconto %:"))
desconto = desconto/100
dependentes = int(input("Digite a quantidade de dependentes:"))
dependentes = dependentes * 100
salario_bruto = quantidade_horas * valor_hora
salario_liquido = salario_bruto - (salario_bruto * desconto) + dependentes
salario_liquido = salario_liquido * 30

print("O valor do salário a receber é de: ", salario_liquido)


