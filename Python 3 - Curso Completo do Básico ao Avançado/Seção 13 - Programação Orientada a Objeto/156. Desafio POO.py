from datetime import datetime
from Loja import Cliente, Vendedor, Compra


def main():
    vendedor = Vendedor('Túlio', 21, 10000)
    cliente = Cliente('Sara', 21)
    compra1 = Compra(vendedor, datetime.now(), 50)
    compra2 = Compra(vendedor, datetime(2018, 6, 4), 100)
    compra3 = Compra(vendedor, datetime(2016, 6, 4), 100)

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    cliente.registrar_compra(compra3)

    print(f'Cliente: {cliente}' , ': (adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')
    print(f'Total: R${cliente.total_compras()} em {len(cliente.compras)} compras')
    print(f'Dia da última compra: {cliente.get_data_ultima_compra()}')


if __name__ == "__main__":
    main()
