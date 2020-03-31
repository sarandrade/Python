# Desafios 18

from math import sin, cos, tan, radians

ang_graus = float(input('Digite um ângulo: '))

ang_rad = radians(ang_graus)

print('O seno do ângulo {}° é {:.2f}.'.format(ang_rad, sin(ang_rad)))
print('O cosseno do ângulo {}° é {:.2f}.'.format(ang_rad, cos(ang_rad)))
print('A tangente do ângulo {}° é {:.2f}.'.format(ang_rad, tan(ang_rad)))