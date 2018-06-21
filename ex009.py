numInt = int(input('Gafanhoto, digite um número inteiro: \n'))

def soma(num):
    global numInt
    return num * numInt


print('=' * 20)
print('A tabuada de {} é: \n'.format(numInt))

print('{} x 0 = {}'.format(numInt, soma(0)))
print('{} x 1 = {}'.format(numInt, soma(1)))
print('{} x 2 = {}'.format(numInt, soma(2)))
print('{} x 3 = {}'.format(numInt, soma(3)))
print('{} x 4 = {}'.format(numInt, soma(4)))
print('{} x 5 = {}'.format(numInt, soma(5)))
print('{} x 6 = {}'.format(numInt, soma(6)))
print('{} x 7 = {}'.format(numInt, soma(7)))
print('{} x 8 = {}'.format(numInt, soma(8)))
print('{} x 9 = {}'.format(numInt, soma(9)))
print('{} x 10 = {}'.format(numInt, soma(10)))
