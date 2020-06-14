from abc import ABCMeta, abstractproperty

# Classe Abstrata
class Humano(metaclass=ABCMeta):
    # Atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Propriedade Abstrata
    @abstractproperty
    def inteligente(self):
        pass

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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == "__main__":
    # Não é possível instanciar uma classe abstrata
    try:
        anonimo = Humano('John Doe')
        print(anonimo.inteligente)
    except TypeError:
        print('Não é possível instanciar uma classe abstrata!')

    jose = HomoSapiens('José')
    print('{} da classe {} : inteligente = {}'.format(jose.nome, jose.__class__.__name__, jose.inteligente))

    grokn = HomoNeanderthalensis('Grokn')
    print('{} da classe {} : inteligente = {}'.format(grokn.nome, grokn.__class__.__name__, grokn.inteligente))
