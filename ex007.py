nota1 = float(input('Nota 1: \n'))
nota2 = float(input('Nota 2: \n'))
media = (nota1 + nota2) / 2

divider = '=' * 20

print(divider)
print('A média entre {} e {} é igual a {:.2f}.'.format(nota1, nota2, media))
