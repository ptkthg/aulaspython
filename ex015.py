produto = float (input('Qual o preço do produto? R$'))
desc = produto - (produto*5/100)
print ('O produto custa R${:.2f}, e com o desconto de 5% passou a valer R${:.2f}'.format(produto, desc))