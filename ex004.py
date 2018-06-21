something = input('Digite alguma coisa: \n')
tipoVar = type(something)

print('O tipo dessa variável é {}'.format(tipoVar))

print('É um número?', something.isnumeric())
print('É do alfabeto?', something.isalpha())
print('É alfanumérico?', something.isalnum())
print('É decimal?', something.isdecimal())
print('Está em maiúscula?', something.isupper())
