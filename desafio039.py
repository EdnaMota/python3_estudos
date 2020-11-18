ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
tempo1 = 18 - idade
tempo2 = idade - 18
print(f'Você tem {idade} anos.')
if idade < 18:
    print(f'Você vai se alistar ao serviço militar daqui a {tempo1} ano.')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Você já passou da idade de se alistar há {tempo2} anos.')
