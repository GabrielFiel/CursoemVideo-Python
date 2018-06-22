import random

primeiro = input('Primeiro aluno')
segundo = input('Segundo aluno')
terceiro = input('Terceiro aluno')
quarto = input('Quarto aluno')

ordem = [primeiro, segundo, terceiro, quarto]

print(random.sample(ordem, len(ordem)))
