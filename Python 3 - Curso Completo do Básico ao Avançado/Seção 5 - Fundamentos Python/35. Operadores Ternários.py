chuva = True

print('Hoje as roupas estão ' + ('secas.', 'molhadas.')[chuva])
print('Hoje as roupas estão ' + ('molhadas.' if chuva else 'secas.'))
