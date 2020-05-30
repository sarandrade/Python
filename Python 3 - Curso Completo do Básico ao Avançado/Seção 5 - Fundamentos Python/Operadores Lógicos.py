# OR
print(True or False)
'''
-> Tabela da Verdade - OR
  True  or True  => True
  True  or False => True
  False or True  => True
  False or False => False
'''

# AND
print(7 != 2 and 7 > 5)
'''
-> Tabela da Verdade - AND
  True  and True  => True
  True  and False => False
  False and True  => False
  False and False => False
'''

# XOR
'''
-> Tabela da Verdade - XOR
  True  != True  => False
  True  != False => True
  False != True  => True
  False != False => False
'''

# Operador de Negação (unário)
'''
not True  => False
not False => True
'''

# Operação bit-a-bit
'''
AND (&)
3 = 11
2 = 10
_ = 10 = 2
'''
print(2 & 3)

'''
OR (|)
3 = 11
2 = 10
_ = 11 = 3
'''
print(3 | 2)

'''
XOR (^)
3 = 11
2 = 10
_ = 01 = 1
'''
print(3 ^ 2)

# Exemplo 
saldo = 1000
salario = 4000
despesas = 3967

saldo_positivo = saldo > 0
salario_controlado = (salario - despesas) >= 0.2 * salario

meta = saldo_positivo and salario_controlado

print(meta)
