for i in range(1, 11):
    print(f'i = {i}', end=' ')

print()

for j in range(10):
    print(f'j = {j}', end=' ')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} x {y} = {x * y}')
    
    print('-+-'*5)
