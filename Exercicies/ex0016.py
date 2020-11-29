from math import trunc
num = float(input('Digit um valor: '))
print(f'O calor digita foi {num} e sua porção inteira é {trunc(num)}')
print(20 * '=')
print('Ou podemmos usar o int() para extrair apenas o valor inteiro')
print(int(num))