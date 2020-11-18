ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 20:
    print('SÊNIOR.')
else:
    print('MASTER.')
