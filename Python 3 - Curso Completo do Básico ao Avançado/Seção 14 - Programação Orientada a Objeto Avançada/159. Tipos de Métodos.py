'''
-> Método de Instância - recebe self como sendo a instância e primeiro parâmetro
-> Método de Classe - recebe uma classe primeiro parâmetro obrigatoriamente
-> Método de Estático - não recebe nenhum parâmetro na definição do método
'''
class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome

    # Método de Instância
    def das_cavernas(self):
        # Atributo de instância
        self.especie = 'Homo Neanderthalensis'
        return self

    # Método Estático
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')

        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # Método de Classe
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class HomoNeanderthalensis(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = HomoSapiens('José')
    grokn = HomoNeanderthalensis('Grokn')

    print(f'-> Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'-> Evolução (a partir da instância): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Homo Neanderthalensis evoluído? {HomoNeanderthalensis.is_evoluido()}')
    print(f'José é evoluído? {jose.is_evoluido()}')
    print(f'Grokn evoluído? {grokn.is_evoluido()}')
