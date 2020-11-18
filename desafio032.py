from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year ## pega o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: ## ano bissexto = a cada 4 anos exceto anos múltiplos de 100 que não são múltiplos de 400
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')