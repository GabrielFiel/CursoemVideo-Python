reais = float(input('Quantos reais você tem na sua carteira? \n'))
dolares = reais * (1 / 3.27)

print('Você consegue comprar ${:.2f} dólares com esse valor em reais'.format(dolares))
