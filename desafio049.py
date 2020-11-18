from time import sleep
t = int(input('Digite um número para ver sua tabuada: '))
print('Calculando...')
sleep(2)
print('-' * 12)
for num in range(11): #conta do 1 ao 10
    print(f'{t} x {num:2} = {t * num}') #:2 põe 2 casas decimais
'''print(f'{t} x {1:2} = {t * 1}')
print(f'{t} x {2:2} = {t*2}')
print(f'{t} x {3:2} = {t*3}')
print(f'{t} x {4:2} = {t*4}')
print(f'{t} x {5:2} = {t*5}')
print(f'{t} x {6:2} = {t*6}')
print(f'{t} x {7:2} = {t*7}')
print(f'{t} x {8:2} = {t*8}')
print(f'{t} x {9:2} = {t*9}')
print(f'{t} x {10:2} = {t*10}')'''
print('-' * 12)