from time import sleep
dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.1f} km.')
sleep (2)
if dist <= 200:
    print(f'E o preço da sua passagem será de R$ {(dist*0.50):.2f}.')
else:
    print(f'E o preço da sua passagem será de R$ {(dist*0.45):.2f}.')




