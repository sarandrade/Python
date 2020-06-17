from functools import reduce
from operator import add

valores = [20, 52, 54, 87, 10, 5]

# Não alteram a lista valores
print(sorted(valores))
print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(list(reversed(valores)))
print(reduce(add, valores))
print(valores)

# Alteram a lista valores
valores.sort()
print(valores)
valores.reverse()
print(valores)
