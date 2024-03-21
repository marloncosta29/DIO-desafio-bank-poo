import textwrap
from Deposit import Deposit
from Withdraw import Withdraw
from Account import Account
from CurrentAccount import CurrentAccount
from PersonCustomer import PersonCustomer
from typing import List


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

def filter_customer(cpf, customers) -> PersonCustomer:
    filtred_customers = [customer for customer in customers if customer.cpf == cpf]
    return filtred_customers[0] if filtred_customers else None

def get_customer_account(customer: PersonCustomer) -> Account:
    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return
    return customer.accounts[0]

def deposit(customers):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers=customers)

    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return
    value = float(input("Informe o valor deposito: "))
    transaction = Deposit(value)
    account = get_customer_account(customer)
    if not account:
        return
    customer.do_transaction(account, transaction)

def withdraw_value(customers: List[PersonCustomer]):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers=customers)
    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return
    value = float(input("Informe o valor deposito: "))
    transaction = Withdraw(value)
    account = get_customer_account(customer)
    if not account:
        return
    customer.do_transaction(account, transaction)

def show_statment(customers: List[PersonCustomer]):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers)
    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return
    account = get_customer_account(customer)
    if not account:
        return
    print("\n================ EXTRATO ================")
    transactions = account.history.transactions
    statment = ""
    print(transactions)

    if not transactions:
        statment = "Não foram realizadas movimentações."
    else:
        for transaction in transactions:
            statment += f"\n{transaction['tipo']}:\n\tR$ {transaction['valor']:.2f}"

    print(statment)
    print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
    print("==========================================")

def create_customer(customers: List[PersonCustomer]):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers)
    if customer:
        print("\n@@@ Cliente ja cadastrado @@@")
        return
    name = input("Informe o nome completo: ")
    date_of_birth =  input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    customer = PersonCustomer(name, date_of_birth, cpf, address)
    customers.append(customer)
    print("\n=== Cliente criado com sucesso! ===")

def create_account(account_number: int, customers: List[PersonCustomer], accounts: List[Account]):
    cpf = input('Informe o CPF do cliente: ')
    customer = filter_customer(cpf, customers)
    if not customer:
        print("\n@@@ Cliente não encontrado @@@")
        return
    account = CurrentAccount.new_account(customer, account_number)
    accounts.append(account)
    customer.accounts.append(account)
    print("\n=== Conta criada com sucesso! ===")

def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))

def main():
    customers: List[PersonCustomer] = []
    accounts = []

    while True:
        option = menu()

        if option == 'd':
            deposit(customers)
        elif option == 's':
            withdraw_value(customers)
        elif option == "e":
            show_statment(customers)
        elif option == "nu":
            create_customer(customers)
        elif option == "nc":
            account_number = len(accounts) + 1
            create_account(account_number, customers, accounts)
        elif option == "lc":
            list_accounts(accounts)
        elif option == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
main()