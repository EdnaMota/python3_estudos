soma = 0   #acumulador
cont = 0   #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c ## ou soma += c (ele mesmo + c)
        cont = cont + 1 ## ou cont += 1 (ele mesmo + 1)
print(f'A soma de todos os {cont} valores solicitados é {soma}.')