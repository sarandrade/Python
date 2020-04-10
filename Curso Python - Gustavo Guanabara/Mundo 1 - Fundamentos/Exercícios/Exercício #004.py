# Desafio 04

n = input('Digite algo: ')

print('Seu tipo primitivo é:', type(n))
print('O valor na string é totalmente numérico?', n.isnumeric())
print('O valor na string é totalmente alfabético?', n.isalpha())
print('O valor na string é alfanumérico?', n.isalnum())
print('O valor na string está todo em maiúsculo?', n.isupper())
print('O valor na string está todo em minúsculo?', n.islower())
print('O valor na string está capitalizado?', n.istitle())