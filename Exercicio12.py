preco = float(input('Insira o preço do produto R$'))
desconto = preco-(preco*5/100)
print('o preço do produto era: R${:.2f} com o desconto de 5% você pagara: R${:.2f}'.format(preco, desconto))
