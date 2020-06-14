class Animal:
    @property
    def capacidades(self):
        return ('Dormir', 'Comer', 'Beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('Estudar', 'Amar', 'Falar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('Fazer teia', 'Andar pelas paredes')

# Herança Múltipla
class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('Bater em bandidos', 'Atirar teias entre prédios')


if __name__ == "__main__":
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')
