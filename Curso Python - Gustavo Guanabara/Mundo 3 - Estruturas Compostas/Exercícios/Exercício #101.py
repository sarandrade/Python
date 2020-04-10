# Desafios 101

def voto(nasc):
    from datetime import date

    hoje = date.today().year
    idade = hoje - nasc

    if idade < 16:
        return f'Idade = {idade} => NÃO VOTA'
    elif idade < 18 or idade > 65:
        return f'Idade = {idade} => VOTO OPCIONAL'
    else:
        return f'Idade = {idade} => VOTO OBRIGATÓRIO'

print('-=-'*10)
nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(nasc))
print('-=-'*10)