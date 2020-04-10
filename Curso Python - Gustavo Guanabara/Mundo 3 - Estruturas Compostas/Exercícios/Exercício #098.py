# Desafios 98

from time import sleep

def contagem(ini, fim, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=-'*12)
    print(f'Contagem de {ini} até {fim} de {p} em {p}: ')
    
    if ini < fim:
        for n in range(ini, fim + 1, p):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print('\n>>> FIM >>>')
    else:
        cont = -p
        for n in range(ini, fim -1, cont):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print('\n>>> FIM >>>')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-=-'*15)
print('Agora é sua vez de personalizar a contagem...')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)