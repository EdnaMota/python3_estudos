print('     GERADOR DE P.A.    ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{primeiro}', end=' -> ')
    primeiro += razão
    cont += 1
print('THE END')
