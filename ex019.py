import random

aluno = []

for x in range(4):
    aluno.append(input('Digite o nome do aluno'))

print(random.choice(aluno))
