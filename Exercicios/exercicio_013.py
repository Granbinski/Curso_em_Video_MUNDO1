salario = float(input('Qual é o salário do funcionário? R$'))
valor_aumento = salario * 0.15
novo_salario = salario + valor_aumento
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(
    salario, novo_salario))
