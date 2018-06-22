nome = input('Digite seu nome completo: \n')

maiuscula = nome.upper()
minuscula = nome.lower()
qtdLetras = len(nome.replace(' ', ''))
letrasPrimeira = len(nome.split()[0])

print('O seu nome em maiúscula é {}.'.format(maiuscula))
print('O seu nome em minúscula é {}.'.format(minuscula))
print('O seu nome possui {} letras.'.format(qtdLetras))
print('O numero de letras do seu primeiro nome é {}.'.format(letrasPrimeira))
