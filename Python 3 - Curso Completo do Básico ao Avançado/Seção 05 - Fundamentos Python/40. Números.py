a = 5
b = 2.5

# Verifica se é inteiro
print(b.is_integer())

# Função soma
print(int.__add__(3, 5))

# Retorna o Módulo do valor
print((-2).__abs__())
print(abs(-2))

# Decimal
from decimal import Decimal, getcontext

getcontext().prec = 4 # Precisão de 4 casas decimais 
print(Decimal(1)/Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))
