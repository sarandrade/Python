# A classe representa um tipo de dado personalizado
class Data:
    # Todo método começa com "self"
    def __init__(self, dia=1, mes=1, ano=1970): # Parâmetros com valor padrão
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019) # Construtor -> Cria um objeto

d2 = Data(7, 11, 2020)
d2.dia = 31

d3 = Data()

d4 = Data(ano=2020)

print(d1)
print(d2)
print(d3)
print(d4)
