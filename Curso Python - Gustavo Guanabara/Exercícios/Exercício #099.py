# Desafios 99

from time import sleep

def maior(*num):
    print('-=-'*10)
    print('Analisando os valores passados...')
    sleep(1)
    
    for n in range(0, len(num)):
        print(num[n], end=' ', flush=True)
        sleep(0.5)

        if n == 0 or num[n] > maior: 
            maior = num[n]

    sleep(1)
    print(f'\nForam informados {len(num)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    sleep(1)

maior(1, 5, 7, 8, 6)
maior(8, 5, 4)
maior(8, 5, 4, 8, 9, 10)