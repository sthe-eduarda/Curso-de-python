something = input('Digite algo:')
print('Seu tipo primitivo é:', type(something))
print('É alfabetico(a)?', something.isalpha())
print('É númerioco?', something.isnumeric())
print('É alfanumerico?', something.isalnum())
print('Faz parte da abela Acii?', something.isascii())
print('Possui apenas decimeis?', something.isdecimal())
print('Possui apenas digitos?', something.isdigit())
print('É um identificador?(Possui apenas str alfanumericas, número (0-9) ou/e "_"):', something.isidentifier())
print('Possui algum caracter em letra maiúscula?', something.islower())
print('Existe algum espaço?', something.isspace())
print('Todas as palavras começam com uma letra maiúscula?', something.istitle())
print('Todos os caracteres estão em maiúsculo?', something.isupper())
print('É possivvel "imprimir"', something.isprintable())
