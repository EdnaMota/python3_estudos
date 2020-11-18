n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda aula: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m}.')
if m < 5:
    print('REPROVADO!')
elif m == 5 or m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
