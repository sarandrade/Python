# Desafios 49

n = int(input('Digite um número: '))

print('  {} TABUADA DE {} {}'.format('-+-', n, '-+-'))

for i in range(0, 11):
    print('[ {:2} ] X [ {} ] = [ {:2} ]'.format(i, n, i * n))