class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')

        self._idade = idade

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
    jose.idade = 40
    print(f'Nome: {jose.nome} | Idade: {jose.idade}')
