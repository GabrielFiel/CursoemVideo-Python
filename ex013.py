salario = float(input('Digite o seu salário: \n'))
novoSalario = salario * 1.15
diferenca = novoSalario - salario
print('Seu novo salário com 15% de aumento é R${:.2f}.'.format(novoSalario))
print('Uma diferença de R${:.2f}.'.format(diferenca))
