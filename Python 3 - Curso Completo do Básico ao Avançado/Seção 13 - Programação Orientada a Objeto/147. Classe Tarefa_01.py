from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.__feito = True


    def __str__(self):
        return self.descricao + (' (✔)' if self.__feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa.'))
    casa.append(Tarefa('Lavar prato.'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato.']

    for tarefa in casa:
        print(f'-> {tarefa}')


if __name__ == "__main__":
    main()
