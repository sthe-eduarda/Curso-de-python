import random
n1 = input('aluno 1:')
n2 = input('aluno 2:')
n3 = input('aluno 3:')
n4 = input('aluno 4:')
lista = [n1, n2, n3, n4]
random.suffle(lista)
print(f'A ordem de apresentação será: {lista}')