# Desafios 67

while True:
    num = int(input('Quer ver a tabuada de qual número? '))

    if num < 0:
        break

    print('-'*25)
    for i in range(1, 11):
        print(f'[ {i:2} ] x [ {num} ] = [ {num*i:2} ]')
    print('-'*25)

print('Programa encerrado...')
