# Desafios 46

from time import sleep
import emoji

for i in range(10, -1, -1):
    print(' -+- {:2} -+-'.format(i))
    sleep(1)

print(emoji.emojize('\nFELIZ ANO NOVO!!:sparkler:\n'))