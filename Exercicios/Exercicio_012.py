preco_produto = float(input('Digite o preço do produto: '))
desconto = preco_produto * 0.05
valor_com_desconto = preco_produto - desconto
print('O valor do produto com desconto é R${:.2f}'.format(valor_com_desconto))
