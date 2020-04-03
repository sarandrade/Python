# Desafios 55

maior = 0
menor = 0

for i in range(0, 5):
   peso = float(input('Digite o peso: '))

   if i == 0:
        maior = peso 
        menor = peso
   else:
     if peso > maior:
          maior = peso
     if peso < menor:
          menor = peso

print('O maior peso foi {}Kg.'.format(maior))
print('O menor peso foi {}Kg.'.format(menor))