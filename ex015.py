dias = int(input('Digite a qtd de dias que alugou o carro: \n'))
km = float(input('Digite a qtd de km rodados: \n'))

preco = (dias * 60) + (km * 0.15)

print('Você terá que pagar um valor de R${:.2f}'.format(preco))
