from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1 #somar mais essa pessoa se ela for menor de 21
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.\nE também tivemos {totmenor} pessoas menores de idade.')