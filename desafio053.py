frase = str(input('Digite uma frase: ')).strip().upper() #strip tira espaços no comçeo e fim
palavras = frase.split() #separa as palavras numa lista
junto = ''.join(palavras) #junta as apalavras eliminando espaços internos
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
