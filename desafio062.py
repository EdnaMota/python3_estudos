print('     GERADOR DE P.A.    ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro}', end=' -> ')
        primeiro += razão
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('THE END')
