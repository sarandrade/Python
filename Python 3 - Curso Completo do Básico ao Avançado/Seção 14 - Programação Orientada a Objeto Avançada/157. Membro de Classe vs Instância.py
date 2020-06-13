'''
Membros de instância (de objeto) vs Membros estáticos (de classe)
'''
class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome


    def das_cavernas(self):
        # Atributo de instância
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == "__main__":
    jose = Humano('José')
    # grokn = Humano('Grokn')
    # grokn.das_cavernas()
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'José.especie: {jose.especie}')
    print(f'Grokn.especie: {grokn.especie}')
