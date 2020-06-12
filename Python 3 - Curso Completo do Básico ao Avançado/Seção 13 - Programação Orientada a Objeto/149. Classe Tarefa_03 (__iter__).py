from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def __iter__(self):
        return self.tarefas.__iter__()


    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))


    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # possível InderError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'- {self.nome} -> {len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()


    def concluir(self):
        self.feito = True


    def __str__(self):
        return self.descricao + (' (✔)' if self.feito else '')


def main():
    casa = Projeto('Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()

    for tarefa in casa:
        print(f'-> {tarefa}')
    print(casa)

    mercado = Projeto('Lista de Mercado')
    mercado.add('Suco')
    mercado.add('Café')
    mercado.add('Laranja')
    mercado.add('Leite')
    print(mercado)

    comprar_leite = mercado.procurar('Leite')
    comprar_leite.concluir()

    for produto in mercado:
        print(f'-> {produto}')
    print(mercado)


if __name__ == "__main__":
    main()
