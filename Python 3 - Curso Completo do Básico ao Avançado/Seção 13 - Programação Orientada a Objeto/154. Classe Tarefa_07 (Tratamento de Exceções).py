'''
Herança
- Classe Pai ou SuperClasse
- Classe Filha ou SubClasse
'''
from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def __iter__(self):
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    # projeto += tarefa  ->  casa += 'Lavar roupa'
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)

        return self


    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)


    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))


    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencmento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)


    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # Possível InderError
        try:
            return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))


    def __str__(self):
        return f'* {self.nome} -> {len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento


    def concluir(self):
        self.feito = True


    def __str__(self):
        status = []
        if self.feito:
            status.append(' (✔)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append(' (Vencida!)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f' (Vence em {dias} dias)')

        return f'{self.descricao}' + ''.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None


    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa

        return nova_tarefa


def main():
    casa = Projeto('Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa += Tarefa('Cuidar das plantas')
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 3)
    casa.procurar('Trocar lençóis').concluir()

    print(casa)

    # Tratamento de Exceções
    try:
        casa.procurar('ERRO').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'-> {tarefa}')
    print(casa)

    mercado = Projeto('Lista de Mercado')
    mercado.add('Suco', datetime.now() + timedelta(days=3, minutes=12))
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
