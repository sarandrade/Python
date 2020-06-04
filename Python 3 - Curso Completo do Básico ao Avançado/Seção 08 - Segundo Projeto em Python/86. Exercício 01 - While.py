# Sequência de Fibinacci
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(limite):
    primeiro = 0
    segundo = 1
    print(f'{primeiro}, {segundo}', end=', ')
    # whilw True: -> While infinito
    while segundo < limite:
        primeiro, segundo = segundo, primeiro + segundo
        print(f'{segundo}', end=', ')

if __name__ == '__main__':
    fibonacci(150)
