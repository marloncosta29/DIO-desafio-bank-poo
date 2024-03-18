import textwrap
from Deposit import Deposit



def menu():
    menu = """\n
        ============= MENU =============
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
    """
    return input(textwrap.dedent(menu))

def filter_customer(cpf, customers):
    filtred_customers = [customer for customer in customers if customer.cpf == cpf]
    return filtred_customers[0] if filtred_customers else None

def deposit(customers):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers=customers)

    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return

def main():
    customers = []
    assounts = []

    while True:
        option = menu()

        if option == 'd':
            pass