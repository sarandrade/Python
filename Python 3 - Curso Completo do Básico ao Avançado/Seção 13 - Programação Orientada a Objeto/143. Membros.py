# A classe representa um tipo de dado personalizado
class Data:
    # Todo método começa com "self"
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data() # Criando um objeto
d1.dia = 5
d1.mes = 12
d1.ano = 2019

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020

print(d1.to_str())
print(d2.to_str())

# Outra Alternativa

class DataAlternativa:
    # Todo método começa com "self"
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = DataAlternativa() # Criando um objeto
d1.dia = 5
d1.mes = 12
d1.ano = 2019

d2 = DataAlternativa()
d2.dia = 7
d2.mes = 11
d2.ano = 2020

print(d1)
print(d2)
