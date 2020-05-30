# Trabalhos
trabalho_terça = True
trabalho_quinta = True

'''
-> Confirmando os dois => TV 50' + Sorvete
-> Confirmando apenas um => TV 32' + Sorvete
-> Nunhum confirmado: Fica em casa
'''
tv_50 = trabalho_terça and trabalho_quinta
tv_32 = trabalho_terça != trabalho_quinta
sorvete = trabalho_terça or trabalho_quinta
em_casa = not sorvete

print("TV 50' -> {}".format(tv_50))
print("TV 32' -> {}".format(tv_32))
print("Sorvete -> {}".format(sorvete))
print("Em casa -> {}".format(em_casa))
