import re

CPF = input('Digite seu CPF: ')
regex = '\d{3}(\.|\s)?\d{3}(\.|\s)?\d{3}(\-|\s)?\d{2}'
validador = re.compile(regex)

if bool(validador.fullmatch(CPF)) is True:
    print('Esse é um CPF válido!')
else:
    print('Esse não é um CPF válido!')